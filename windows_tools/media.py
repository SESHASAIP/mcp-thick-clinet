import pyautogui

def play_pause():
    """Toggles media play/pause."""
    pyautogui.press('playpause')

def next_track():
    """Skips to next track."""
    pyautogui.press('nexttrack')

def prev_track():
    """Goes to previous track."""
    pyautogui.press('prevtrack')

def volume_up():
    """Increases system volume."""
    pyautogui.press('volumeup')

def volume_down():
    """Decreases system volume."""
    pyautogui.press('volumedown')

def mute():
    """Toggles system mute."""
    pyautogui.press('volumemute')
