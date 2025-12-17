import uiautomation as auto
import time
from . import system
from . import keyboard_tools

def open_start_menu():
    """Opens the Windows Start menu."""
    auto.SendKeys('{Win}')
    system.wait(1.0)

def search_app(app_name: str):
    """
    Opens the start menu and searches for an app.
    """
    open_start_menu()
    keyboard_tools.type_text(app_name, interval=0.1)
    system.wait(1.0) 

def launch_app(app_name: str):
    """Opens start, searches, and launches the app."""
    search_app(app_name)
    auto.SendKeys('{Enter}')
    system.wait(3.0) 
