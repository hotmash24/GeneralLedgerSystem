from datetime import datetime
from calendar import monthrange

# Get the current date without time
today = datetime.now().date()

# Get the first day of the current month
first_day_of_month = today.replace(day=1)

# Get the last day of the current month
last_day_of_month = today.replace(day=monthrange(today.year, today.month)[1])

# Print start_date and end_date
print(first_day_of_month)
print(last_day_of_month)
