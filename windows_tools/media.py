import uiautomation as auto

def play_pause() -> None:
    """Toggles the system media play/pause state."""
    auto.SendKeys('{MediaPlayPause}')

def next_track() -> None:
    """Skips to the next track in the active media player."""
    auto.SendKeys('{MediaNextTrack}')

def prev_track() -> None:
    """Returns to the previous track in the active media player."""
    auto.SendKeys('{MediaPrevTrack}')

def volume_up() -> None:
    """
    Increases the system volume by one step.
    Call this multiple times to raise volume significantly.
    """
    auto.SendKeys('{VolumeUp}')

def volume_down() -> None:
    """
    Decreases the system volume by one step.
    Call this multiple times to lower volume significantly.
    """
    auto.SendKeys('{VolumeDown}')

def mute() -> None:
    """Toggles the system volume mute state."""
    auto.SendKeys('{VolumeMute}')
