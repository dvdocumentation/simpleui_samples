
def settings_on_create(hashMap,_files=None,_data=None):
   
    if hashMap.containsKey("load")!=True:
        hashMap.put("get_face_recognition_url","face_recognition_url")  
        hashMap.put("load","")
    if hashMap.containsKey("face_recognition_url")!=True: #face_recognition_url - зарезервированная переменная сервера распознавания лиц
        hashMap.put("face_recognition_url","http://127.0.0.1:2050")
    elif hashMap.get("face_recognition_url")=='null':
        hashMap.put("face_recognition_url","http://127.0.0.1:2050")
           

    return hashMap 


def settings_input(hashMap,_files=None,_data=None):
   
    if hashMap.get("listener")=="btn_save":
        hashMap.put("put_face_recognition_url",hashMap.get("face_recognition_url"))
 
    return hashMap 


def training_on_create(hashMap,_files=None,_data=None):
   
    if hashMap.containsKey("load")!=True: # такую конструкцию имеет смысл использвоать в "При запуске" чтобы не было зацикливания
        hashMap.put("get_face_recognition_url","face_recognition_url")  
        hashMap.put("load","")
           

    return hashMap 

def training_input(hashMap,_files=None,_data=None):
   
    hashMap.put("RunCV","Обучение CV")
    hashMap.put("FinishProcess","")
 
    return hashMap 

def training_on_create_cv(hashMap,_files=None,_data=None):
   
    hashMap.put("title","Обучение:"+hashMap.get("name"))
           

    return hashMap 

def training_cv_action(hashMap,_files=None,_data=None):
   
    if hashMap.get("listener")=="complete":
        hashMap.put("toast","Обучение завершено")
    if hashMap.get("listener")=="Завершить" or hashMap.get("listener")=="complete":
        hashMap.put("FinishProcess","")
 
    return hashMap 

def prediction_on_create(hashMap,_files=None,_data=None):
   
    if hashMap.containsKey("load")!=True: # такую конструкцию имеет смысл использвоать в "При запуске" чтобы не было зацикливания
        hashMap.put("get_face_recognition_url","face_recognition_url")  
        hashMap.put("load","")
 
    return hashMap 
   