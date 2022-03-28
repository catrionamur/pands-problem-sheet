# How to Find the Current Day is Weekday or Weekends in Python
# Author: Catriona Murray
# Import Module datetime
import datetime
# Get todays day
todaysDay = datetime.datetime.today().weekday()
if todaysDay <= 5: #5 days make up a weekday
    print("Yes, unfortunately today is a weekday.")
else: #otherwise its the weekend
    print ("It is the weekend, yay!",end="")  # End line with space an not a new line