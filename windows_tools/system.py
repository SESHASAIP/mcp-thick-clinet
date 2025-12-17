import time

def wait(seconds: float) -> None:
    """
    Pauses the agent's execution for a specified duration.
    
    You MUST use this tool after launching apps or clicking buttons that trigger
    animations or network requests (like opening a compose window). It gives the
    UI time to update.

    Args:
        seconds (float): The number of seconds to sleep.
    """
    time.sleep(seconds)
