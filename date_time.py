import datetime
import calendar

d = datetime.date(2019, 5, 15)  # create a date (don't write zero before single digit)
print(d)
# today's date
today = datetime.date.today()
print(today)
print(today.day, today.month, today.year, today.weekday())  # weekday()  : Monday 0  sunday 6

# TimeDelta : find date of seven days from now in future
tdelta = datetime.timedelta(days=7)
print(today + tdelta)  # date2 = date1 + timedelta
# get what day of week it was 7 days ago
print((today - tdelta).weekday())

bday = datetime.date(2019, 9, 11)  # timedelta = date1 - date2
till_bday = bday - today
print(till_bday.days)

t = datetime.time(9, 30, 45)  # hour - minute - second
print(t)

t = datetime.datetime(2019, 5, 18, 14, 51, 30)
print(t)
print(t.date(), "|=====|", t.time())

tdelta = datetime.timedelta(hours=13)
print(t + tdelta)

# this is current time without any timezone
dt_today = datetime.datetime.today()
print(dt_today)
# this is same as dt_today, but we can give it timezones
dt_now = datetime.datetime.now()
print(dt_now)
# current utc time
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow)

# formatting time to custom mode for printing : strftime
print(dt_today.strftime("%B %d %Y"))
# convert string to datetime : strptime
dt_str = "May 18, 2019"
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# dates and time in python : find day from the date
date = "9 18 1997"
month, day, year = date.split(" ")
l = list(calendar.day_name)
print(l[calendar.weekday(int(year), int(month), int(day))].upper())

# weight loss planning via datetime
current_weight = 79
goal_weight = 70
avg_loss_week = 1
start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_loss_week
print(f'reach goal in {(end_date - start_date).days} days')
