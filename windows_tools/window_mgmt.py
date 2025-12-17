import uiautomation as auto
from pywinauto import Desktop
from typing import List

def list_windows() -> List[str]:
    """
    Retrieves a list of titles for all currently visible windows on the desktop.
    
    Use this to see what applications are currently running and available to switch to.

    Returns:
        List[str]: A list of window title strings.
    """
    windows = Desktop(backend="uia").windows()
    return [w.window_text() for w in windows if w.window_text()]

def set_foreground(app_name: str) -> bool:
    """
    Brings the window containing the specified name to the foreground and gives it input focus.
    
    This is extremely important! You must call this before typing or clicking in an application
    to ensure your actions go to the correct place.

    Args:
        app_name (str): A substring of the window title to find and focus (e.g., "Mail", "Notepad").

    Returns:
        bool: True if the window was found and focused, False otherwise.
    """
    try:
        window = auto.WindowControl(searchDepth=1, Name=app_name, SubName=True) 
        
        if not window.Exists(maxSearchSeconds=1):
             for win in auto.GetRootControl().GetChildren():
                 if app_name.lower() in win.Name.lower():
                     window = win
                     break
        
        if window and window.Exists():
            window.SetFocus()
            window.SetActive()
            window.MoveCursorToMyCenter() 
            return True
        print(f"Window '{app_name}' not found.")
        return False
    except Exception as e:
        print(f"Error setting foreground: {e}")
        return False
