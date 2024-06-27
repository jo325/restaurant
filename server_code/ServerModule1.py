import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_category():
   
    items = list(app_tables.categories.search())
    return [(item['name'], item['image'], item['price'], item['description']) for item in items]