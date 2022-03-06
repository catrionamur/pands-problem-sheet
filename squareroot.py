# squareroot.py
# This program takes in a positive number as a decimal, finds the square root and rounds to 1 decimal place
# It then outputs the number and the square root of the number
# Author: Catriona Murray
import math #  Import library so can use math function to call square root
number = float(input("Enter a positive number:")) # Take in number as float
squrtNum = (round(math.sqrt(abs(number)),1)) # convert number entered to a positive number , calculate square root of that number , then round that number to 1 decimal place
print('The square root of {} is {}'.format(number, squrtNum)) # Print out the number entered and the square root calculated