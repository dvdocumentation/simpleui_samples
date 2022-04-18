import ui_global
from pony.orm.core import db_session
from pony import orm
from pony.orm import Database,Required,Set,select,commit
import json

def sample1_on_create(hashMap,_files=None,_data=None):
    if not hashMap.containsKey("a"):
        hashMap.put("a","")    
    if not hashMap.containsKey("b"):
        hashMap.put("b","")        
    return hashMap

def sample1_on_input(hashMap,_files=None,_data=None):
    if hashMap.get("listener")=="btn_res":
        hashMap.put("toast",str(int(hashMap.get("a"))-int(hashMap.get("b"))))    
    
    return hashMap    

def init_on_start(hashMap,_files=None,_data=None):
    ui_global.init()
    return hashMap

def input_qty(hashMap,_files=None,_data=None):
    with db_session:
        p = ui_global.Record(barcode=hashMap.get('barcode'),name=hashMap.get('nom'), qty=int(hashMap.get('qty')))
        commit()

    hashMap.put("ShowScreen","Сканирование штрихкода")
    hashMap.put("toast","Добавлено")
    return hashMap

def on_start_barcode(hashMap,_files=None,_data=None):

    table  = {
    "type": "table",
    "textsize": "20",

    "columns": [
    {
        "name": "barcode",
        "header": "Barcode",
        "weight": "2"
    },
    {
        "name": "name",
        "header": "Name",
        "weight": "2"
    },
      {
        "name": "qty",
        "header": "Qty.",
        "weight": "1"
    }
    ]
    }
    #work with SQL via Pony ORM
    query = select(c for c in ui_global.Record)
    rows=[]
    for record in query:
        rows.append({"barcode":record.barcode,"name":record.name,"qty":record.qty})

    table['rows'] =rows   
    hashMap.put("table",json.dumps(table))

    return hashMap

def on_start_active_cv(hashMap,_files=None,_data=None):

    import sqlite3 # This is another way to work with SQL
    from sqlite3.dbapi2 import Error
    import json

    
    #create connection with database
    conn= None
    try:
        conn = sqlite3.connect('//data/data/ru.travelfood.simple_ui/databases/SimpleWMS')
    except Error as e:
        raise ValueError('Нет соединения с базой!')
  
    cursor = conn.cursor()
    cursor.execute("SELECT barcode,name,qty FROM Record")

    results = cursor.fetchall()

    green_list = []
    red_list= []
    info_list = []
    for link in results:
        job = {"object":str(link[0]),"info":str(link[1])+" </n> Остаток: <big>"+str(link[2])+"</big>"}
        info_list.append(job)
        green_list.append(link[0])    
            
    conn.close()     

    hashMap.put("object_info_list",json.dumps(info_list,ensure_ascii=False))
    hashMap.put("green_list",';'.join(green_list))
    
    return hashMap

#under construction
def sample1_setscreenshot(hashMap,_files=None,_data=None):
    if hashMap.get("listener")=="btn_set":
        hashMap.put("setScreenshotURL","http://192.168.1.143:2075/post_screenshot")    
    elif hashMap.get("listener")=="btn_send":   
        hashMap.put("sendScreenshots","3")    
    
    return hashMap  