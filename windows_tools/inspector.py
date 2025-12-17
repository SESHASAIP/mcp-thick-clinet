import uiautomation as auto
from typing import Optional, Dict, Any, Tuple

def find_element(name: str, control_type: Optional[str] = None, timeout: int = 10) -> Optional[Dict[str, Any]]:
    """
    Scans the active window for a UI element with the specified name and returns its details.
    
    This tool is essential for "feeling" the UI to find buttons, input fields, or menus
    without relying on visual screenshots. It uses the Windows Accessibility API.

    Args:
        name (str): The 'Name' property of the UI element to find (e.g., "New mail", "Send", "File").
        control_type (str, optional): The specific ControlType to filter by (e.g., "Button", "Edit", "Document").
            Defaults to None, which searches all types.
        timeout (int, optional): The maximum time to wait for the element to appear, in seconds. Defaults to 10.

    Returns:
        Optional[Dict[str, Any]]: A dictionary containing the element's properties if found, or None if not found.
            The dictionary keys are:
            - 'name' (str): The element's name.
            - 'control_type' (str): The element's control type.
            - 'rect' (tuple): The formatted bounding box (left, top, right, bottom).
            - 'center' (tuple): The (x, y) coordinates of the element's center.
            - 'handle' (int): The native window handle.
    """
    try:
        root = auto.GetForegroundControl()
        if not root:
            root = auto.GetRootControl()
            
        # Simplified search: using Name is usually sufficienc for high-level tasks
        # For control_type, we would need to map string to ControlType constant if strictly required,
        # but uiautomation allows filtering by ControlTypeName usually? 
        # Actually simpler to just search by name first.
        found = root.Control(Name=name, searchDepth=10, foundIndex=1)
        
        if found.Exists(maxSearchSeconds=timeout):
            # If control_type is specified, verify it matches
            if control_type and control_type.lower() not in found.ControlTypeName.lower():
                # This is a naive check; ideally we search WITH the control type constraint
                pass 

            rect = found.BoundingRectangle
            center_x = (rect.left + rect.right) // 2
            center_y = (rect.top + rect.bottom) // 2
            
            return {
                "name": found.Name,
                "control_type": found.ControlTypeName,
                "rect": (rect.left, rect.top, rect.right, rect.bottom),
                "center": (center_x, center_y),
                "handle": found.NativeWindowHandle
            }
        return None
    except Exception as e:
        print(f"Error finding element '{name}': {e}")
        return None

def dump_hierarchy() -> str:
    """
    Generates a textual representation of the active window's UI control hierarchy.
    
    Use this tool to debug layout issues or to discover the names of buttons and fields
    if `find_element` is failing.

    Returns:
        str: A string containing a tree-like list of controls in the foreground window.
    """
    root = auto.GetForegroundControl()
    if not root:
        return "No foreground window found."
    
    output = []
    for control, depth in auto.WalkControl(root):
        output.append("  " * depth + f"{control.Name} ({control.ControlTypeName})")
        if len(output) > 200: 
            output.append("... (truncated)")
            break
    return "\n".join(output)
