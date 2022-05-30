import cv2
import numpy as np
from PIL import Image
import os
from flask import Flask
import json
from flask import request
import io
import base64
from base64 import decodestring
from pathlib import Path
from flask import jsonify, make_response

COUNT_IMAGES_FOR_TRAIN = 30
app = Flask(__name__)

@app.route('/add', methods=['POST']) #добавление лиц для обучения
def add():
   return save_picture_b(request.get_data(),request.args.get("name"))
  
@app.route('/train', methods=['POST']) #ручной запуск переобучения елси требуется
def train():
    train_dataset()
    return "end"    

path = 'dataset'
APP_ROOT = os.path.dirname(os.path.realpath(__file__))

DATASET_F = os.sep+path+os.sep
DATASET_FOLD = APP_ROOT+DATASET_F

Path(DATASET_FOLD).mkdir(parents=True, exist_ok=True)

face_names = []  
facePaths = []

facePaths = [os.path.join(path,f) for f in os.listdir(path)]     
for facePath in facePaths:
        facedirname = os.path.basename(os.path.normpath(facePath))
        face_names.append(facedirname)  

recognizer = cv2.face.LBPHFaceRecognizer_create() #создаем объект для распознавания
if os.path.isfile(APP_ROOT+os.sep+'trainer.yml'): #если обученная модель есть - читаем ее
    recognizer.read(APP_ROOT+os.sep+'trainer.yml')

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #детектор -каскад Хаара

# читаем записанные изображения лиц и метки
def getImagesAndLabels(path):

    face_names = []  
    

    facePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    for facePath in facePaths:
        facedirname = os.path.basename(os.path.normpath(facePath))
        face_names.append(facedirname)  

    
    faceSamples=[]
    ids = []
    for facePath in facePaths:
        next(os.walk('.'))[1]
        facedirname = os.path.basename(os.path.normpath(facePath))
        #face_names.append(facedirname)    
        imagePaths = [os.path.join(facePath,f) for f in os.listdir(facePath)]  

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L') # grayscale
            img_numpy = np.array(PIL_img,'uint8')
            id =face_names.index(facedirname)
            faces = detector.detectMultiScale( 
            img_numpy,
            scaleFactor = 1.2,
            minNeighbors = 5,
       )

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
    return faceSamples,ids

def train_dataset():    #переобучение
    face_names.clear()
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    # Сохраняем модель
    recognizer.write(APP_ROOT+os.sep+'trainer.yml') 
  
#Сохранение картинки из Base64
def save_picture(file_or_bytes,name):
   
    #image = Image.fromstring('RGB',decodestring(file_or_bytes))
    
    UPLOAD_FOLD = os.sep+path+os.sep+name+os.sep
    UPLOAD_FOLDER = APP_ROOT+UPLOAD_FOLD

    Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

    listfiles = os.listdir(UPLOAD_FOLDER) 
    number_files = len(listfiles)
    number_files+=1

    with open(UPLOAD_FOLDER+"face_"+str(number_files)+".jpg", "wb") as fh:
        fh.write(base64.decodebytes(file_or_bytes.encode()))

    if number_files>=COUNT_IMAGES_FOR_TRAIN:
        train_dataset()
        return "-1" #stop activeCV train mode

    return json.dumps({"id":"Обучение","confidence":str(number_files)+" из "+str(COUNT_IMAGES_FOR_TRAIN)+"..."})    
    #image.save(UPLOAD_FOLDER+name+".png", format="PNG")

#сохранение картинки в бинарном виде
def save_picture_b(file_or_bytes,name): 
    #image = Image.fromstring('RGB',decodestring(file_or_bytes))
  
    UPLOAD_FOLD = os.sep+path+os.sep+name+os.sep
    UPLOAD_FOLDER = APP_ROOT+UPLOAD_FOLD

    Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
    listfiles = os.listdir(UPLOAD_FOLDER) 
    number_files = len(listfiles)
    number_files+=1

    with open(UPLOAD_FOLDER+"face_"+str(number_files)+".jpg", "wb") as fh:
        fh.write(file_or_bytes)

    if number_files>=COUNT_IMAGES_FOR_TRAIN:
        train_dataset()
        return "-1" #особый код для SimpleUI - остановить обучение

    return json.dumps({"id":"Обучение","confidence":str(number_files)+" из "+str(COUNT_IMAGES_FOR_TRAIN)+"..."})        
    
@app.route('/predict', methods=['POST']) #запрос на распознавание
def predict():


    face_names = []  
    facePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    for facePath in facePaths:
        facedirname = os.path.basename(os.path.normpath(facePath))
        face_names.append(facedirname)  

    request.encoding='utf-8'
    #jresponse = request.json 
    #save_picture(jresponse['image'],jresponse['name'])
    #image = base64.b64decode(str(jresponse['image']))       
    image = request.get_data()
 
    PIL_img = Image.open(io.BytesIO(image)).convert('L') # grayscale
    img_numpy = np.array(PIL_img,'uint8')
    
    faces = detector.detectMultiScale( 
            img_numpy,
            scaleFactor = 1.2,
            minNeighbors = 5,
       )

    d = {"id":"","confidence":"--","info":""}

    for(x,y,w,h) in faces:
        
        id, confidence = recognizer.predict(img_numpy[y:y+h,x:x+w])
       
        # Точность больше 100 - ошибка
        if (confidence < 100):
            id = face_names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
       
        d = {"id":id,"confidence":confidence,"info":""}
        
    return make_response(jsonify(d), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2050,debug=True)