### Dates ###

from datetime import datetime
now = datetime.now()

def print_date(now):
    print(now)
    print(f"Today is: {now.day}/{now.month}/{now.year}")
    print(now)
    print(now.day)
    print(now.month)
    print(now.year)
    print(now.hour)
    print(now.minute)
    print(now.second)

print_date(now)

timestamp = now.timestamp()
print(timestamp)  # 1625184367.123456

year_2023 = datetime(2023, 1, 1)
print(year_2023)  # 2023-01-01 00:00:00

from datetime import time

current_time = time(21, 6, 0)
print(current_time)  # 21:06:00
print(current_time.hour)  # 21
print(current_time.minute)  # 6
print(current_time.second)  # 0
print(current_time.microsecond)  # 0
print(current_time.tzinfo)  # None

from datetime import date
current_date = date.today()
print(current_date)  # 2023-08-11
print(current_date.year)  # 2023
print(current_date.month)  # 8
print(current_date.day)  # 11


#Operaciones con fechas

from datetime import datetime
now = datetime.now()
print(now)  # 2023-08-11 20:29:24.085716
year_2024 = datetime(2024, 1, 1)
print(year_2024)  # 2024-01-01 00:00:00
time_remaining = year_2024 - now
print(time_remaining)  # 365 days, 0:00:00
print(time_remaining.days)  # 365
print(time_remaining.seconds)  # 31536000
print(time_remaining.total_seconds())  # 31536000.0
print(now.time())  # 20:29:24.085716
print(now.date())  # 2023-08-11
print(now.day)  # 11


from datetime import timedelta
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
print(one_day)  # 1 day, 0:00:00
print(one_week)  # 7 days, 0:00:00

