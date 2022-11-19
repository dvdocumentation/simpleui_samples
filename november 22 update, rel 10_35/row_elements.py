from ru.travelfood.simple_ui import SimpleUtilites as suClass
import json
import random

def tst_input(hashMap,_files=None,_data=None):
    from ru.travelfood.simple_ui import ImportUtils as iuClass
    from android.graphics.drawable import GradientDrawable as GradientDrawable
    from android.graphics import Color
    

    v = iuClass.getView("btn_tst")
    v.setTextColor(-65536)


    shape =  GradientDrawable()
    shape.setShape(GradientDrawable.OVAL)
    shape.setColor(Color.WHITE)
    shape.setStroke(2, Color.BLACK)
    

    v.setBackground(shape)

    hashMap.put("toast",str(v)) 
    hashMap.put("noRefresh","")    
    
    return hashMap 


def lib_open(hashMap,_files=None,_data=None):
    
    import zipfile
    import sys
    import os
    import base64


    whlPath =  suClass.get_stored_file("pygal")
    targetDir = suClass.get_temp_dir()
    sys.path.append(targetDir)
    with zipfile.ZipFile(whlPath, "r") as whl:
        whl.extractall(targetDir)
    sys.path.append(os.path.join(targetDir, 'pygal'))
    import pygal  

   

    bar_chart = pygal.Bar()                                            # Then create a bar graph object
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values


    output_file = suClass.get_temp_file("svg")
    bar_chart.render_to_file(output_file)                          # Save the svg to a file
    
    with open(output_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Using SVG as an image tag</title>
    <link href="index.css" rel="stylesheet" />
  </head>
  <body>
    <img src="data:image/svg+xml;base64,"""+encoded_string+""""/>
  </body>
</html>"""
    
    hashMap.put("html",html)

    return hashMap     

def java_open(hashMap,_files=None,_data=None):
    
    from ru.travelfood.simple_ui import ImportUtils as iuClass
    from android.widget import Switch
    from android.widget import TextView



    sw = Switch(iuClass.getContext())
    sw.setText("Какой то параметр 1")
    
    l1 = iuClass.getView("left")
    l1.addView(sw)

    sw2 = Switch(iuClass.getContext())
    sw2.setText("Какой то параметр 2")
    
    l1 = iuClass.getView("right")
    l1.addView(sw2)


    return hashMap 

def java_input(hashMap,_files=None,_data=None):
    
    from ru.travelfood.simple_ui import ImportUtils as iuClass
    from android.widget import Switch
    from android.widget import TextView


    sw = Switch(iuClass.getContext())
    sw.setText("Какой то параметр еще")
    



    
    


    root = iuClass.getRootLayout()
    root.addView(sw)
    #hashMap.put("toast",str(sw))
    hashMap.put("noRefresh","")  

    return hashMap      


def serv(hashMap,_files=None,_data=None):
    
    if hashMap.get("listener") == "custom_command_kill": 
      hashMap.put("app_shutdown","")  

    if hashMap.get("listener") == "test_customws": 
      hashMap.put("beep","")    

    return hashMap      


def tst1(hashMap,_files=None,_data=None):
    
    hashMap.put("app_shutdown","")  

    return hashMap      


def visible_open(hashMap,_files=None,_data=None):
    
    #пустой обработчик, чтобы применились переменные при отрисовке  

    return hashMap 

def visible_input(hashMap,_files=None,_data=None):
    
    if hashMap.get("listener") == "btn_1": 
      hashMap.put("Show_left","-1")  
    if hashMap.get("listener") == "btn_2": 
      hashMap.put("Show_left","0")
    if hashMap.get("listener") == "btn_3": 
      hashMap.put("Show_lb_left_1","0")
    if hashMap.get("listener") == "btn_clear": 
      hashMap.put("Show_lb_left_1","1")
      hashMap.put("Show_left","1")        

    return hashMap 


def urovo_input(hashMap,_files=None,_data=None):
    
    if hashMap.get("listener")=="barcode":
      hashMap.put("toast",hashMap.get("barcode"))

    if hashMap.get("listener")=="btns":
      if hashMap.get("btns")=="trigger lock on":
        suClass.urovo_set_lock_trigger(True)
      if hashMap.get("btns")=="trigger lock off":
        suClass.urovo_set_lock_trigger(False)
      if hashMap.get("btns")=="open scanner":
        if suClass.urovo_open_scanner():
          suClass.urovo_start_decode()
      if hashMap.get("btns")=="close scanner":
        suClass.urovo_stop_decode()
        #suClass.urovo_close_scanner()      
      #еще есть:
      # boolean urovo_get_scanner_state()
      # boolean urovo_get_lock_trigger_state()

    return hashMap           

def tables_open(hashMap,_files=None,_data=None):
    
    j = { "customtable":         {
       "options":{
              "search_enabled":False,
              "save_position":True
            },
            
            "layout":         


       {
        "type": "LinearLayout",
        "orientation": "horizontal",
        "height": "match_parent",
        "width": "match_parent",
        "weight": "1",
        "Padding": "0",
        "Elements": [
        
         {
          "type": "LinearLayout",
          "orientation": "vertical",
          "height": "match_parent",
          "width": "match_parent",
          "weight": "1",
          "BackgroundColor": "#F0F8FF",
          "Padding": "0",
          "StrokeWidth": "1",
          "Elements": [
           {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@pos",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": ""
           }
               
        ]
    
    },

 {
          "type": "LinearLayout",
          "orientation": "vertical",
          "height": "match_parent",
          "width": "match_parent",
          "weight": "2",
          "BackgroundColor": "#F0F8FF",
          "Padding": "0",
          "StrokeWidth": "1",
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
          "type": "LinearLayout",
          "orientation": "vertical",
          "height": "match_parent",
          "width": "match_parent",
          "weight": "1",
          "BackgroundColor": "#F5DEB3",
          "Padding": "0",
          "StrokeWidth": "1",
          "Elements": [
           {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@val",
            "NoRefresh": False,
            "document_type": "",
            "TextSize": "16",
            "TextColor": "#DB7093",
            "TextBold": True,
            "mask": "",
            "Variable": ""
           }
               
        ]
    
    }

        ]
}
}
}


    red_layout = {
        "type": "LinearLayout",
        "orientation": "horizontal",
        "height": "match_parent",
        "width": "match_parent",
        "weight": "1",
        "Padding": "0",
        "Elements": [
        
         {
          "type": "LinearLayout",
          "orientation": "vertical",
          "height": "match_parent",
          "width": "match_parent",
          "weight": "1",
          "BackgroundColor": "#CD5C5C",
          "Padding": "0",
          "StrokeWidth": "1",
          "Elements": [
           {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@pos",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": ""
           }
               
        ]
    
    },

 {
          "type": "LinearLayout",
          "orientation": "vertical",
          "height": "match_parent",
          "width": "match_parent",
          "weight": "2",
          "BackgroundColor": "#CD5C5C",
          "Padding": "0",
          "StrokeWidth": "1",
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
          "type": "LinearLayout",
          "orientation": "vertical",
          "height": "match_parent",
          "width": "match_parent",
          "weight": "1",
          "BackgroundColor": "#CD5C5C",
          "Padding": "0",
          "StrokeWidth": "1",
          "Elements": [
           {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@val",
            "NoRefresh": False,
            "document_type": "",
            "TextSize": "18",
            "TextColor": "#2E8B57",
            "TextBold": True,
            "mask": "",
            "Variable": ""
           }
               
        ]
    
    }

        ]
}

   
    j["customtable"]["tabledata"]=[]
    for i in range(0,50):
        c =  {
        "key": str(i),
        "descr": "Pos. "+str(i),
        "val": str(random.randint(10, 10000))+" руб.",
        "pos": str(i),
        "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
        "string2": "Гнездо процессора LGA 1700",
        "string3": "Частотная спецификация памяти 4800 МГц"
      }
        if i==2:
          c['_layout']=red_layout

        j["customtable"]["tabledata"].append(c)

    hashMap.put("table",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    
    return hashMap
