# bmi.py
# This program calculates BMI which is calculated from user input
# author: Catriona Murray
from pickletools import int4 #Import Library
weight = abs(int(input("Enter Weight(kg):"))) # Take in weight as positive integer
height = abs(int(input("Enter Height (cm):")))  #Take in height as positive integer
heightm = float(height/100) # Convert to meters
bmi = float(round((weight/(heightm**2)),2) )# calculate BMI and round to two decimal place
print("The BMI is (kg/m2) " +str(bmi) +".") # Convert Output BMI as a string
if bmi<18.5: print("Your BMI is classed as underweight",end=' ') #output classification of BMI
elif bmi>=18.5 and bmi<25: print("Your BMI is classed as normal",end=' ')
elif bmi>=25 and bmi<30: print("Your BMI is classed as overweight",end=' ') 
else: print("Your BMI is classed as obese",end=' ') #end='' prevent print out of new lines