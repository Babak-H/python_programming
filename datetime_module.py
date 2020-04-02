import datetime

# working with date and time in python

d = datetime.date(2019, 5, 12)  # create a date (don't write zero before single digit)
print(d)

today = datetime.date.today() # gives back today's date
print(today)
print(today.day, today.month, today.year, today.weekday())   # weekday()  : Monday 0  sunday 6

# Time Delta
# fimd date of seven days from now in future
tdelta = datetime.timedelta(days=7)
print(today + tdelta)

# get what day of the week was 7 days ago
print((today - tdelta).weekday())

# date2 = date1 + timedelta
# timeDelta = date1 + date2

bday = datetime.date(2019, 9, 11)
till_bday = bday - today
print(till_bday.days)

t = datetime.time(9, 30, 45) # hour, minute, second
print(t)

t = datetime.datetime(2019, 5, 18, 14, 51, 30)
print(t)
print(t.date(), "|====|", t.time())  # 2019-05-18 |=====| 14:51:30
tdelta = datetime.timedelta(hours= 13)
print(t + tdelta)

# ===========================
# current time without any timezone
dt_today = datetime.datetime.today()
print(dt_today)

# same as dt_today but we can give it timezones
dt_now = datetime.datetime.now()
print(dt_now)

# current utc time
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow)

# ===========================
# formatting time to custom mode for printing: strftime

print(dt_today.strftime("%B %d, %Y"))

# convert string to datetime: strptime
dt_str = "May 18, 2019"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)

# =================================
# dates and time in python :

# find day from the date
import calendar

date = "10 4 1996"
month, day, year = date.split(" ")

l = list(calendar.day_name)
print(l[calendar.weekday(int(year), int(month), int(day))].upper())

# =================================

'''
if we get a loan today and we have to start to pay first day of next month, how many months does it take?
and give back the exact date for each payment and its amount based on interest
'''

balance = 5000
interest_rate = 13 * 0.01
monthly_payment = 500

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)
print(days_in_current_month)    # (first day of this month, how many days)

days_till_end_month = days_in_current_month[1] - today.day
print(days_till_end_month)

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
print(start_date)

end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment
    balance = 0 if balance < 0 else round(balance, 2)
    print(end_date, balance)    # next date for payment, how much is left after the pay

    # here we add days left in next month to end_date (first day of that month) so it will give us back the payment
    # date after the upcoming one
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)

# =================================
# weight loss calculator

current_weight = 158
goal_weight = 150
avg_loss_week = 3

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(day=7)
    current_weight -= avg_loss_week

print(f'reach goal in {(end_date - start_date).days // 7} weeks')

# =================================
import re

'''
given a timestamp date "2019-07-01 12:42:33" return string of "19jul1B"
hours: 0-7 A 7-14 B 14-21 C 21-24 D, it should be the shown after start of the hour (7:00:01 accepted)
'''

def DateChecker(timestamp):
    date = re.match(r'(\d{4})\-(\d{2})\-(\d{2}) (\d{2})\:(\d{2})\:(\d{2})', timestamp)
    year = date.group(1)[2:]
    month = int(date.group(2))
    day = int(date.group(3))
    hour = int(date.group(4))
    mint = int(date.group(5))
    sec = int(date.group(6))
    string = ""
    string += year
    string += calendar.month_abbr[month]
    string += str(day)

    if (hour >= 0 and hour < 7) and (mint > 0 or sec > 0):
        string += "A"
    elif (hour >= 7 and hour < 14) and (mint > 0 or sec > 0):
        string += "B"
    elif (hour >= 14 and hour < 24) and (mint > 0 or sec > 0):
        string += "C"

print(DateChecker("2019-07-01 12:00:33"))
