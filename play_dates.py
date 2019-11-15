from datetime import date, timedelta, datetime

today = date.today()
print(today)
print(type(today))
print(today.year)
print(today.month) # in python month is 1 based
print(today.day)

birthday = date(year=1986, month=11, day=25)
print(birthday)
print(type(birthday))

upcoming_birthday = birthday.replace(year=today.year)
print(upcoming_birthday)
print(type(upcoming_birthday))
print(upcoming_birthday.strftime('%d/%m/%Y'))
print(upcoming_birthday.strftime('%d, %B %Y'))

# create a date object which is 1 week from now
one_week_hence = timedelta(weeks=1)
one_week_hence_date = today + one_week_hence
print(one_week_hence_date)
print(type(one_week_hence_date))

# create a date object which is 2 weeks and 15 days from now
d2 = timedelta(weeks=2, days=15)
two_weeks_15_days = today + d2
print(two_weeks_15_days)

# create a date object which is 2 weeks 15 days in the past from now
past = today - d2
print(past)


now = datetime.now()
print(now)
print(type(now))
print(now.day, now.month, now.year, now.hour, now.minute)

d = now.date()
print(d)
t = now.time()
print(t)

# regular relational operators can be applied on the date objects in python
print(today > upcoming_birthday)
print(today > birthday)
print(today == d)