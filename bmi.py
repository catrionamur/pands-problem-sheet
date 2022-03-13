# bmi.py
# This program calculates BMI which is calculated from user input
# author: Catriona Murray
from pickletools import int4 #Import Library
weight = int(input("Enter Weight(kg):")) # Take in weight as integer
height = int(input("Enter Height (cm):"))  #Take in height as integer
heightm = float(height/100) # Convert to meters
bmi = round((weight/(heightm**2)),2) # calculate BMI and round to two decimal place
print("The BMI is (kg/m2) " +str(bmi) +".") # Output BMI as a string
if bmi < 18.5: print("Your BMI is classed as underweight",end=' ') #output classification of BMI without printing blank line
elif bmi < 25: print("Your BMI is classed as normal",end=' ')
elif bmi < 30: print("Your BMI is classed as overweight",end=' ')
else: print("Your BMI is classed as obese",end=' ')