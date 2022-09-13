import json


def test_open(hashMap,_files=None,_data=None):
  
  
  hashMap.put("getJSONConfiguration","")
  

  return hashMap

def test_input(hashMap,_files=None,_data=None):
  
  config = json.loads(hashMap.get('_configuration'))

  for process in config['ClientConfiguration']['Processes']:
    if process['type']=='CVOperation':
        for frame in process['CVFrames']:
            frame['CVCameraDevice']="Back"


  hashMap.put('setJSONConfiguration', json.dumps(config, ensure_ascii=False))

  hashMap.put("toast","поменяли")
  

  return hashMap


def screen_open(hashMap,_files=None,_data=None):
 

  hashMap.put("getJSONScreen","")  

  return hashMap

def screen_input(hashMap,_files=None,_data=None):

  screen = json.loads(hashMap.get('JSONScreen'))


  el = screen['Elements'][0]
  new_btn = {
                                        "type": "Button",
                                        "height": "wrap_content",
                                        "width": "wrap_content",
                                        "weight": "0",
                                        "Value": "тест",
                                        "Variable": "btn_change"
                                    }
  el['Elements'].append(new_btn)
      
  hashMap.put("toast",json.dumps(screen, ensure_ascii=False))   

  hashMap.put("setJSONScreen",json.dumps(screen, ensure_ascii=False))  

  return hashMap

  