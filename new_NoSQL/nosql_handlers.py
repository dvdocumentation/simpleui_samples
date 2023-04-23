import json
from ru.travelfood.simple_ui import NoSQL as noClass
from java import jclass

# это для нативного тоста (но в 11 Андроиде импорт библиотеки com.chaquo.python - вызывает ошибку, и приводит к неработоспособности всех функций)
# from android.widget import Toast
# from com.chaquo.python import Python


def putget_input(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("test_new_nosql")

    if hashMap.get("listener") == "btn_text":
        ncl.put("k1", "Это строка", True)
        res1 = ncl.get("k1")
        # Toast.makeText(Python.getPlatform().getApplication(), str(res1)+" тип "+str(type(res1)),
        #               Toast.LENGTH_SHORT).show()
        hashMap.put("toast", f"`{res1}`: тип {type(res1)}")

    if hashMap.get("listener") == "btn_number":
        ncl.put("k2", 555, True)
        res2 = ncl.get("k2")
        # Toast.makeText(Python.getPlatform().getApplication(), str(res2)+" тип "+str(type(res2)),
        #               Toast.LENGTH_SHORT).show()
        hashMap.put("toast", f"`{res2}`: тип {type(res2)}")

    if hashMap.get("listener") == "btn_boolean":
        ncl.put("k3", True, True)
        res3 = ncl.get("k3")
        # Toast.makeText(Python.getPlatform().getApplication(), str(res3)+" тип "+str(type(res3)),
        #               Toast.LENGTH_SHORT).show()
        hashMap.put("toast", f"`{res3}`: тип {type(res3)}")

    if hashMap.get("listener") == "btn_destroy":
        ncl.destroy()
        hashMap.put("speak", "Attention! All data has been destroyed!")
    return hashMap 


def putget_start(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    ncl = noClass("test_new_nosql")

    results={
    "type": "table",
    "textsize": "25",
    "hidecaption": "false",
    "hideinterline": "false",
    "columns": [
    {
        "name": "k",
        "header": "Ключ",
        "weight": "1"
    },
    {
        "name": "v",
        "header": "Значение",
        "weight": "1"
    }
    ],
    "rows": []
    }             

    keys = ncl.getallkeys()
    hashMap.put("toast", str(keys))
    
    jkeys = json.loads(keys)
    for k in jkeys:
        results['rows'].append({"k": str(k), "v": str(ncl.get(k))})

    hashMap.put("table", json.dumps(results))
    return hashMap     


def search_input(hashMap, _files=None, _data=None):
    ncl = noClass("test_new_nosql")
    j1 = {"name": "Иван", "surname": "Синицын"}
    ncl.put("jk1", json.dumps(j1, ensure_ascii=False), True)

    j2 = {"name": "Дарья", "surname": "Фролова"}
    ncl.put("jk2", json.dumps(j2, ensure_ascii=False), True)

    j3 = {"name": "Дарья", "surname": "Смирнова"}
    ncl.put("jk3", json.dumps(j3, ensure_ascii=False), True)

    # Поиск без индекса
    # res = ncl.findJSON("name", "Дарья")
    # jres = json.loads(str(res).encode("utf-8"))

    # Поиск по индексу
    res = ncl.findJSON_index("surnameindx", "surname", "Синицын")
    jres = json.loads(str(res).encode("utf-8"))   

    hashMap.put("toast", str(jres))
    return hashMap   


def init(hashMap, _files=None, _data=None):
    ncl = noClass("test_new_nosql")
    ncl.run_index("surnameindx", "surname")

    return hashMap
