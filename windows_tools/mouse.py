import pyautogui

def click(x: int, y: int):
    """Clicks at the specified coordinates."""
    pyautogui.click(x, y)

def double_click(x: int, y: int):
    """Double-clicks at the specified coordinates."""
    pyautogui.doubleClick(x, y)

def right_click(x: int, y: int):
    """Right-clicks at the specified coordinates."""
    pyautogui.rightClick(x, y)

def scroll(amount: int):
    """Scrolls the mouse wheel. Positive is up, negative is down."""
    pyautogui.scroll(amount)

def move(x: int, y: int):
    """Moves the mouse to the coordinates."""
    pyautogui.moveTo(x, y)
