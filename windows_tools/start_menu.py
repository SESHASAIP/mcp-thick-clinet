import uiautomation as auto
import time
from . import system
from . import keyboard_tools

def open_start_menu() -> None:
    """
    Opens the Windows Start menu by simulating a press of the Windows key.
    
    This function is useful to return the system to a known state or to begin
    searching for an application.
    """
    auto.SendKeys('{Win}')
    system.wait(1.0)

def search_app(app_name: str) -> None:
    """
    Opens the Start menu and types the name of an application to search for it.
    
    This does NOT launch the application. It leaves the Start menu open with
    search results visible. Use `launch_app` to open it.

    Args:
        app_name (str): The name of the application to search for (e.g., "Notepad", "Mail").
    """
    open_start_menu()
    keyboard_tools.type_text(app_name, interval=0.1)
    system.wait(1.0) 

def launch_app(app_name: str) -> None:
    """
    Opens the Start menu, searches for an application, and launches it.
    
    This is the primary method for opening new applications. It waits for 3 seconds
    after launching to allow the application to appear.

    Args:
        app_name (str): The name of the application to launch (e.g., "Chrome", "Spotify").
    """
    search_app(app_name)
    auto.SendKeys('{Enter}')
    system.wait(3.0) 
