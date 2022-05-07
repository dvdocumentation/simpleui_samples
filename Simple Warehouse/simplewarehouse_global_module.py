from tokenize import Double
from pony import orm
from pony.orm import Database,Required,Set,Json,PrimaryKey,Optional
from pony.orm.core import db_session
import datetime

db = Database()
db.bind(provider='sqlite', filename='//data/data/ru.travelfood.simple_ui/databases/SimpleWMS', create_db=True)

class SW_Units(db.Entity):
        name =  Required(str)

class SW_Groups(db.Entity):
        name =  Required(str)

class SW_Cells(db.Entity):
        name =  Required(str)
        barcode =  Optional(str)
        
class SW_Goods(db.Entity):
        name =  Required(str)
        product_number =  Optional(str)
        barcode =  Optional(str)
        group = Optional(str)
        unique = Optional(int)
        unit = Required(str)
        price = Optional(float)
        pictures = Optional(Json)
        created_at = Optional(datetime.datetime, sql_default='CURRENT_TIMESTAMP')

class SW_Account(db.Entity):
        sku =  Required(int)
        cell =  Required(int)
        qty =  Required(float)
        
        period = Optional(datetime.datetime, sql_default='CURRENT_TIMESTAMP')
       

class SW_Inventory(db.Entity):
        description =  Required(str)
        created_at = Optional(datetime.datetime, sql_default='CURRENT_TIMESTAMP') 
        lines = Set("SW_Inventory_line")    

class SW_Inventory_line(db.Entity):
        sku =  Required(int)
        cell =  Required(int)
        qty =  Required(float)
        inventory = Required("SW_Inventory")
        
        date = Optional(datetime.datetime, sql_default='CURRENT_TIMESTAMP')          

def init():
    db.generate_mapping(create_tables=True) 
    
