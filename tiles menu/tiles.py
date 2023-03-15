import json
import random

j ={
  "tiles": [
    [
      {
        "template": "Узкая плитка 1",
        "data": {
          "room": "котельная",
          "temp": str(random.randint(0,100))+ " °C",
          "rate": "11°C...28°C",
          "port": "N1"
      },
      "color": "#78002e",
      "start_screen": "",
      "start_process": "Процесс 1"
    },
    {
      "template": "Узкая плитка 1",
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
        "template": "Широкая плитка 1",
        "data": {
          "room": "Отопление",
          "default_temp": "23°C",
          "temp":str(random.randint(0,100))+ " °C"
        },
        "color": "#4b830d",
        "start_screen": "",
        "start_process": "Редактирование процесс"
      }
    ],
    [
      {
        "template": "Маленькая плитка Awesome",
        "data": {
          "pic": "#f019"
        },
        "color": "#26a69a",
        "start_screen": "",
        "start_process": "Процесс 1"
      },
      {
        "template": "Маленькая плитка Awesome",
        "data": {
          "pic": "#f48b"
        },
        "color": "#00acc1",
        "start_screen": "",
        "start_process": "Процесс 2"
      },
      {
        "template": "Маленькая плитка",
        "data": {
          "pic": "list"
        },
        "color": "#320b86",
        "start_screen": "",
        "start_process": "Процесс 2"
      },
      {
        "template": "Маленькая плитка",
        "data": {
          "pic": "chat"
        },
        "color": "#320b86",
        "start_screen": "",
        "start_process": "Процесс 2"
      }
    ]
  ],
  "background_color": "#f5f5f5"
}

def timer(hashMap,_files=None,_data=None):

  #hashMap.put("beep","")

 
  hashMap.put("RefreshMenu","")
  hashMap.put("_tiles",json.dumps(j))
  hashMap.put("temp",str(random.randint(0,100)))

  return hashMap

def on_open(hashMap,_files=None,_data=None):
  
 
  hashMap.put("RefreshMenu","")
  hashMap.put("_tiles",json.dumps(j))
  hashMap.put("temp",str(random.randint(0,5)))
  

  return hashMap