import json
from datetime import datetime
import base64
from ru.travelfood.simple_ui import SimpleUtilites as suClass


def init(hashMap,_files=None,_data=None):

    hashMap.put("SQLConnectDatabase","test55.DB")
    hashMap.put("SQLExec",json.dumps({"query":"create table IF NOT EXISTS goods (id integer primary key autoincrement,art text, barcode text, nom text)","params":""}))
   
    username=""
    password=""
    userpass = username + ':' + password
    encoded_u = base64.b64encode(userpass.encode()).decode()
 
    hashMap.put("HTTPAddAlias",json.dumps({"alias":"long1c","url":"http://192.168.1.41:3000","headers":{"Content-Type":"application/json; charset=utf-8","Accept":"*/*"},"basic":{"user":username,"password":password}},ensure_ascii=False))     
    
    return hashMap


def run_request_task_native(hashMap,_files=None,_data=None):
    hashMap.put("BreakHandlersIfError","")
    
    workercode=[{"action":"run","type":"http","method":"GET #long1c/get_goods"},
                {"action":"run","type":"set","method":"SQLParameter=@ResultMessage"},
                {"action":"run","type":"sql","method":"insert into goods(art,barcode,nom) values(?,?,?)"},
                {"action":"run","type":"set","method":"speak=Данные загружены"}]
    
   
    hashMap.put("StartWork",json.dumps({"work":workercode,"tag":"my_single_task","retry":True,"conditions":"BATTERY_NOT_LOW;CHARGING;CONNECTED"},ensure_ascii=False))
    
    return hashMap    



def run_periodic_worker(hashMap,_files=None,_data=None):
   

    if hashMap.get("listener") == "btn_run_periodic":
        workercode=[{"action":"run","type":"set","method":"beep"}]
    
               
        hashMap.put("StartPeriodicWork",json.dumps({"work":workercode,"period":15,"tag":"periodic1","conditions":"CONNECTED"},ensure_ascii=False))

    if hashMap.get("listener") == "btn_stop_periodic":
         hashMap.put("StopWork","periodic1")
    
    return hashMap  


def upload_open(hashMap,_files=None,_data=None):
   
    hashMap.put("mm_local","")
    
    return hashMap 

def upload_input(hashMap,_files=None,_data=None):
   

    if hashMap.get('listener')=='photo':
        filename =hashMap.get("photo_path") 
        postExecute=[{"action":"run","type":"python","method":"request_upload_callback"}]
        #описание события по ошибке
        #описание запроса
        username=""
        password=""
        userpass = username + ':' + password
        encoded_u = base64.b64encode(userpass.encode()).decode()
        r = {"url":"http://192.168.1.41:3000/upload", "auth":"Basic %s" % encoded_u,"method":"POST", "headers":{"Accept":"*/*"},"file":filename,"postExecute":postExecute}
        hashMap.put("StartUploadWorkRequest",json.dumps({"request":r,"tag":"my_task_upload"},ensure_ascii=False))
    if hashMap.get('listener')=='btn_stop':    
        hashMap.put("StopWork","my_task_upload")
    
    return hashMap  

def request_upload_callback(hashMap,_files=None,_data=None):
   
    if len(hashMap.get("ResultError"))>0:
      hashMap.put("speak","Ошибка "+hashMap.get("ResultError"))    
    else:  
      hashMap.put("speak","Файл отправлен на сервер")
    
    return hashMap  

def download_input(hashMap,_files=None,_data=None):
   

    if hashMap.get('listener')=='btn_run':
        filename =suClass.get_temp_file("mp4") 
        postExecute=[{"action":"run","type":"python","method":"request_download_callback"}]
        #описание события по ошибке
        #описание запроса
        #username=""
        #password=""
        #userpass = username + ':' + password
        #encoded_u = base64.b64encode(userpass.encode()).decode()
        
        #Можно вот такой вариант:
        #r = {"url":"http://192.168.1.41:3000/download","method":"GET", "headers":{"Accept":"*/*"},"basic":{"user":"usr","password":""},"file":filename,"postExecute":postExecute}
        #...или через alias:
        r = {"url":"#long1c/download","method":"GET","file":filename,"postExecute":postExecute}
        
        hashMap.put("StartDownloadWorkRequest",json.dumps({"request":r,"tag":"my_task_download","title":"Загрузка","body":"видео.mp4"},ensure_ascii=False))
    
    return hashMap  

def request_download_callback(hashMap,_files=None,_data=None):
   
    if len(hashMap.get("ResultError"))>0:
      hashMap.put("speak","Ошибка "+hashMap.get("ResultError"))    
    else:  
      hashMap.put("speak","Файл загружен")
    
    return hashMap  
