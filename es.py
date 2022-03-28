# plottask.py
# This program reads in a text file which is passed as an argument from a user and calculates number of e's
# Author: Catriona Murray

import sys # Import library
fileName = sys.argv[1] # Use function from predefined sys lbrary which expects return of one parameter and store in variable filename
inputFile = open(fileName, "r")  # open file in read mode
def letterFrequency (fileName, letter): #define function that has 2 arguments, name of the file and the letter that is being checked 
    # store content of the file in a variable for processing
    text = inputFile.read()
    # declare count variable used in the for loop
    count = 0
    # iterate through each character in the text filer
    for char in text: 
        # compare each character with the given letter
        if char == letter:
            count += 1 # If the letter is found iterate count by 1
    # return letter count 
    return count
    # call function passing back the letter we are checking for and display the letter count
print(letterFrequency('inputFile', 'e'),end="")