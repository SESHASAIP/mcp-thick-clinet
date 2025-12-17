import uiautomation as auto

def click(x: int, y: int) -> None:
    """
    Simulates a left mouse click at the absolute screen coordinates (x, y).

    Args:
        x (int): The horizontal pixel coordinate.
        y (int): The vertical pixel coordinate.
    """
    auto.Click(x, y)

def double_click(x: int, y: int) -> None:
    """
    Simulates a double left mouse click at the absolute screen coordinates (x, y).

    Args:
        x (int): The horizontal pixel coordinate.
        y (int): The vertical pixel coordinate.
    """
    auto.DoubleClick(x, y)

def right_click(x: int, y: int) -> None:
    """
    Simulates a right mouse click at the absolute screen coordinates (x, y).
    Use this to open context menus.

    Args:
        x (int): The horizontal pixel coordinate.
        y (int): The vertical pixel coordinate.
    """
    auto.RightClick(x, y)

def scroll(amount: int) -> None:
    """
    Scrolls the mouse wheel up or down.

    Args:
        amount (int): The number of clicks to scroll. 
            Positive values scroll UP. 
            Negative values scroll DOWN.
    """
    if amount > 0:
        auto.WheelUp(clicks=1)
    else:
        auto.WheelDown(clicks=1)

def move(x: int, y: int) -> None:
    """
    Moves the mouse cursor to the specified absolute screen coordinates without clicking.

    Args:
        x (int): The horizontal pixel coordinate.
        y (int): The vertical pixel coordinate.
    """
    auto.SetCursorPos(x, y)
