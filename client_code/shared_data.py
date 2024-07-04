import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# In shared_data.py
shared_variable = None

def set_shared_data(data):
    global shared_variable
    shared_variable = data

def get_shared_data():
    return shared_variable


