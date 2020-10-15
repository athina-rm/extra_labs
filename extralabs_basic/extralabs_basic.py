#Write a Python program display a list of the dates for the 2nd Saturday of every month for a
#given year.
from  datetime import datetime

year=int(input("enter the year:"))
for j in range(1,13):
    for i in range (8,15):
        dates =datetime(year,j,i)
        if dates.strftime("%w")=="6":
            print(dates.strftime("%Y-%m-%d"))


