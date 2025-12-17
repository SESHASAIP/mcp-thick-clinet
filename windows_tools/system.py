import time

def wait(seconds: float):
    """
    Pauses execution for the specified number of seconds.
    Crucial for allowing UI animations and app launch times to complete.
    """
    time.sleep(seconds)
