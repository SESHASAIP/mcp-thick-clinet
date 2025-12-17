import pyautogui
import base64
import io
from typing import Optional

def capture_screen(filename: Optional[str] = None) -> str:
    """
    Captures the entire screen.
    Returns: A base64 encoded string of the PNG image (for LLM consumption).
    if filename is provided, also saves to disk.
    """
    shot = pyautogui.screenshot()
    
    if filename:
        shot.save(filename)
        
    buffer = io.BytesIO()
    shot.save(buffer, format="PNG")
    b64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return b64_str
