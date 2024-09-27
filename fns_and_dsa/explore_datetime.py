from datetime import datetime

def display_current_datetime():
    current_date =datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

display_current_datetime()

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    now = datetime.datetime.now()
    future_date = now + datetime.timedelta(days=days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()                      