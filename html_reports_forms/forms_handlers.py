from asyncore import write
from jinja2 import Template
from bs4 import BeautifulSoup as BS
import base64
import random
from ru.travelfood.simple_ui import SimpleUtilites as suClass

def test_html_input(hashMap,_files=None,_data=None):
    

    t = Template("""{% for user in users -%}
    <p>Привет, {{ user }}!</p>
    {% endfor %}""")
    res =t.render(users=["admin", "Alex", "prog1C"])

    hashMap.put("PrintPreview",res)    
    
    return hashMap  

def template_html_input(hashMap,_files=None,_data=None):
    

    
    import barcode
    from barcode.writer import ImageWriter
    from io import BytesIO
    from barcode import generate
   
    filename = suClass.get_stored_file("template1")

    with open(filename) as file_:
        htmltxt = file_.read()

    htmltxt.replace("&nbsp"," ")
    
    soup = BS(htmltxt)
    for imgtag in soup.find_all('img'):
        EAN = barcode.get_barcode_class('ean13')
        #ean = EAN(u'123456789011', writer=ImageWriter())
        fp = BytesIO()
        generate('EAN13', u'5901234123457', writer=ImageWriter(), output=fp)
        base64data = base64.b64encode(fp.getvalue()).decode('utf-8')
        imgtag['src']="data:image/jpg;base64,"+base64data

 
    htmltxt=str(soup)

    template = Template(htmltxt)
    docdata = { 'number': '1-555', 'customer': "Тульская мануфактура №1",'barcode':'tool.jpg' }

    res =template.render(doc=docdata)

    hashMap.put("PrintPreview",res)  
    
    return hashMap     

def html_field_open(hashMap,_files=None,_data=None):
    
    htmlstring = """
    <!DOCTYPE html>
<html>
<body>

<h1>HTML Приходная накладная {{docdata.doc}} </h1>
    <table>
     <style>
   table {
    width: 100%; /* Ширина таблицы в процентах */
   }
   .col1 {
    width: 100px; /* Ширина ячейки */
   }</style>
  <colgroup>
    <col span="2" style="background:Khaki"><!-- С помощью этой конструкции задаем цвет фона для первых двух столбцов таблицы-->
    <col style="background-color:LightCyan"><!-- Задаем цвет фона для следующего (одного) столбца таблицы-->
  </colgroup>
  {% for item in items %}
<TR>
   <TD class="c1">{{item.npp}}</TD>
   <TD class="c2">{{item.name}}</TD>
   <TD class="c3"><SPAN>{{item.price}}</SPAN></TD>
 
</TR>
{% endfor %}
</table>

<input type="button" onclick="callJS('Кнопка 1')" value="Кнопка 1">
<input type="button" onclick="callJS('Кнопка 2')" value="Кнопка 2">

<script type="text/javascript">
    function callJS(param) {
        Android.onInput(param);
    }
</script>

</body>
</html>
"""

    t = Template(htmlstring)
    docdata = { 'doc': '1555 от 01.08.2022' }


    items = []
    items.append(dict(npp="№ п/п", name="Наименование товара",price="Цена"))
    for i in range(1, 11):
        i = str(i)
        item = dict(npp=i, name="Товар "+i,price=str(random.randint(10, 10000)))
        items.append(item)

    res = t.render(items=items,docdata=docdata)

    hashMap.put("html_value",res)    
    
    return hashMap     


def html_field_input(hashMap,_files=None,_data=None):
    
    if hashMap.get("listener")=="JSClick":
        hashMap.put("toast",hashMap.get("jsdata"))     
        #hashMap.put("noRefresh","")
    
    return hashMap 


def doc_input(hashMap,_files=None,_data=None):
    
    if hashMap.get("listener")=="btn_run":
        
        filename = suClass.get_stored_file("agreement")

    

        with open(filename,encoding='windows-1251') as file_:
            htmltxt = file_.read()
            #htmltxt.replace("&nbsp"," ")
 
        template = Template(htmltxt)
        #docdata = { 'number': '1-555', 'customer': "Воронцов Дмитрий Игоревич" }

        res =template.render(number='1-555',customer= "122")

        hashMap.put("PrintPreview",res)  
        
        return hashMap             


    
def bill_oninput(hashMap,_files=None,_data=None):
    
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

    res =template.render(lines=lines,customer = "Дмитрий Воронцов")
    hashMap.put("bill",res)  
    #hashMap.put("PrintPreview",res)
    
    return hashMap         