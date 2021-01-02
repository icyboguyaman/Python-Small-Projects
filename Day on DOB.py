import datetime
import calendar

def birthday(date):
    borndate = datetime.datetime.strptime(date, '%d/%m/%Y')
    day = borndate.weekday()
    return(calendar.day_name[day])
date = input("Enter the DOB (day/month/year):")
print(birthday(date))
