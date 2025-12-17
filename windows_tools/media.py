import uiautomation as auto

def play_pause():
    """Toggles media play/pause."""
    auto.SendKeys('{MediaPlayPause}')

def next_track():
    """Skips to next track."""
    auto.SendKeys('{MediaNextTrack}')

def prev_track():
    """Goes to previous track."""
    auto.SendKeys('{MediaPrevTrack}')

def volume_up():
    """Increases system volume."""
    auto.SendKeys('{VolumeUp}')

def volume_down():
    """Decreases system volume."""
    auto.SendKeys('{VolumeDown}')

def mute():
    """Toggles system mute."""
    auto.SendKeys('{VolumeMute}')
