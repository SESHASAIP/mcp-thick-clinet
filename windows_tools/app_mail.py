from . import inspector
from . import mouse
from . import keyboard_tools
from . import system
from . import window_mgmt

def compose_new_email(to_address: str, subject: str, body: str) -> bool:
    """
    Orchestrates the entire flow of composing and sending a new email in the Windows Mail app.
    
    This high-level tool automates:
    1. Finding the "New mail" button.
    2. Filling out the "To", "Subject", and "Body" fields.
    3. Clicking "Send" (or pressing Ctrl+Enter).

    Precondition: The Mail app should be running (use `launch_app("Mail")` first if unsure).

    Args:
        to_address (str): The email address of the recipient.
        subject (str): The subject line of the email.
        body (str): The main content of the email message.

    Returns:
        bool: True if the email was presumably sent, False if a UI element (like the New button) could not be found.
    """
    if not window_mgmt.set_foreground("Mail"):
        print("Mail app not found or could not be focused.")
        return False

    new_btn = inspector.find_element(name="New mail")
    # Some versions might just use "+" or "New"
    if not new_btn:
        print("Could not find 'New mail' button.")
        return False
    
    mouse.click(*new_btn['center'])
    system.wait(1.0) 

    keyboard_tools.type_text(to_address)
    keyboard_tools.press_key('enter') 
    keyboard_tools.press_key('tab') 
    
    keyboard_tools.type_text(subject)
    keyboard_tools.press_key('tab') 
    
    keyboard_tools.paste(body) 
    
    # Try to find Send button to click
    send_btn = inspector.find_element(name="Send")
    if send_btn:
        mouse.click(*send_btn['center'])
        return True
    else:
        # Fallback to hotkey
        keyboard_tools.press_hotkey('ctrl', 'enter')
        return True
