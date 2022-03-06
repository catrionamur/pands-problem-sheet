# collatz.py
#author: Catriona Murray
# This program takes in an absolute integer, checks if it is even, if it is even it divides number by 2 otherwise it multiplys by 3 and adds 1
def collatz(num): #Define a function that passes variable of type integer
    while num != 1: #Do the below steps as long until it doesnt reach 1
        print(num) #print out the num variable value
        if num % 2 == 0: #If the num variable value is even so divide by 2
            num = int(num / 2)
        else:
            num = int(3 * num + 1)  #Otherwise the num variable value is odd so divide by 2
    else:
        print(num) #if the number variable reaches 1 end while
        print('Number 1 was reached!')


def main():
    n = int(input('Please Input a positive integer enter 1 to exit: ')) # Define a function that takes absolute integer from user and retuns that integer to defined collatz function.
    num =abs(n) # ensure its a positive number
    collatz(num) #close col latz function and pass back absolute value inputted by user for collatz function to process
main() #close main function and pass nothing back 