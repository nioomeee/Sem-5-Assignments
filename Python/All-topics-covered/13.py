# All date time operations

from datetime import datetime, timedelta

now = datetime.now()
print(f"Now: {now}")

# 7 days and 7 hours in future
future_date = now + timedelta(days=7, hours=7)
print(f"\n 7 days and 7 hours in future: {future_date}")

past_date = now - timedelta(weeks=2)
print(f"\n 2 weeks ago: {past_date}")

# Coverting string to date ----------------------------------
date_string = "19/11/2025"

date_object = datetime.strptime(date_string, "%d/%m/%Y")

print(f"\n Date string: {date_string}")
print(f"Date object: {date_object}")
print(f"Type: {type(date_object)}")

# Difference between dates --------------------------------------
deadline = datetime(2026, 3, 21)
today = datetime.now()

# Subracting gives timedelta object
time_left = deadline - today
print(f"\n Time left: {time_left}")
print(f"Days left: {time_left.days}")