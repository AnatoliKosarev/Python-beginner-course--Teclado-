from datetime import datetime, timezone, timedelta
import time
import calendar

today = datetime.now(timezone.utc)
print(today)

tomorrow = today + timedelta(days=1)
print(tomorrow)

print(today.strftime("%A, %B, %d-%m-%Y, %H:%M:%S, %x, %X, %p"))  # string format time

# user_date = input("Enter the date in YYYY-mm-dd format: ")
# user_date = datetime.strptime(user_date, "%Y-%m-%d")  # string parse time
# print(user_date)

#  timestamp of current time
timestamp_now = datetime.now(timezone.utc).timestamp()
print(timestamp_now)
datetime_now = datetime.utcfromtimestamp(timestamp_now)
print(datetime_now)

#  timestamp of existing time value
datetime_object = "2018-05-21 18:30:00"
time_tuple_utc = time.strptime(datetime_object, "%Y-%m-%d %H:%M:%S")
print(time_tuple_utc)
timestamp_utc = calendar.timegm(time_tuple_utc)
print(timestamp_utc)
datetime_object_returned = datetime.utcfromtimestamp(timestamp_utc)
print(datetime_object_returned)