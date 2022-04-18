from flask import Flask
from flask import request
import json
app = Flask(__name__)

goods_sample = [{"barcode":"740617303506","sku":"Kingston SSD M2 512Mb"},{"barcode":"8901043000427","sku":"SiliconePower SSD 256Mb"},{"barcode":"4009932559132","sku":"Samsung SSD 1024 Mb"}]

def barcode_on_input():
    #handlers code
    if hashMap.get("listener")=='barcode': #check scan event
        b = hashMap.get('barcode') #barcode variable
        nom = next((item for item in goods_sample if item["barcode"] == b), None) #search by barcode value
        
        #inserting displaying value
        if b==None:
            hashMap.put('nom',"<Неизвестный штрихкод>")    
        else:    
            hashMap.put('nom',nom['sku'])

        #command to show a specific screen
        hashMap.put('ShowScreen','Ввод количества')


@app.route('/set_input_direct/<method>', methods=['POST'])
def set_input(method):
    func = method
    jdata = json.loads(request.data.decode("utf-8"))
    f = globals()[func]
    hashMap.d=jdata['hashmap']
    f()
    jdata['hashmap'] = hashMap.export()
    jdata['stop'] =False
    jdata['ErrorMessage']=""
    jdata['Rows']=[]

    return json.dumps(jdata)

@app.route('/post_screenshot', methods=['POST'])
def post_screenshot():
    d = request.data
    return "1"

class hashMap:
    d = {}
    def put(key,val):
        hashMap.d[key]=val
    def get(key):
        return hashMap.d.get(key)
    def remove(key):
        if key in hashMap.d:
            hashMap.d.pop(key)
    def containsKey(key):
        return  key in hashMap.d
    def export():
        ex_hashMap = []
        for key in hashMap.d.keys():
            ex_hashMap.append({"key":key,"value":hashMap.d[key]})
        return ex_hashMap

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=2075,debug=True)