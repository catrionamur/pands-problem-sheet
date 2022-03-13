# secondstring.py
# This program takes in a string reverses the string and prints out every second letter in the sentance
# author: Catriona Murray
rawString = input("please enter a string:")
rev = "".join(reversed(rawString)) [::2]# Reverse the string using reversed function and convert it to a string. Printing the string without using th join will print the stting in hex +
 #Use the slice function to go through sentance in 2s
print (rev,end="")
