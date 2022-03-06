# How to Find the Current Day is Weekday or Weekends in Python
# Author: Catriona Murray
# Import Module
import datetime

# Get todays day
weekNumber = datetime.datetime.today().weekday()

if weekNumber < 5: #5 days in a weekday
    print("Today's DateTime is {0} and it's a Weekday".format(datetime.datetime.today()))
else: #otherwise its 6th or 7th day in the week its the weekend
    print ("Today's DateTime is {0} and it's a Weekend".format(datetime.datetime.today()))