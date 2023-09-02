from datetime import datetime

# Define the future date in the format "DD-MMM-YY"
future_date_str = "15-Sep-23"

# Convert the future date string to a datetime object
future_date = datetime.strptime(future_date_str, "%d-%b-%y")

# Get today's date as a datetime object
today_date = datetime.now()

# Calculate the difference in days
days_difference = (future_date - today_date).days

print(f"Number of days between today and {future_date_str}: {days_difference} days")
