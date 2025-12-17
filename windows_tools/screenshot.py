from PIL import ImageGrab
import base64
import io
from typing import Optional

def capture_screen(filename: Optional[str] = None) -> str:
    """
    Captures an image of the current screen state.
    
    This function returns a Base64-encoded string of the screenshot, which can be
    passed to Vision-enabled models (like Gemini Pro Vision) to "see" the desktop.
    It can optionally save the image to a file for debugging.

    Args:
        filename (str, optional): If provided, the screenshot will be saved to this file path. 
            Defaults to None.

    Returns:
        str: A Base64 encoded string representing the PNG screenshot image.
    """
    shot = ImageGrab.grab()
    
    if filename:
        shot.save(filename)
        
    buffer = io.BytesIO()
    shot.save(buffer, format="PNG")
    b64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return b64_str
