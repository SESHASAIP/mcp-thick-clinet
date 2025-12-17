import uiautomation as auto
import pywinauto
from pywinauto import Desktop

def list_windows():
    """Returns a list of titles of all visible windows."""
    windows = Desktop(backend="uia").windows()
    return [w.window_text() for w in windows if w.window_text()]

def set_foreground(app_name: str) -> bool:
    """
    Brings a window with a title containing 'app_name' to the foreground.
    This ensures subsequent keyboard/mouse actions target this window.
    """
    try:
        # Using uiautomation for finding; pywinauto also works
        window = auto.WindowControl(searchDepth=1, Name=app_name, SubName=True) 
        # SubName=True allows partial match in uiautomation? 
        # Actually uiautomation regex or substring search usually works by default or needs params.
        # Let's use a simpler loop for robustness if library specifics vary.
        
        if not window.Exists(maxSearchSeconds=1):
             # Manual search
             for win in auto.GetRootControl().GetChildren():
                 if app_name.lower() in win.Name.lower():
                     window = win
                     break
        
        if window and window.Exists():
            window.SetFocus()
            window.SetActive()
            # Bring to front hack if needed
            window.MoveCursorToMyCenter() 
            # Or use SetForegroundWindow api via ctypes if this fails, 
            # but UIA usually handles it.
            return True
        print(f"Window '{app_name}' not found.")
        return False
    except Exception as e:
        print(f"Error setting foreground: {e}")
        return False
