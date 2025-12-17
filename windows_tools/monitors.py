import pyautogui

def get_screen_size():
    """Returns the width and height of the primary screen."""
    return pyautogui.size()

def get_mouse_position():
    """Returns the current mouse (x, y) position."""
    return pyautogui.position()

def on_screen(x: int, y: int) -> bool:
    """Checks if coordinates are within the screen info."""
    return pyautogui.onScreen(x, y)
