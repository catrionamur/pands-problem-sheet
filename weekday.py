# How to Find the Current Day is Weekday or Weekends in Python
# Author: Catriona Murray
# Import Module datetime
import datetime
# Get todays day
weekNumber = datetime.datetime.today().weekday()
if weekNumber < 5: #5 days in a weekday
    #print("Today's DateTime is {0} and it's a Weekday".format(datetime.datetime.today()))
    print("Yes, unfortunately today is a weekday.")
else: #otherwise its the weekend
    print ("It is the weekend, yay!",end="")