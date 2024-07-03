from ._anvil_designer import ItemTemplatemenuTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class ItemTemplatemenu(ItemTemplatemenuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.counter_value = 0
    self.counter_label.text = str(self.counter_value)
    # Any code you write here will run before the form opens.

  def increment_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.counter_value += 1
    self.counter_label.text = str(self.counter_value)

  def decrement_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.counter_value -= 1
    self.counter_label.text = str(self.counter_value)

  def add_to_order_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    if selected_item:
      new_order_item = {
        'item': selected_item['name'],
        'price': selected_item['price'],
        'quantity': 1
      }
      self.repeating_panel_order.items.append(new_order_item)

