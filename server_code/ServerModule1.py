import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from datetime import datetime

@anvil.server.callable
def get_menu_items():
    """Retrieve all menu items from the database."""
    return app_tables.menu_items.search()


@anvil.server.callable
def add_to_cart(name,price,quantity):
    # Check if the cart exists in the session, otherwise initialize it
    if 'cart' not in anvil.server.session:
        anvil.server.session['cart'] = []
    
    # Add the item to the cart
    anvil.server.session['cart'].append({"name":name ,"price": price, "quantity": quantity})

@anvil.server.callable
def get_cart():
    # Retrieve the cart from the session
    cart = anvil.server.session.get('cart', [])
    return cart

@anvil.server.callable
def place_order(table_number, order_items):
    #new_order=[]
    items =None
    """Place a new order in the database."""
    new_order = app_tables.orders.add_row(
        table_no=table_number,
        timestamp=datetime.now(),
        status='Pending'
    )
    for items in order_items:
       app_tables.order_items.add_row(
          order_id = new_order,
          item = anvil.server.call('get_cart')
        )
    
    return new_order

@anvil.server.callable
def add_pending(self, table_number):
  
  if 'pend' not in anvil.server.session:
      anvil.server.session['pend'] = []
    
    # Add the item to the cart
  anvil.server.session['pend'].append({'table_number':table_number ,'status':'pending'})

@anvil.server.callable
def get_pending():
   cart = anvil.server.session.get('pend', [])
   return cart
  
  