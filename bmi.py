# bmi.py
# This program calculates BMI inputted by user
# author: Catriona Murray
weight = float(input("Enter Weight(kg):"))
height = float(input("Enter Height (cm):"))

heightm = float(height/100)
bmi = round(weight / (heightm**2),2)

print("The BMI is (kg/m2) " +str(bmi))
if bmi < 18.5:
  print("Your BMI is classed as underweight")
elif bmi < 25:
  print("Your BMI is classed as normal")
elif bmi < 30:
  print("Your BMI is classed as overweight")
else:
  print("Your BMI is classed as obese")