import pyautogui
import pyperclip
import time

def type_text(text: str, interval: float = 0.05):
    """
    Types text character by character. 
    Good for short fields.
    """
    pyautogui.write(text, interval=interval)

def paste(text: str):
    """
    Pastes text using the clipboard.
    Much faster and more reliable for long blocks (like email bodies).
    """
    pyperclip.copy(text)
    time.sleep(0.1) # Wait for clipboard update
    pyautogui.hotkey('ctrl', 'v')

def press_key(key: str):
    """Presses a single key (e.g., 'enter', 'tab', 'esc')."""
    pyautogui.press(key)

def press_hotkey(*keys):
    """Presses a combination of keys (e.g. 'ctrl', 'c')."""
    pyautogui.hotkey(*keys)
