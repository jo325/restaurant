import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
    """Place a new order in the database."""
    new_order = app_tables.orders.add_row(
        table_no=table_number,
        timestamp=datetime.now(),
        status='Pending'
    )
    
    for item in order_items:
        app_tables.order_items.add_row(
            order=new_order,
            item=item['item'],
            quantity=item['quantity']
        )
    
    return new_order