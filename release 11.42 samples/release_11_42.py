import json
from ru.travelfood.simple_ui import SimpleUtilites as suClass
import random


def init(hashMap,_files=None,_data=None):

    hashMap.put("SQLConnectDatabase","test55.DB")
     
    return hashMap

def longroutine(hashMap,_files=None,_data=None):
    import time
    time.sleep(3)
    
    hashMap.put("beep","")
    hashMap.put("ShowScreen","Экран2")
    return hashMap 

def testprogress(hashMap,_files=None,_data=None):
    hashMap.put("RunPyThreadProgressDef","longroutine")
        
    return hashMap    

def longroutine2(hashMap,_files=None,_data=None):
    import time
    time.sleep(3)

    hashMap.put("label1","Установлено асинхронно")
    
    hashMap.put("RefreshScreen","")
    
    return hashMap

def longroutine_progress_notification(hashMap,_files=None,_data=None):
    import time

    suClass.UpdateProgressNotification(json.dumps({"id":111,"progress":0,"title":"Title","body":"Main text"}))

  
    time.sleep(3)
    suClass.UpdateProgressNotification(json.dumps({"id":111,"progress":25,"title":"Title","body":"Main text"}))
    time.sleep(2)
    suClass.UpdateProgressNotification(json.dumps({"id":111,"progress":50,"title":"Title","body":"Main text"}))
    time.sleep(2)
    suClass.UpdateProgressNotification(json.dumps({"id":111,"progress":75,"title":"Title","body":"Main text"}))
    time.sleep(2)
    suClass.UpdateProgressNotification(json.dumps({"id":111,"progress":100,"title":"Title","body":"Main text"}))

   
    
    return hashMap

def openobjectslist_on_open(hashMap,_files=None,_data=None):
    
    j = { "customcards":         {
            "options":{
              "search_enabled":True,
              "save_position":True
            

            },
            "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
            {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                
                {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string3",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                }
                ]
                },
                {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@val",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "16",
                "TextColor": "#DB7093",
                "TextBold": True,
                "TextItalic": False,
                "BackgroundColor": "",
                "width": "match_parent",
                "height": "wrap_content",
                "weight": 2
                }
                ]
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@descr",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "-1",
                "TextColor": "#6F9393",
                "TextBold": False,
                "TextItalic": True,
                "BackgroundColor": "",
                "width": "wrap_content",
                "height": "wrap_content",
                "weight": 0
            }
            ]
        }

    }
    }
   
    j["customcards"]["cardsdata"]=[]
    for i in range(0,5):
      if i==0:
        c =  {
       
          "group": "Комплектующие"
       
        }
      
        j["customcards"]["cardsdata"].append(c)

      if i==4:
        c =  {
       
          "group": "Уценка"
       
        }
      
        j["customcards"]["cardsdata"].append(c)   

      price =  str(random.randint(10, 10000))+" руб." 
      c =  {
        "key": "Материнская плата ASUS ROG MAXIMUS Z690 APEX"+", "+str(price),
       
        "descr": "Pos. "+str(i),
        "val": str(price)+" руб.",
        "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
        "string2": "Гнездо процессора LGA 1700",
        "string3": "Частотная спецификация памяти 4800 МГц"
      }
      
      j["customcards"]["cardsdata"].append(c)

    if not hashMap.containsKey("cards"):
      hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    
    return hashMap


def units_on_open(hashMap,_files=None,_data=None):
    
    j = { "customcards":         {
            "options":{
              "search_enabled":True,
              "save_position":True
              

            },
            "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
            {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                
                {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string3",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                }
                ]
                }
                ]
            }
            ]
        }

    }
    }
   
    j["customcards"]["cardsdata"]=[]

    c =  {
        "key": "Шт",
       
        
        "val": "001",
        "string1": "Шт.",
        "string2": "Количество в упаковке=1",
        "string3": "Штуки"
      }
      
    j["customcards"]["cardsdata"].append(c)

    c =  {
        "key": "Кг",
       
        
        "val": "001",
        "string1": "Кг.",
        "string2": "Количество в упаковке=1",
        "string3": "Килограммы"
      }
      
    j["customcards"]["cardsdata"].append(c)

    c =  {
        "key": "Упак",
       
        
        "val": "001",
        "string1": "Упак.",
        "string2": "Количество в упаковке=1",
        "string3": "Упаковки"
      }
      
    j["customcards"]["cardsdata"].append(c)

    

    if not hashMap.containsKey("cards"):
      hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    
    return hashMap

def card_input(hashMap,_files=None,_data=None):
    
   
   hashMap.put(hashMap.get("field"),hashMap.get("selected_card_key"))

   hashMap.put("FinishProcessResult","")

    
   return hashMap



def testargs(hashMap,*args):
 
   
  
  hashMap.put("vibrate","")
  hashMap.put("toast",args[0]+args[1]+args[2])

  return hashMap

def set_list_search(hashMap,_files=None,_data=None):
    
   
   

    j = { "customcards":         {
            "options":{
              "search_enabled":True,
              "save_position":True,
              "override_search":True

            },
            "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
            {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                {
                "type": "CheckBox",
                "Value": "@cb1",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "cb1",
                "BackgroundColor": "#DB7093",
                "width": "match_parent",
                "height": "wrap_content",
                "weight": 2
                },
                {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string3",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "Button",
                    "show_by_condition": "",
                    "Value": "#f290",
                    "TextColor": "#DB7093",
                    "Variable": "btn_tst1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": ""
                    
                },
                {
                    "type": "Button",
                    "show_by_condition": "",
                    "Value": "#f469",
                    "TextColor": "#DB7093",
                    "Variable": "btn_tst2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": ""
                    
                }
                ]
                },
                {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@val",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "16",
                "TextColor": "#DB7093",
                "TextBold": True,
                "TextItalic": False,
                "BackgroundColor": "",
                "width": "match_parent",
                "height": "wrap_content",
                "weight": 2
                },
               {
                "type": "PopupMenuButton",
                "show_by_condition": "",
                "Value": "Удалить;Проверить",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "menu_delete"
                
                }
                ]
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@descr",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "-1",
                "TextColor": "#6F9393",
                "TextBold": False,
                "TextItalic": True,
                "BackgroundColor": "",
                "width": "wrap_content",
                "height": "wrap_content",
                "weight": 0
            }
            ]
        }

    }
    }
   
    j["customcards"]["cardsdata"]=[]
    for i in range(0,5):
      if i==0:
        c =  {
       
          "group": "Комплектующие"
       
        }
      
        j["customcards"]["cardsdata"].append(c)

      if i==4:
        c =  {
       
          "group": "Уценка"
       
        }
      
        j["customcards"]["cardsdata"].append(c)   

    price =  str(random.randint(10, 10000))+" руб." 
    c =  {
        "key": "Материнская плата ASUS ROG MAXIMUS Z690 APEX"+", "+str(price),
       
        "descr": "Pos. "+str(i),
        "val": str(price)+" руб.",
        "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
        "string2": "Гнездо процессора LGA 1700",
        "string3": "Частотная спецификация памяти 4800 МГц"
      }
      
    j["customcards"]["cardsdata"].append(c)

    
    hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    hashMap.put("toast",hashMap.get("cards"))

    
    return hashMap

def map_on_start(hashMap,_files=None,_data=None):
   import os
    
   filename = suClass.get_temp_dir()+os.sep+"test_map.sug"
   
   hashMap.put("mapname",filename)

   

    
   return hashMap

def show_pin(hashMap,_files=None,_data=None):
    
   h=[{"action":"run","type":"python","listener":"pin_success","method":"check_pin"},
               {"action":"run","type":"set","listener":"pin_cancel","method":"vibrate"}
               ]
   hashMap.put("ShowPIN",json.dumps({"header":"Введите ПИН","handlers":h,"block_cancel":False},ensure_ascii=False))

    
   return hashMap

def check_pin(hashMap,_files=None,_data=None):
    
   hashMap.put("toast",hashMap.get("pin"))

   if hashMap.get("pin")=="1111":
      hashMap.put("beep","")
      hashMap.put("ClosePIN","")
   
    
   return hashMap


def show_biometric(hashMap,_files=None,_data=None):
    
   h=[{"action":"run","type":"python","listener":"BiometricAuthenticationSucceeded","method":"biometric_success"},
               {"action":"run","type":"set","listener":"BiometricAuthenticationFailed","method":"app_shutdown"},
               {"action":"run","type":"set","listener":"BiometricAuthenticationError","method":"app_shutdown"}
               ]
   hashMap.put("ShowBiometric",json.dumps({"title":"Проверка входа","body":"Необходима аутенификация","handlers":h},ensure_ascii=False))

    
   return hashMap

def biometric_success(hashMap,_files=None,_data=None):
    
   hashMap.put("toast","willkommen zurück")

   
    
   return hashMap

def biometric_success(hashMap,_files=None,_data=None):
    
   hashMap.put("toast","willkommen zurück")

   
    
   return hashMap

def highlight_lists(hashMap,_files=None,_data=None):
    
   hashMap.put("SetRed","et1;et2;et3")
   hashMap.put("SetGreen","et5;et6;et7")

   
    
   return hashMap

def foo(hashMap,*args):
    param1 =  args[0] 
    param2 =  args[1] 
    param3 =  args[2]  

    return hashMap