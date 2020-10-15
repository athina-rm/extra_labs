#1. Write a Python program to get the dates 30 days before and after from the current date.

from datetime import datetime,timedelta

today=datetime.now()
after=today+timedelta(30)
before=today-timedelta(30)
print (after.strftime("%Y-%m-%d"))
print (before.strftime("%Y-%m-%d"))