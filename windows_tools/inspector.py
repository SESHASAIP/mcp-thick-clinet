import uiautomation as auto
from typing import Optional, Tuple, Dict, Any

def find_element(name: str, control_type: str = None, timeout: int = 10) -> Optional[Dict[str, Any]]:
    """
    Scans the active window (or works globally if needed) for a UI element.
    Returns a dictionary with element properties including coordinates, or None.
    
    Args:
        name: The 'Name' property of the UI element (e.g., "New mail").
        control_type: Optional 'ControlType' (e.g., "Button", "Edit").
        timeout: How long to wait for element to appear.
    """
    # Create a search criteria
    # This is a simplified wrapper. Real usage might need more complex search.
    try:
        # Search in the foreground window first
        root = auto.GetForegroundControl()
        if not root:
            root = auto.GetRootControl()
            
        # Basic search (breadth-first or depth-first is handled by walk/GetFirstChild)
        # using the powerful Control search of uiautomation
        found = root.Control(Name=name, searchDepth=10, foundIndex=1)
        
        if found.Exists(maxSearchSeconds=timeout):
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

def dump_hierarchy():
    """Returns a simplified tree of the active window's controls."""
    root = auto.GetForegroundControl()
    if not root:
        return "No foreground window found."
    
    # Simple recursive dump or flattened list could be implemented here
    # For now, let's just use the Log functionality or simple walk
    output = []
    for control, depth in auto.WalkControl(root):
        output.append("  " * depth + f"{control.Name} ({control.ControlTypeName})")
        if len(output) > 200: # Limit output
            output.append("... (truncated)")
            break
    return "\n".join(output)
