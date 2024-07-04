from ._anvil_designer import cookstaffTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..shared_data import shared_data

class cookstaff(cookstaffTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def item_selected(self):
    self.selected_item = shared_data.get_shared_data()
    self.update_display()

  def update_display(self):
    if self.selected_item:
      self.card_1.visible = True
      self.card_1.text = f"Selected: {self.selected_item['table_number']}\nInput: "
    else:
      self.card_1.visible = False