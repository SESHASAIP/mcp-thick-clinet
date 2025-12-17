import uiautomation as auto

def get_screen_size():
    """Returns the width and height of the primary screen."""
    width = auto.GetSystemMetrics(0) # SM_CXSCREEN
    height = auto.GetSystemMetrics(1) # SM_CYSCREEN
    return (width, height)

def get_mouse_position():
    """Returns the current mouse (x, y) position."""
    return auto.GetCursorPos()

def on_screen(x: int, y: int) -> bool:
    """Checks if coordinates are within the screen info."""
    w, h = get_screen_size()
    return 0 <= x < w and 0 <= y < h
