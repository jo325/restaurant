from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_menu_item = None 
    self.load_menu_items()
    
  def load_menu_items(self):
    # Load menu items from the database
    menu_items = anvil.server.call('get_menu_items')
    self.repeating_panel_menu.items = menu_items
    self.add_to_order()
    # Any code you write here will run before the form opens.

  def add_to_order(self):
      if self.selected_menu_item:
        self.item = anvil.server.call('get_cart')
        self.repeating_panel_order.items=
