import json
from ru.travelfood.simple_ui import SimpleSQLProvider as sqlClass

def sample1_on_create(hashMap,_files=None,_data=None):
    if not hashMap.containsKey("a"):
        hashMap.put("a","")    
    if not hashMap.containsKey("b"):
        hashMap.put("b","")        
    return hashMap

def sample1_on_input(hashMap,_files=None,_data=None):
    if hashMap.get("listener")=="btn_res":
        hashMap.put("toast",str(int(hashMap.get("a"))+int(hashMap.get("b"))))    
    
    return hashMap    

def init_on_start(hashMap,_files=None,_data=None):
    
    hashMap.put("SQLConnectDatabase","test1.DB")
    hashMap.put("SQLExec",json.dumps({"query":"create table IF NOT EXISTS Record(id integer primary key autoincrement,art text, barcode text, name text, qty real)","params":""}))

    return hashMap

def input_qty(hashMap,_files=None,_data=None):

    sql = sqlClass()
    success=sql.SQLExec("insert into Record(barcode,name,qty) values(?,?,?)",hashMap.get('barcode')+","+hashMap.get("nom")+","+str(hashMap.get("qty")))
        
    if success:    
            hashMap.put("ShowScreen","Сканирование штрихкода")
            hashMap.put("toast","Добавлено")

    
    return hashMap

def on_start_barcode(hashMap,_files=None,_data=None):

    rows=[]    

    table  = {
    "type": "table",
    "textsize": "20",

    "columns": [
    {
        "name": "barcode",
        "header": "[Barcode]",
        "weight": "2"
    },
    {
        "name": "name",
        "header": "Name",
        "weight": "2"
    },
      {
        "name": "qty",
        "header": "[Qty]",
        "weight": "1"
    }
    ]
    }
    
    sql = sqlClass()
    res = sql.SQLQuery("select * from Record","")

    records = json.loads(res)
    for record in records:
        rows.append({"barcode":record['barcode'],"name":record['name'],"qty":str(record['qty'])})

    table['rows'] =rows   
    hashMap.put("table",json.dumps(table))

    return hashMap

def on_start_active_cv(hashMap,_files=None,_data=None):
    
    
    sql = sqlClass()
    res = sql.SQLQuery("select barcode,name,sum(qty) as qty from Record group by barcode,name","")

    results = json.loads(res)
   

    green_list = []
    red_list= []
    info_list = []
    for link in results:
        job = {"object":str(link['barcode']),"info":str(link['name'])+" </n> Остаток: <big>"+str(link['qty'])+"</big>"}
        info_list.append(job)
        green_list.append(link['barcode'])    
            
    

    hashMap.put("object_info_list",json.dumps(info_list,ensure_ascii=False))
    hashMap.put("green_list",';'.join(green_list))
    
    return hashMap

def settings_on_create(hashMap,_files=None,_data=None):
    if not hashMap.containsKey("_UserLocale"):
        hashMap.put("get_user_locale","_UserLocale") #get from NoSQL
    else:
        hashMap.put("lang",hashMap.get("_UserLocale")) #set defaul list value
    
    return hashMap 

def settings_on_input(hashMap,_files=None,_data=None):
    if hashMap.get("listener")=="lang":
        hashMap.put("put_user_locale",hashMap.get("lang"))
        hashMap.put("_UserLocale",hashMap.get("lang")) 

        if hashMap.get("lang")=="Русский":
            hashMap.put("setLocale","ru")   
        elif hashMap.get("lang")=="Английский":
            hashMap.put("setLocale","en")      
    
    return hashMap    

