from flask import Flask
from flask import request
from flask import send_file


import json
app = Flask(__name__)

goods_sample = [{"barcode":"740617303506","sku":"Kingston SSD M2 512Mb"},{"barcode":"8901043000427","sku":"SiliconePower SSD 256Mb"},{"barcode":"4009932559132","sku":"Samsung SSD 1024 Mb"}]



@app.route('/download', methods=['GET'])
def download():
    filename = 'video_2022-10-06_12-39-52.mp4'
    return send_file(filename, mimetype='video/mp4')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
      data = request.get_data()  
      with open("uploaded.jpg", "wb") as fh:
        fh.write(data)
      return 'file uploaded successfully',200

@app.route('/get_data', methods=['GET','POST'])
def get_data():
    if request.method == 'POST':
      data = request.get_data()  
      with open("uploaded.mp4", "wb") as fh:
        fh.write(data)
      return 'file uploaded successfully',200      
    if request.method == 'GET':  
      return {"message":"данные отправлены"},200
    
@app.route('/get_goods', methods=['GET'])
def get_goods():
    if request.method == 'GET':  

      values=[]
      for i in range(1,5):
        record =[]
        record.append("AA"+str(i))
        record.append("22"+str(i))
        record.append("Товар через запрос 2"+str(i))
        values.append(record)
      
      return json.dumps(values,ensure_ascii=False),200    


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=3000,debug=False)