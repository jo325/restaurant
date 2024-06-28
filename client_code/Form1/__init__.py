from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.items = anvil.server.call('get_category')
    item = self.items
    # Create the dropdown and populate it with items
    self.category_dropdown = item
    

  def category_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    selected_item = self.category_dropdown.selected_value
    # Do something with the selected item
    print(selected_item)
