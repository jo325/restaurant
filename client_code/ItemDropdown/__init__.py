from ._anvil_designer import ItemDropdownTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.ui

class ItemDropdown(ItemDropdownTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

        
        # Create the table to display item details
       
    self.item_table = anvil.ui.GridPanel(column_spacing=10, row_spacing=10)
    self.add_component(self.item_table)
        
        # Add the table headers
    self.item_table.add_component(Label(text="Image", width=100, height=50, align="center"))
    self.item_table.add_component(Label(text="Name", width=150, height=50, align="center"))
    self.item_table.add_component(Label(text="Price", width=100, height=50, align="center"))
    self.item_table.add_component(Label(text="Description", width=300, height=50, align="center"))
    # Any code you write here will run before the form opens.
