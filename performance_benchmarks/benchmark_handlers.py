import json
import requests
from requests.auth import HTTPBasicAuth
import sqlite3
from sqlite3.dbapi2 import Error
import time
import datetime

from pony import orm
from pony.orm import Database,Required,Set,Json,PrimaryKey,Optional
from pony.orm.core import db_session

from ru.travelfood.simple_ui import NoSQL as noClass
from java import jclass
from android.widget import Toast
from com.chaquo.python import Python

db = Database()
db.bind(provider='sqlite', filename='//data/data/ru.travelfood.simple_ui/databases/SimpleWMS', create_db=True)

results_barcode={
    "type": "table",
    "textsize": "25",
    "hidecaption": "false",
    "hideinterline": "false",
    "columns": [
    {
        "name": "action",
        "header": "Действие",
        "weight": "3"
    },
    {
        "name": "time",
        "header": "Время,с",
        "weight": "1"
    }
    ],
    "rows": []
    }

        
class TST_Goods(db.Entity):
        name =  Required(str)
        product_number =  Optional(str)
        barcode =  Optional(str)
        created_at = Optional(datetime.datetime, sql_default='CURRENT_TIMESTAMP')


time_request=None

def init(hashMap,_files=None,_data=None):
    db.generate_mapping(create_tables=True) 

    return hashMap

def sync_on_start(hashMap,_files=None,_data=None):

    j = {"hint":"OData URL","default_text":"http://192.168.1.40:2312/ui2/odata/standard.odata/Catalog_Номенклатура?$format=json"}
    hashMap.put("url_fill",json.dumps(j))

    j = {"hint":"1C user","default_text":"usr"}
    hashMap.put("user_fill",json.dumps(j))

    j = {"hint":"1C password","default_text":"","password":True}
    hashMap.put("password_fill",json.dumps(j))

    

    return hashMap

def sync_input(hashMap,_files=None,_data=None):
   
    #hashMap.put("toast",str(hashMap.get("listener")))
    
    if hashMap.get("listener")=="btn_download":

        username=hashMap.get("user")
        password=hashMap.get("password")
        url = hashMap.get("url")

        jt ={
        "type": "table",
        "textsize": "25",
        "hidecaption": "false",
        "hideinterline": "false",
        "columns": [
        {
            "name": "action",
            "header": "Действие",
            "weight": "3"
        },
        {
            "name": "time",
            "header": "Время,с",
            "weight": "1"
        }
        ],
        "rows": []
        }

        skip=0
        step=50000
        for k in range(20):


            start_time = time.time()
            first=False
            if skip>0:
                locurl = url+'&$skip='+str(skip)+'&$top='+str(step)
                
            else:    
                first=True
                locurl = url+'&$top='+str(step)

            r = requests.get(locurl, auth=HTTPBasicAuth(username, password,),
                    headers={'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'})

            time_request =time.time() - start_time

            jt['rows'].append({"action":'Запрос к OData '+locurl,"time":"{:.3f}".format(time_request)})


            skip+=step

            if r.status_code==200:
                r.encoding='utf-8'
                jdata = json.loads(r.text.encode("utf-8"))
                
                if  len(jdata['value'])==0:
                    break   

                values  =[]

                #if first:
                    #ncl = noClass("test_new_nosql")
                    #start_time = time.time()
                    #ncl.put("response",jdata['value'],True)
                    #time_insert = time.time() - start_time
                    #jt['rows'].append({"action":'Запись в NoSQL',"time":"{:.5f}".format(time_insert)})

                    #Toast.makeText(Python.getPlatform().getApplication(), "Загрузили с OData ",  Toast.LENGTH_SHORT).show()

                    #start_time = time.time()
                    #res1 = ncl.get("response"+str(skip))
                    #jt['rows'].append({"action":'Получение из NoSQL',"time":"{:.5f}".format(time_insert)})

                    #Toast.makeText(Python.getPlatform().getApplication(), str(jdata['value']),  Toast.LENGTH_SHORT).show()
                
                for g in jdata['value']:
                    values.append((g["Description"],str(g["Артикул"]).replace(' ',''),str(g["Артикул"]).replace(' ','')))

                

                #hashMap.put("toast",str(len(values))) 


                conn = sqlite3.connect('//data/data/ru.travelfood.simple_ui/databases/SimpleWMS')

                start_time = time.time()
                #conn.executemany("insert into test_goods(title, art,barcode) values (?,?,?)", values)

                try:
                        сursor1 = conn.cursor()
                        сursor1.executemany("insert into TST_Goods(name, product_number,barcode) values (?,?,?)", values)
                        conn.commit()
                except sqlite3.Error as err:
                        raise ValueError(err) 

                

        
                conn.close()

                time_insert = time.time() - start_time
                jt['rows'].append({"action":'Запись в TST_Goods',"time":"{:.3f}".format(time_insert)})

                Toast.makeText(Python.getPlatform().getApplication(), "Загрузили "+str(skip), Toast.LENGTH_SHORT).show()
                
            

                #hashMap.put("toast","Количество записей:"+str(len(values))+"Время запроса :"+str(round(time_request,1))+". Время записи:"+str(round(time_insert,1)))   
            else:
                hashMap.put("toast",str(r.status_code))        

        hashMap.put("table",json.dumps(jt))
    
        # conn = sqlite3.connect('//data/data/ru.travelfood.simple_ui/databases/SimpleWMS')
        # cursor = conn.cursor()
        # cursor.execute('SELECT COUNT(*) FROM TST_Goods')
        # rowcount = cursor.fetchone()[0]
        # conn.close()
        # hashMap.put("toast","Всего записей в TST_Goods="+str(rowcount))

    return hashMap 


def barcode_input(hashMap,_files=None,_data=None):
    global results_barcode
   
    if hashMap.get("listener")=="barcode":
        start_time=time.time()
        nom = TST_Goods.get(barcode=hashMap.get("barcode"))
        time_request =time.time() - start_time
        if nom==None:
            hashMap.put("toast","Не найдено")
        else:
            hashMap.put("nom",str(nom.name))
            results_barcode['rows'].append({"action":'Поиск ORM:'+str(hashMap.get("barcode")),"time":"{:.3f}".format(time_request)})    
    
    hashMap.put("table",json.dumps(results_barcode))       

    return hashMap 
    
def test_input(hashMap,_files=None,_data=None):
   
    from ru.travelfood.simple_ui import FileOperations as foClass
    from java import jclass

    foClass = jclass("ru.travelfood.simple_ui.FileOperations")
    fcl = foClass()
    res = fcl.export_file('/data/data/ru.travelfood.simple_ui/app_files/SimpleUI images/01366153_691c_439b_8be9_f75538b23cf5.jpg','test_j_1.jpg')
    res = fcl.import_file('РелизИюнь2021.PNG','/data/data/ru.travelfood.simple_ui/app_files/SimpleUI images/РелизИюнь2021.PNG')
    if res:
        hashMap.put("toast","Все хорошо")
    
           

    return hashMap 

    

def cv_run(hashMap,_files=None,_data=None):
    global counter_barcode
    global start_time
    global results_barcode

    counter_barcode=0
    start_time=time.time()
    #global results_cv
    hashMap.put("toast",hashMap.get("listener"))


    if hashMap.get('listener')=='btn_run':
        hashMap.put("RunCV","Штрихкоды ActiveCV")

    if hashMap.get('listener')=='btn_run_ocr':
        hashMap.put("RunCV","OCR ActiveCV")    

    if hashMap.get('listener')=='ActiveCV':
        hashMap.put("table",json.dumps(results_barcode))
        hashMap.put("beep","")

    return hashMap 

def cv_barcodes_on_new_object(hashMap,_files=None,_data=None):
    global counter_barcode
    global results_barcode
    global start_time

    obj = str(hashMap.get("current_object"))
    nom = TST_Goods.get(barcode=obj)
    
    time_request =time.time() - start_time
    
    
    
    if nom==None:
        hashMap.put("toast","Не найден товар "+obj)
    else:    
        if hashMap.containsKey("green_list"):
                greenlist = str(hashMap.get("green_list")).split(";")
                greenlist.append(obj)
                hashMap.put("green_list",";".join(greenlist))
        else:
            greenlist=[obj]
            hashMap.put("green_list",";".join(greenlist))    

        counter_barcode+=1
        hashMap.put("info","Найдено: "+str(counter_barcode))

        time_request =time.time() - start_time
        results_barcode['rows'].append({"action":'ActiveCV найдено:'+obj,"time":"{:.3f}".format(time_request)})  
    
        
    if counter_barcode>=5:
        hashMap.put("FinishProcess","")

    return hashMap    

def cv_ocr_on_new_object(hashMap,_files=None,_data=None):
    global counter_barcode
    global results_barcode
    global start_time

    obj = str(hashMap.get("current_object"))

    hashMap.put("toast","Объект: "+obj)

    nom = TST_Goods[int(obj)]
    
    time_request =time.time() - start_time
    
    
    if nom==None:
         hashMap.put("toast","Не найден товар "+obj)
    else:    
        if hashMap.containsKey("green_list"):
                greenlist = str(hashMap.get("green_list")).split(";")
                greenlist.append(obj)
                hashMap.put("green_list",";".join(greenlist))
        else:
            greenlist=[obj]
            hashMap.put("green_list",";".join(greenlist))    
        counter_barcode+=1
        hashMap.put("info","Найдено: "+str(counter_barcode))

        time_request =time.time() - start_time
        results_barcode['rows'].append({"action":'ActiveCV найдено:'+obj,"time":"{:.3f}".format(time_request)})  
    
        
    if counter_barcode>=5:
        hashMap.put("FinishProcess","")

    return hashMap    

#@db_session
def add_record(description, art, barcode):
    TST_Goods(name=description,product_number=art,barcode=barcode)

def sync_input_ORM(hashMap,_files=None,_data=None):
   
    #hashMap.put("toast",str(hashMap.get("listener")))
    
    if hashMap.get("listener")=="btn_download":

        username=hashMap.get("user")
        password=hashMap.get("password")
        url = hashMap.get("url")

        jt ={
        "type": "table",
        "textsize": "25",
        "hidecaption": "false",
        "hideinterline": "false",
        "columns": [
        {
            "name": "action",
            "header": "Действие",
            "weight": "3"
        },
        {
            "name": "time",
            "header": "Время,с",
            "weight": "1"
        }
        ],
        "rows": []
        }

        skip=0
        step=50000
        for k in range(2):


            start_time = time.time()
            first=False
            if skip>0:
                locurl = url+'&$skip='+str(skip)+'&$top='+str(step)
                
            else:    
                first=True
                locurl = url+'&$top='+str(step)

            r = requests.get(locurl, auth=HTTPBasicAuth(username, password,),
                    headers={'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'})

            time_request =time.time() - start_time

            jt['rows'].append({"action":'Запрос к OData '+locurl,"time":"{:.3f}".format(time_request)})


            skip+=step

            if r.status_code==200:
                r.encoding='utf-8'
                jdata = json.loads(r.text.encode("utf-8"))
                
                if  len(jdata['value'])==0:
                    break   

                start_time = time.time()

                with db_session:
                    for g in jdata['value']:
                        add_record(g["Description"],str(g["Артикул"]).replace(' ',''),str(g["Артикул"]).replace(' ',''))
                    

                
                time_insert = time.time() - start_time
                jt['rows'].append({"action":'Запись в TST_Goods ORM',"time":"{:.3f}".format(time_insert)})

                Toast.makeText(Python.getPlatform().getApplication(), "Загрузили "+str(skip), Toast.LENGTH_SHORT).show()
                
            

                #hashMap.put("toast","Количество записей:"+str(len(values))+"Время запроса :"+str(round(time_request,1))+". Время записи:"+str(round(time_insert,1)))   
            else:
                hashMap.put("toast",str(r.status_code))        

        hashMap.put("table",json.dumps(jt))
    
        conn = sqlite3.connect('//data/data/ru.travelfood.simple_ui/databases/SimpleWMS')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM TST_Goods')
        rowcount = cursor.fetchone()[0]
        conn.close()
        #hashMap.put("toast","Всего записей в TST_Goods="+str(rowcount))

    return hashMap 


