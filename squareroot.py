# squareroot.py
# This program takes in a positive number as a decimal, finds the square root and rounds to 1 decimal place
# It then outputs the number and the square root of the number
# Author: Catriona Murray
def newton_method(number, number_iters = 100): #Define a function, function has 2 numbers defined as parameter

    a = (float(number)) #Define a variable that stores a number as a float the variable will intially be the number entered by user but later the root number will be set as the value

    for i in range(number_iters): # run a loop until it reaches 100 
        number = 0.5 * (number + a / number) # set the variable number to calculated value of itself plus the user input divided by itself and muliplied by 0.5 - calculates root of user input

    return number # return the root calculation to the function close the function

a=abs(float(input("Enter first number:"))) # Take in an absolute number as float 
aout = newton_method(a) # call the method which will calculate the root of number entered by user
print('The square root of {} is {}'.format(a, round (aout,1)) +".") # Print out the user inputted number and the calculated root number rounded to 1 decimal place