import pyautogui
import time
from . import system
from . import keyboard_tools

def open_start_menu():
    """Opens the Windows Start menu."""
    pyautogui.press('win')
    system.wait(1.0) # Wait for animation

def search_app(app_name: str):
    """
    Opens the start menu and searches for an app.
    Does NOT press enter to launch; leaves it in search state.
    """
    open_start_menu()
    keyboard_tools.type_text(app_name, interval=0.1)
    system.wait(1.0) # Wait for search results

def launch_app(app_name: str):
    """Opens start, searches, and launches the app."""
    search_app(app_name)
    pyautogui.press('enter')
    system.wait(3.0) # Standard wait for app launch
