import json
import random
from tempfile import tempdir

cells=["1-1","1-2","1-3","1-4","1-5","1-6","1-7","1-8","2-1","2-2","2-3","2-4","2-5","2-6","2-7","2-8","3-1","3-2","3-3","3-4","3-5","3-6","3-7","3-8","001","5-1","5-2","5-3","5-4","5-5","6-1","6-2","6-3","6-4","6-5","7-1","7-2","7-3","7-4","7-5","ОТБ"] 
gradient=["#139c13","#d3f562","#f59c02","#f28383","#c71a1a"]

def map_on_open(hashMap,_files=None,_data=None):
  
  cellfrom = cells[random.randint (0,len(cells)-1)]
  cellto = cells[random.randint (0,len(cells)-1)]
  cellto2 = "ОТБ"

  cellblue = cells[random.randint (0,len(cells)-1)]
  
  paint_cells=[{"color":"#f56042","cells":[cellfrom,cellto,cellto2]},{"color":"#2a60b8","cells":[cellblue]}]  

  hashMap.put("map_highlight_cells",json.dumps(paint_cells))

  hashMap.put("map_add_move",json.dumps([{"from":cellfrom,"to":cellto},{"from":cellto,"to":cellto2}]))
  

  #hashMap.put("map_zoom","1.2")
  #hashMap.put("map_move_x","-100")

  hashMap.put("toast",json.dumps({"from":cellfrom,"to":cellto}))
  

  return hashMap

def map_on_open_nav(hashMap,_files=None,_data=None):
  
  cellfrom = cells[random.randint (0,len(cells)-1)]
  cellto = cells[random.randint (0,len(cells)-1)]
  cellto2 = "ОТБ"

  cellblue = cells[random.randint (0,len(cells)-1)]
  
  paint_cells=[{"color":"#f56042","cells":[cellfrom,cellto,cellto2]},{"color":"#2a60b8","cells":[cellblue]}]  

  hashMap.put("map_highlight_cells",json.dumps(paint_cells))

  hashMap.put("map_add_move",json.dumps([{"from":cellfrom,"to":cellto},{"from":cellto,"to":cellto2}]))
  

  #hashMap.put("map_zoom","1.2")
  #hashMap.put("map_move_x","-100")

  hashMap.put("toast",json.dumps({"from":cellfrom,"to":cellto}))
  hashMap.put("map_nav_mode","")
  

  return hashMap

def maptags_on_open(hashMap,_files=None,_data=None):
  
  
  #hashMap.put("map_set_color",json.dumps([{"tag":"arr2","color":"#b23e32"}]))
  
  #hashMap.put("toast","есть")
  

  return hashMap

def maptags_down(hashMap,_files=None,_data=None):
  
  hashMap.put("toast","event="+str(hashMap.get("event"))+", listener="+str(hashMap.get("listener"))+", tag="+str(hashMap.get("map_tag")))
  
  if str(hashMap.get("event"))=="MapAction":
    #hashMap.put("speak","15")
    if hashMap.get("listener")=="map_action_down":
      #hashMap.put("speak","down")
      hashMap.put("map_set_color",json.dumps([{"tag":str(hashMap.get("map_tag")),"color":"#a83c32"}]))
      hashMap.put("beep","")
    if hashMap.get("listener")=="map_action_up":
      #hashMap.put("speak","up")
      hashMap.put("map_set_color",json.dumps([{"tag":str(hashMap.get("map_tag")),"color":"#000000"}]))
      hashMap.put("beep","50")

  return hashMap

def tags2_input(hashMap,_files=None,_data=None):
  
  if hashMap.get("listener")=="btn_1":
    hashMap.put("map_set_color",json.dumps([{"tag":"arr1","color":"#a83c32"},{"tag":"btn1","color":"#a83c32"}]))
  if hashMap.get("listener")=="btn_2":  
    hashMap.put("map_set_visibility",json.dumps([{"tag":"arr2","visible":0},{"tag":"btn2","visible":0}]))
  if hashMap.get("listener")=="btn_3":  
    hashMap.put("map_set_color",json.dumps([{"tag":"arr1","color":"#000000"},{"tag":"btn1","color":"#000000"}]))  
    hashMap.put("map_set_visibility",json.dumps([{"tag":"arr2","visible":1},{"tag":"btn2","visible":1}]))

  return hashMap


def inputs_on_open(hashMap,_files=None,_data=None):
  
  if not hashMap.containsKey("btn_next"):
    hashMap.put("btn_next","0 из 3")
  else:
    if hashMap.containsKey("begin"):
      hashMap.put("btn_next","1 из 3")
    if hashMap.containsKey("middle"):
      hashMap.put("btn_next","2 из 3")  

  return hashMap

def diagramm_on_open(hashMap,_files=None,_data=None):
  
  hashMap.put("map_set_visibility",json.dumps([{"tag":"arr1","visible":0},{"tag":"arr2","visible":0},{"tag":"arr3","visible":1},{"tag":"arr4","visible":0},{"tag":"arr5","visible":0}])) 
  hashMap.put("map_set_color",json.dumps([{"tag":"arr3","color":"#CA211E"},{"tag":"t3","color":"#CA211E"},{"tag":"t4","color":"#8E8787"},{"tag":"t5","color":"#8E8787"},{"tag":"t1","color":"#156712"},{"tag":"t2","color":"#156712"}])) 
  
  return hashMap

  
def edit_mode_on_open(hashMap,_files=None,_data=None):
  hashMap.put("mm_local","")

  hashMap.put("map_edit_mode","") 

 
  
  return hashMap  

def edit_mode_on_input(hashMap,_files=None,_data=None):
  
  if hashMap.get("listener")=="photo":

    hashMap.put("map_background_picture",hashMap.get("photo_path")) 
  elif hashMap.get("listener")=="":
    hashMap.put("map_save","") 
  
  return hashMap    


def edit_mode2_on_open(hashMap,_files=None,_data=None):

  from ru.travelfood.simple_ui import SimpleUtilites as suClass
  from jinja2 import Template
  
  


  filename = suClass.get_stored_file("bill")

  with open(filename) as file_:
        htmltxt = file_.read()

  htmltxt.replace("&nbsp"," ")
  template = Template(htmltxt)
  lines = []
  for i in range(1, 5):
        i = str(i)
        line = dict(npp=i, name="Товар "+i,price=str(random.randint(10, 10000)),qty=str(random.randint(1, 5)))
        lines.append(line)

  res =template.render(lines=lines,customer = "Дмитрий В.")
  hashMap.put("bill",res)  
  
  return hashMap  

def edit_mode2_on_input(hashMap,_files=None,_data=None):
  
  
 
  hashMap.put("map_background_html","") 
  hashMap.put("ShowScreen","Редактирование") 

  hashMap.put("map_edit_mode","")

  return hashMap 
 
colored_cells=[]

def map_ctrl_on_open(hashMap,_files=None,_data=None):
  
  cellfrom = cells[random.randint (0,len(cells)-1)]
  cellto = cells[random.randint (0,len(cells)-1)]
  cellto2 = "ОТБ"

  cellblue = cells[random.randint (0,len(cells)-1)]
  
  
  paint_cells=[{"color":"#f56042","cells":[cellfrom,cellto,cellto2]},{"color":"#2a60b8","cells":[cellblue]},{"color":"#3e8c3c","cells":colored_cells}]  

  hashMap.put("map_highlight_cells",json.dumps(paint_cells))

  hashMap.put("map_add_move",json.dumps([{"from":cellfrom,"to":cellto},{"from":cellto,"to":cellto2}]))
  

  hashMap.put("map_zoom","1.1")
  hashMap.put("map_move_x","-50")
  hashMap.put("map_move_y","50")

  #hashMap.put("toast",json.dumps({"from":cellfrom,"to":cellto}))
  

  return hashMap

def map_ctrl_down(hashMap,_files=None,_data=None):
  
  hashMap.put("toast","event="+str(hashMap.get("event"))+", listener="+str(hashMap.get("listener"))+", tag="+str(hashMap.get("map_tag")))
  if hashMap.get("listener")=="map_action_down":
    colored_cells.append(str(hashMap.get("map_tag")))

  return hashMap

def color_map_on_open(hashMap,_files=None,_data=None):

  paint_cells=[]  

  
  for color in gradient:
    cs=[]
    for i in range(10):
      cell = cells[random.randint (0,len(cells)-1)]
      cs.append(cell) 
    c = {"color":color,"cells":cs}  
    paint_cells.append(c)
  
  
  hashMap.put("map_highlight_cells",json.dumps(paint_cells))

  return hashMap  

def code_open(hashMap,_files=None,_data=None):
  
  

  hashMap.put("map_set_size",json.dumps({"width":1000,"height":2000})) 
  
  
  return hashMap

def code_input(hashMap,_files=None,_data=None):
  
  rowslist=[]
  cellsize = 75
  shifty = 0
  n=0
  for i in range(3):
    shiftx=0
    for j in range(5):
      n+=1
      rowslist.append({"x":20+shiftx,"y":30+shifty,"row_count":5,"column_count":1,"cell_size":cellsize,"tags":[[str(n)+"-1",str(n)+"-2",str(n)+"-3",str(n)+"-4",str(n)+"-5"]]})
      shiftx+=1*cellsize+90
    shifty+=5*cellsize+100  
  
  hashMap.put("map_clear_rows","")
  hashMap.put("map_add_rows",json.dumps(rowslist)) 
  hashMap.put("map_add_move",json.dumps([{"from":"1-2","to":"2-2"},{"from":"2-2","to":"3-5"},{"from":"3-5","to":"7-2"},{"from":"7-2","to":"9-5"},{"from":"9-5","to":"13-4"}]))
  return hashMap     