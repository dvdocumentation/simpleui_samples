import json
import random
import time
import base64

def NewFields_onCreate(hashMap,_files=None,_data=None):
    #input_type: https://developer.android.com/reference/android/text/InputType
    default_password="123"
    if hashMap.containsKey("password"):
        default_password=hashMap.get("password")

    default_login=""
    if hashMap.containsKey("login"):
        default_login=hashMap.get("login")

    j1 = {"hint":"Логин","default_text":default_login}
    hashMap.put("fill_login",json.dumps(j1))

    j2 = {"hint":"Пароль","default_text":default_password,"counter":True,"counter_max":15,"input_type":145,"password":True}
    hashMap.put("fill_password",json.dumps(j2))
    
    return hashMap

def NewFields_onInput(hashMap,_files=None,_data=None):
    
    hashMap.put("toast",hashMap.get('login')+"|"+hashMap.get('password'))
    return hashMap

def progress_btns(hashMap,_files=None,_data=None):
    time.sleep(3)
    return hashMap

def thread_progress(hashMap,_files=None,_data=None):
    py ="""import time
time.sleep(5)
hashMap.put("beep","")"""


    hashMap.put("RunPyThreadProgress",base64.b64encode(py.encode('utf-8')).decode('utf-8'))

    return hashMap   

def customcards_on_open(hashMap,_files=None,_data=None):
    
    j = { "customcards":         {
            
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
                "type": "Picture",
                "show_by_condition": "",
                "Value": "@pic1",
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
    for i in range(0,2):
        c =  {
        "key": str(i),
        "descr": "Pos. "+str(i),
        "val": str(random.randint(10, 10000))+" руб.",
        "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
        "string2": "Гнездо процессора LGA 1700",
        "string3": "Частотная спецификация памяти 4800 МГц"
      }
        j["customcards"]["cardsdata"].append(c)

    hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    
    return hashMap


def customtable_on_open(hashMap,_files=None,_data=None):
    
    j = { "customtable":         {
            
            "layout":  {
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
          "type": "Picture",
          "show_by_condition": "",
          "Value": "@pic1",
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
   
    j["customtable"]["tabledata"]=[]
    for i in range(0,3):
        c =  {
        "key": str(i),
        "descr": "Pos. "+str(i),
        "val": str(random.randint(10, 10000))+" руб.",
        "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
        "string2": "Гнездо процессора LGA 1700",
        "string3": "Частотная спецификация памяти 4800 МГц"
      }
        j["customtable"]["tabledata"].append(c)

    hashMap.put("table",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    
    return hashMap
    

def set_tiles(hashMap,_files=None,_data=None):

    small_tile={
    "type": "LinearLayout",
    "orientation": "vertical",
    "height": "match_parent",
    "width": "match_parent",
    "weight": "0",
    "Elements": [
        {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@room",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "15",
            "TextColor": "#FFFFFF",
            "TextBold": True,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "wrap_content",
            "weight": 0,
            "gravity_horizontal": "center"
        },
        {
            "type": "LinearLayout",
            "orientation": "horizontal",
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "1",
            "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "Текущая",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "0",
                    "TextColor": "#ffffff",
                    "TextBold": False,
                    "TextItalic": False,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@temp",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "0",
                    "TextColor": "#ffffff",
                    "TextBold": False,
                    "TextItalic": False,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0
                }
            ]
        },
        {
            "type": "LinearLayout",
            "orientation": "horizontal",
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "1",
            "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "Диапазон",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "0",
                    "TextColor": "#ffffff",
                    "TextBold": False,
                    "TextItalic": False,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@rate",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "0",
                    "TextColor": "#ffffff",
                    "TextBold": False,
                    "TextItalic": False,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0
                }
            ]
        },
        {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@port",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "-1",
            "TextColor": "#ffffff",
            "TextBold": True,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "wrap_content",
            "weight": 0
        }
    ]
}


    wide_tile={
    "type": "LinearLayout",
    "orientation": "vertical",
    "height": "match_parent",
    "width": "match_parent",
    "weight": "0",
    "Elements": [
        {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@room",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "15",
            "TextColor": "#FFFFFF",
            "TextBold": True,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "wrap_content",
            "weight": 0,
            "gravity_horizontal": "center"
        },
        {
            "type": "Chart",
            "show_by_condition": "",
            "Value": "@pie1",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "11",
            "TextColor": "",
            "TextBold": False,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "match_parent",
            "weight": 1
        }
    ]
}

    
    tiny_tile={
    "type": "LinearLayout",
    "orientation": "vertical",
    "height": "match_parent",
    "width": "match_parent",
    "weight": "0",
    "Elements": [
        {
            "type": "Picture",
            "show_by_condition": "",
            "Value": "^pic",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "11",
            "TextColor": "",
            "TextBold": False,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "match_parent",
            "weight": 1
        }
    ]
}

    j = {
  "tiles": [
    [
      {
        "layout": small_tile,
        "data": {
          "room": "котельная",
          "temp": "23°C",
          "rate": "11°C...28°C",
          "port": "N1"
        },
        "color": "#78002e",
        "start_screen": "",
        "start_process": "Процесс 1"
      },
      {
        "layout": small_tile,
        "data": {
          "room": "водоподготовка",
          "temp": "24°C",
          "rate": "11°C...29°C",
          "port": "N1"
        },
        "color": "#78002e",
        "start_screen": "",
        "start_process": "Процесс 2"
      }
    ],
    [
      {
        "layout": small_tile,
        "data": {
          "room": "котельная #2",
          "temp": "23°C",
          "rate": "10°C...22°C",
          "port": "N2"
        },
        "color": "#e53935",
        "start_screen": "",
        "start_process": "Процесс 2"
      },
      {
        "layout": small_tile,
        "data": {
          "room": "станция ВЭО",
          "temp": "норма",
          "rate": "",
          "port": ""
        },
        "color": "#78002e",
        "start_screen": "",
        "start_process": "Процесс 1"
      }
    ],
    [
      {
        "layout": wide_tile,
        "data": {
          "room": "Отопление",
          "default_temp": "23°C",
          "temp":"°C-",
          "state_pic": "^flame"
        },
        "color": "#4b830d",
        "start_screen": "",
        "start_process": "Редактирование процесс"
      }
    ],
    [
      {
        "layout": tiny_tile,
        "data": {
          "pic": "home"
        },
        "color": "#26a69a",
        "start_screen": "",
        "start_process": "Процесс 1"
      },
      {
        "layout": tiny_tile,
        "data": {
          "pic": "mail"
        },
        "color": "#00acc1",
        "start_screen": "",
        "start_process": "Процесс 2"
      },
      {
        "layout": tiny_tile,
        "data": {
          "pic": "notification"
        },
        "color": "#320b86",
        "start_screen": "",
        "start_process": "Процесс 2"
      },
      {
        "layout": tiny_tile,
        "data": {
          "pic": "notification"
        },
        "color": "#320b86",
        "start_screen": "",
        "start_process": "Процесс 2"
      }
    ],
    [
      {
        "layout": wide_tile,
        "data": {
          "room": "ГВС Контур 1",
          "default_temp": "23°C",
          "temp": "22°C",
          "state_pic": ""
        },
        "color": "#64b5f6",
        "start_screen": "",
        "start_process": "Редактирование процесс"
      }
    ]
  ],
  "background_color": "#f5f5f5"
}

    hashMap.put("tiles",json.dumps(j,ensure_ascii=False).encode('utf8').decode())

    return hashMap    


def customcards_touch(hashMap,_files=None,_data=None):
  hashMap.put("toast","res="+str(hashMap.get("selected_card_key")))
  return hashMap