from . import inspector
from . import mouse
from . import keyboard_tools
from . import system
from . import window_mgmt

def compose_new_email(to_address: str, subject: str, body: str) -> bool:
    """
    Orchestrates the 'New Email' flow in the Windows Mail app.
    Assumes Mail is already open and in foreground (or handles it).
    """
    # 1. Ensure focus (in case called directly)
    if not window_mgmt.set_foreground("Mail"):
        print("Mail app not found or could not be focused.")
        return False

    # 2. Find "New mail" or "+" button
    # Note: AutomationId might be 'NewMessageButton' or Name 'New mail' depending on version
    new_btn = inspector.find_element(name="New mail", control_type="Button")
    if not new_btn:
        print("Could not find 'New mail' button.")
        return False
    
    mouse.click(*new_btn['center'])
    system.wait(1.0) # Wait for compose window

    # 3. Fill "To"
    # Usually focus starts in "To", but let's be safe and try to find it or just type
    # Robust way: Find "To:" field.
    # Simple way (assuming focus):
    keyboard_tools.type_text(to_address)
    keyboard_tools.press_key('tab') # Often moves to suggestion list or CC
    
    # Mail app behavior varies. 
    # Usually: To -> Tab -> Subject -> Tab -> Body
    # But sometimes To -> Tab -> Select Person -> Enter -> Tab...
    
    # Better: Use Inspector to find "Subject" field to click explicitly if possible,
    # or rely on standard keyboard navigation.
    
    # Heuristic for demo:
    # After typing address, usually need to hit Enter to confirm the "chip", then Tab.
    keyboard_tools.press_key('enter') 
    keyboard_tools.press_key('tab') # Move to Subject
    
    keyboard_tools.type_text(subject)
    keyboard_tools.press_key('tab') # Move to Body
    
    # Body
    keyboard_tools.paste(body) # Use paste for speed/reliability
    
    # 4. Send
    # Find "Send" button
    send_btn = inspector.find_element(name="Send", control_type="Button")
    if send_btn:
        mouse.click(*send_btn['center'])
        return True
    else:
        # Fallback hotkey? Ctrl+Enter usually works in Outlook/Mail
        keyboard_tools.press_hotkey('ctrl', 'enter')
        return True
