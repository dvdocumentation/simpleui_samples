import json
from ru.travelfood.simple_ui import SimpleSQLProvider as sqlClass

def init(hashMap,_files=None,_data=None):
    hashMap.put("SQLConnectDatabase","test55.DB")
    #А вот так должно быть соединение с основной базой (которая была всегда)
    #hashMap.put("SQLConnectDatabase","") 
    hashMap.put("SQLExec",json.dumps({"query":"create table IF NOT EXISTS goods (id integer primary key autoincrement,art text, barcode text, nom text)","params":""}))
    
    return hashMap

def scr1_input(hashMap,_files=None,_data=None):
    import time
    time.sleep(2)
    
    
    return hashMap

def scr1_on_start(hashMap,_files=None,_data=None):
    
    hashMap.put("val1","... значение установлено в обработчике")
    
    
    return hashMap

def scr1_beep(hashMap,_files=None,_data=None):
    
    hashMap.put("beep","55")
    
    
    return hashMap    

def post_online(hashMap,_files=None,_data=None):
    import time
    time.sleep(2)
    hashMap.put("vibrate","")
    hashMap.put("beep","")
    hashMap.put("speak","спали 2 секунды")
    hashMap.put("speak","А сейчас - завершился асинхронный.")
    
    return hashMap    

def scr1_input_prepare(hashMap,_files=None,_data=None):
    hashMap.put("after","Сразу после")
    hashMap.put("toast","Сейчас выполнился синхронный обработчик, параллельно началось выполнение асинхронного. Экран не блокируется можно работать с приложением")
    
    return hashMap        

def cv_after(hashMap,_files=None,_data=None):
    
    hashMap.put("toast",hashMap.get("current_object"))
    
    return hashMap  


def other_open(hashMap,_files=None,_data=None):
        
    hashMap.put("mm_local","") 
    return hashMap    

def other_input(hashMap,_files=None,_data=None):
   
    
    hashMap.put("toast",hashMap.get("listener"))

    if hashMap.get("listener")=="btns":
        if hashMap.get("btns")=="Сохранение настроек":
            hashMap.put("SetSettingsJSON",json.dumps({"torch":True}))
        if hashMap.get("btns")=="Открыть камеру":
            hashMap.put("noRefresh","") 
            hashMap.put("StartCaptureCamera","photo_from_camera")    
        if hashMap.get("btns")=="Открыть галерею":
            hashMap.put("noRefresh","") 
            hashMap.put("StartMediaGallery","photo_from_camera")    
    elif hashMap.get("listener")=="photo":
        hashMap.put("toast",hashMap.get("photo_from_camera"))
    return hashMap 

def manual_after(hashMap,_files=None,_data=None):
        
    hashMap.put("toast","Все") 
    return hashMap  

def manual_input(hashMap,_files=None,_data=None):
    if hashMap.get("listener")=="btn_run":    
        hashMap.put("RunEvent",json.dumps([{"action": "run","type": "python","method": "post_online", "postExecute": "" }])) 
    elif hashMap.get("listener")=="btn_run_async":   
        hashMap.put("RunEvent",json.dumps([{"action": "runasync","type": "python","method": "post_online", "postExecute": json.dumps([{"action": "run","type": "python","method": "manual_after"}])  }])) 

    return hashMap  


def sql_input(hashMap,_files=None,_data=None):
   

    if hashMap.get("listener")=="run_execsql_many":  
        sql = sqlClass()
        values=[]
        for i in range(1,10000):
            record =[]
            record.append("A"+str(i))
            record.append(str(i))
            record.append("Товар"+str(i))
            values.append(record)


        sql.SQLExecMany("insert into goods(art,barcode,nom) values(?,?,?)",json.dumps(values,ensure_ascii=False))
       
        hashMap.put("beep","") 
   
    return hashMap  

def sql_check(hashMap,_files=None,_data=None):
   

    if len(hashMap.get("name"))==0 or hashMap.get("name")==None:  
               
        hashMap.put("beep","") 
        hashMap.put("BreakHandlers","") 
        hashMap.put("toast","Не заполнено наименование") 

    if len(hashMap.get("barcode"))==0 or len(hashMap.get("barcode"))==None:  
               
        hashMap.put("beep","") 
        hashMap.put("BreakHandlers","") 
        hashMap.put("toast","Не заполнен штрихкод")     

        
   
    return hashMap 

def sql_insert_var(hashMap,_files=None,_data=None):

    values=[]
    for i in range(1,3):
        record =[]
        record.append("AA"+str(i))
        record.append("22"+str(i))
        record.append("Товар вручную "+str(i))
        values.append(record)
   
    hashMap.put("SQLParameter",json.dumps(values,ensure_ascii=False))     

    return hashMap     


def save_http_settings(hashMap,_files=None,_data=None):
      
    hashMap.put("HTTPAddAlias",json.dumps({"alias":"odata","url":hashMap.get("url"),"headers":{"Content-Type":"application/json; charset=utf-8","Accept":"*/*"},"basic":{"user":hashMap.get("user"),"password":hashMap.get("password")}},ensure_ascii=False))     

    return hashMap     

def calculate_async(hashMap,_files=None,_data=None):

    import time
    time.sleep(3) 
    
    hashMap.put("res",str(int(hashMap.get("a"))+int(hashMap.get("b"))))
    hashMap.put("vibrate","")
    hashMap.put("RefreshScreen","")
    
    return hashMap    

def play_beep(hashMap,_files=None,_data=None):
   
    
    hashMap.put("beep","")
    
    
    return hashMap    

def test(hashMap,_files=None,_data=None):
   
    
    hashMap.put("beep","10")
   
    
    
    return hashMap 

def datachange(hashMap,_files=None,_data=None):
   
    
    
    hashMap.put("toast",hashMap.get("listener"))
    
    
    return hashMap     

def open_file(hashMap,_files=None,_data=None):
   
    
    
    hashMap.put("speak",hashMap.get("content")+"/"+hashMap.get("extra_text"))

    #Обязательно нужно отключать стандартную обработку OffStandardListener и обработчики должны быть в синхронном режиме

    hashMap.put("OffStandardListener","true")
    hashMap.put("reply_notification",json.dumps([{"number":5,"title":"Опрос","message":hashMap.get("content")}],ensure_ascii=False))
    

    
    
    return hashMap                

def input_select_command(hashMap,_files=None,_data=None):
    
    hashMap.put("SQLQuery",json.dumps({"query":"select * from goods where id=?","params":"2"}))
    
    return hashMap

def input_execmany_command(hashMap,_files=None,_data=None):
    
    values=[]
    for i in range(1,3):
        record =[]
        record.append("AA"+str(i))
        record.append("22"+str(i))
        record.append("Товар через переменную "+str(i))
        values.append(record)
   
   
    hashMap.put("SQLExecMany",json.dumps({"query":"insert into goods(art,barcode,nom) values(?,?,?)","params":json.dumps(values,ensure_ascii=False)}))
    
    return hashMap    

def input_class_input(hashMap,_files=None,_data=None):
    
    sql = sqlClass()

    success=sql.SQLExec("insert into goods(art,barcode,nom) values(?,?,?)","111222,22000332323,Некий товар")
    res = sql.SQLQuery("select * from goods where id=1","")
    if success:    
        hashMap.put("toast",res) 
    else:
        hashMap.put("toast","Ашипка")             
    
    return hashMap

def periodic1(hashMap,_files=None,_data=None):
    import random
    
    #эта функция , также как и periodic2 - для проверки параллельной работы с СУБД из разных подключений

    #содержимое закоментировано, чтобы не мешало проверять другие. Для проверки этого обработчика можно раскомментировать


    # sql = sqlClass()

    # success=sql.SQLExec("update goods set nom=? where id=1","Periodic -"+str(random.randint(10, 10000)))
    # res = sql.SQLQuery("select * from goods where id=1","")
    # if success:    
        
    #     hashMap.put("beep","15") 
            
    
    return hashMap
    