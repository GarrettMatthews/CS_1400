# Guidance from https://www.sanfoundry.com/python-program-find-gcd-two-numbers-recursively/ was followed

def gcd(a,b):
    if (b == 0) :
        return a
    else:
        return gcd(b, a % b)

print("This program will find the greatest common divisor between two numbers.")
print("When prompted, please enter the two numbers that you wish to be evaluated.")
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

GCD = gcd(a,b)
print("The GCD is",GCD)