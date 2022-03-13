# bmi.py
# This program calculates BMI inputted by user
# author: Catriona Murray
from pickletools import int4 #Import Library
weight = int(input("Enter Weight(kg):")) # Take in weight as integer
height = int(input("Enter Height (cm):"))  #Take in height as integer
heightm = float(height/100) # Convert tp meters
bmi = round(weight/(heightm**2),2) # calculate BMI and round to rtwo decimal place
print("The BMI is (kg/m2) " +str(bmi) +".") # Output BMI as a strong
if bmi < 18.5: # Output the classification of BMI using of if statement
  print("Your BMI is classed as underweight")
elif bmi < 25:
  print("Your BMI is classed as normal")
elif bmi < 30:
  print("Your BMI is classed as overweight")
else:
  print("Your BMI is classed as obese")