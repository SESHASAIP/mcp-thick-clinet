import uiautomation as auto
import time

def type_text(text: str, interval: float = 0.05) -> None:
    """
    Simulates typing a string of text on the keyboard.
    
    Use this for short strings into input fields. For large blocks of text,
    consider using `paste` instead.

    Args:
        text (str): The text to type.
        interval (float, optional): The delay in seconds between each keystroke. Defaults to 0.05.
    """
    auto.SendKeys(text, interval=interval)

def paste(text: str) -> None:
    """
    Pastes text at the current cursor location using the system clipboard.
    
    This is faster and more reliable than `type_text` for long content (like email bodies).
    It simulates setting the clipboard and pressing Ctrl+V.

    Args:
        text (str): The text to paste.
    """
    auto.SetClipboardText(text)
    time.sleep(0.1)
    auto.SendKeys('{Ctrl}v')

def press_key(key: str) -> None:
    """
    Presses a single specific key on the keyboard.

    Args:
        key (str): The name of the key to press. 
            Common keys: "enter", "tab", "esc", "backspace", "delete", "win", "space".
            Arrow keys: "up", "down", "left", "right".
    """
    key_map = {
        'enter': '{Enter}',
        'tab': '{Tab}',
        'esc': '{Esc}',
        'escape': '{Esc}',
        'win': '{Win}',
        'windows': '{Win}',
        'backspace': '{Back}',
        'delete': '{Delete}',
        'up': '{Up}',
        'down': '{Down}',
        'left': '{Left}',
        'right': '{Right}',
        'space': '{Space}'
    }
    
    formatted_key = key_map.get(key.lower(), key)
    if not formatted_key.startswith('{') and len(formatted_key) > 1:
         formatted_key = f'{{{formatted_key.title()}}}'
         
    auto.SendKeys(formatted_key)

def press_hotkey(*keys: str) -> None:
    """
    Presses a key combination (hotkey).

    Args:
        *keys (str): A variable number of key names to press together.
            Example: press_hotkey("ctrl", "c")
            Example: press_hotkey("alt", "tab")
    """
    cmd = ""
    normal_key = ""
    
    for k in keys:
        k = k.lower()
        if k in ['ctrl', 'control']:
            cmd += "{Ctrl}"
        elif k in ['alt']:
            cmd += "{Alt}"
        elif k in ['shift']:
            cmd += "{Shift}"
        elif k in ['win']:
            cmd += "{Win}"
        else:
            normal_key = k
            
    key_map = {
        'enter': '{Enter}',
        'tab': '{Tab}'
    }
    normal_key = key_map.get(normal_key, normal_key)
    
    auto.SendKeys(cmd + normal_key)
