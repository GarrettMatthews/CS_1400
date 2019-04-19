# Guidance from https://gist.github.com/obikag/f12ad029f70c0b21ebe4 was followed

import sys

def pascal(col,row):
    if(col == 0) or (col == row):
        return 1
    else:
        return pascal(col-1,row-1) + pascal(col,row-1)

def triangle(num):
    if (num <= 0):
        print("I'm sorry, please only enter a positive number larger than 0")
    
    for r in range(num):
        for c in range(r+1):
            sys.stdout.write(str(pascal(c,r))+' ')
        sys.stdout.write('\n')
    
number = int(input("How many rows of Pascals Triangle would you like to print?"))

triangle(number)