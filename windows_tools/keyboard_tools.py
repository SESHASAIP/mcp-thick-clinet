import uiautomation as auto
import time

def type_text(text: str, interval: float = 0.05):
    """
    Types text character by character.
    Using uiautomation.SendKeys.
    """
    # SendKeys supports raw text, but need to be careful with special chars if they look like keys.
    # uiautomation keys format is {KeyName}. 
    # For plain text typing, simple string usually works unless it contains braces.
    # If text has braces, we might need to escape or send chars individually.
    auto.SendKeys(text, interval=interval)

def paste(text: str):
    """
    Pastes text using the clipboard.
    Native Windows clipboard set + Ctrl-V.
    """
    auto.SetClipboardText(text)
    time.sleep(0.1)
    auto.SendKeys('{Ctrl}v')

def press_key(key: str):
    """
    Presses a single key.
    Examples: 'enter', 'tab', 'esc'.
    Mapped to uiautomation format (Capitalized + braces).
    """
    # Simple mapping for common lowercase keys to uiautomation format
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
    # If not in map, assume it's already correct or a simple character
    if not formatted_key.startswith('{') and len(formatted_key) > 1:
         formatted_key = f'{{{formatted_key.title()}}}'
         
    auto.SendKeys(formatted_key)

def press_hotkey(*keys):
    """
    Presses a combination of keys (e.g. 'ctrl', 'c').
    uiautomation format: '{Ctrl}c'
    """
    # Logic to unnecessary since auto.SendKeys handles combos if formatted right.
    # But usually hotkeys are sent as '{Modifier}Key'.
    # Example user call: press_hotkey('ctrl', 'enter') -> '{Ctrl}{Enter}'?
    # uiautomation typically holds modifiers if you do SendKeys('{Ctrl}(c)') or similar combiners
    # or just simple '{Ctrl}c'.
    
    # Construct command string
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
            # The final non-modifier key
            normal_key = k
            
    # For the normal key, check mapping
    key_map = {
        'enter': '{Enter}',
        'tab': '{Tab}'
    }
    normal_key = key_map.get(normal_key, normal_key)
    
    auto.SendKeys(cmd + normal_key)
