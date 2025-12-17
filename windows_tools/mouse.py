import uiautomation as auto

def click(x: int, y: int):
    """Clicks at the specified coordinates."""
    auto.Click(x, y)

def double_click(x: int, y: int):
    """Double-clicks at the specified coordinates."""
    auto.DoubleClick(x, y)

def right_click(x: int, y: int):
    """Right-clicks at the specified coordinates."""
    auto.RightClick(x, y)

def scroll(amount: int):
    """
    Scrolls the mouse wheel. 
    uiautomation.WheelDown/Up take number of 'notches'.
    PyAutoGUI 'amount' was roughly pixels? 
    Let's map amount to wheel clicks.
    """
    if amount > 0:
        auto.WheelUp(clicks=1)
    else:
        auto.WheelDown(clicks=1)

def move(x: int, y: int):
    """Moves the mouse to the coordinates."""
    auto.SetCursorPos(x, y)
