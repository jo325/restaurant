import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_menu_items():
    """Retrieve all menu items from the database."""
    return app_tables.menu_items.search()