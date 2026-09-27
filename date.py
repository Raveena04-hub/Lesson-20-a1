from datetime import datetime

def current_date_time():
    """
    Function to display the current date and time.
    """
    # Get current date and time
    now = datetime.now()
    
    # Format output
    print("Current Date:", now.date())
    print("Current Time:", now.strftime("%H:%M:%S"))

# Example usage
current_date_time()
