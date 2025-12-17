import uiautomation as auto
from typing import Tuple

def get_screen_size() -> Tuple[int, int]:
    """
    Retrieves the width and height of the primary display in pixels.

    Returns:
        Tuple[int, int]: A tuple containing (width, height).
    """
    width = auto.GetSystemMetrics(0) # SM_CXSCREEN
    height = auto.GetSystemMetrics(1) # SM_CYSCREEN
    return (width, height)

def get_mouse_position() -> Tuple[int, int]:
    """
    Retrieves the current absolute screen coordinates of the mouse cursor.

    Returns:
        Tuple[int, int]: A tuple containing (x, y).
    """
    return auto.GetCursorPos()

def on_screen(x: int, y: int) -> bool:
    """
    Checks if the specified coordinates fall within the primary display's bounds.

    Args:
        x (int): The horizontal coordinate.
        y (int): The vertical coordinate.

    Returns:
        bool: True if inside the screen bounds, False otherwise.
    """
    w, h = get_screen_size()
    return 0 <= x < w and 0 <= y < h
