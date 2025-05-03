from datetime import date, time, datetime

today_date = date.today()
time_right_now = datetime.now()
print("Today's date is,", today_date)
print("The current time right now is", time_right_now)
print(" The components of the date are,", today_date.year",", today_date.month(","), today_date.day)