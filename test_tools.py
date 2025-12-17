import time
from windows_tools import start_menu, window_mgmt, keyboard_tools, mouse, inspector, system, app_mail

def test_phase_1():
    print("Testing Phase 1 Tools...")
    
    print("1. Opening Start Menu...")
    start_menu.open_start_menu()
    system.wait(1)
    
    print("2. Launching Notepad (Test target)...")
    start_menu.launch_app("Notepad")
    system.wait(2)
    
    print("3. Checking Window...")
    if window_mgmt.set_foreground("Notepad"):
        print("   Notepad focused successfully.")
    else:
        print("   FAILED to focus Notepad.")
        return

    print("4. Typing test...")
    keyboard_tools.type_text("Hello User! This is the Windows Agent.")
    keyboard_tools.press_key("enter")
    keyboard_tools.paste("This text was pasted securely.")
    
    print("5. Testing Inspector (Looking for 'File' menu)...")
    file_menu = inspector.find_element(name="File", control_type="MenuItem")
    if file_menu:
        print(f"   Found 'File' menu at {file_menu['center']}")
        mouse.click(*file_menu['center'])
        system.wait(0.5)
        # Click away to close menu
        mouse.click(500, 500) 
    else:
        print("   Could not find 'File' menu (might be expected depending on Notepad version).")

    print("\n--- Mail App Workflow Simulation ---")
    print("Do you want to run the ACTUAL Mail app test? (It will send an email if configured)")
    # We won't block here in automation, but user can uncomment
    # app_mail.compose_new_email("test@example.com", "Agent Test", "Success!")

    print("\nPhase 1 Test Complete.")

if __name__ == "__main__":
    test_phase_1()
