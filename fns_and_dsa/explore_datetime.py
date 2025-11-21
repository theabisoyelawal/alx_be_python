from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

def calculate_future_date(days_to_add):
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date

if __name__ == "__main__":
    print("Current date and time:", display_current_datetime())
    days = int(input("Enter the number of days to add to the current date: "))
    print("Future date:", calculate_future_date(days))
