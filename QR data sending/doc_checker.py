
import json

def new_part_cv(hashMap,_files=None,_data=None):   

  qr = hashMap.get("current_object")  
  mqr = qr.split("~")
  
  if len(mqr)>=2:
    if hashMap.containsKey("green_list"):
        greenlist =   hashMap.get("green_list").split(";")
    else:
        greenlist=[]  

    greenlist.append(qr)    
    hashMap.put("green_list",";".join(greenlist))

    
    if len(greenlist)==int(mqr[1]): #now we have complete value from all parts
        

        total = []
        for el in greenlist:
            mqrl = el.split("~")
            total.append({"number":int(mqrl[0]),"value":mqrl[2]})
        sorted_total = sorted(total, key=lambda d: d['number'])
        result=""
        for el in sorted_total:
            result+=el['value']
        
        hashMap.put("result",result)
        hashMap.put("FinishProcess","")
        

  return hashMap

def start_cv_download(hashMap,_files=None,_data=None):   
  
  if hashMap.containsKey("green_list"):
        hashMap.remove("green_list")
  
  if hashMap.containsKey("result"):
        hashMap.remove("result")      

  hashMap.put("RunCV","Скачать накладную")  

  return hashMap

def run_scan_goods(hashMap,_files=None,_data=None):   
  
  hashMap.put("RunCV","Сканировать накладную")  

  return hashMap  

checked = []


def main_input(hashMap,_files=None,_data=None):   
  global checked
  
  if hashMap.get("listener")=="ActiveCV":  
    
    if hashMap.containsKey("result"):
        hashMap.put("beep","42")  
  if hashMap.get("listener")=="barcode": 
    checked.append(hashMap.get("barcode")) 
        

  return hashMap 

def scan_cv_new_object(hashMap,_files=None,_data=None):   
  global checked

  if hashMap.containsKey("green_list"):
        greenlist =   hashMap.get("green_list").split(";")
  else:
        greenlist=[]

  greenlist.append(hashMap.get("current_object"))    
  hashMap.put("green_list",";".join(greenlist))      
    
  checked.append(hashMap.get("current_object"))
  hashMap.put("info","Найдено :"+str(len(checked)))
        

  return hashMap    



def main_open(hashMap,_files=None,_data=None):   
  global checked
  
  if not hashMap.containsKey("result"):
    checked.clear()
  else:  
        
    j = {
    "type": "table",
    "textsize": "20",
    "hidecaption": "false",
    "hideinterline": "false",
    "columns": [
    {
        "name": "nom",
        "header": "Товар",
        "weight": "3"
    },
    
    {
        "name": "unit",
        "header": "Ед.",
        "weight": "1"
    },
    {
        "name": "qty",
        "header": "Кол-во",
        "weight": "1"
    }
    ],
    "rows":[],
    "colorcells":[]


    }

   
    jresult = json.loads(hashMap.get("result"))
    for i in jresult:
     
      j['rows'].append(i)

    for c in checked:
        r=0
        for i in j['rows']:
            r+=1
            if i['barcode']==c:
                j["colorcells"].append({"row":str(r),"column":"0","color": "#33CC99"})
                j["colorcells"].append({"row":str(r),"column":"1","color": "#33CC99"})
                j["colorcells"].append({"row":str(r),"column":"2","color": "#33CC99"})


    hashMap.put("table",json.dumps(j,ensure_ascii=False).encode('utf8').decode())

  return hashMap    