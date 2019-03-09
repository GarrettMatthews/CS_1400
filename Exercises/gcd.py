m = int(input("Enter the first number you wish to find the GCD for"))
n = int(input("Enter the second number you wish to find the GCD for"))

def gcd(m,n):
    """Find the greatest common denominator of a number m and n"""
    while n:
        m, n = n, m % n
    return m
print("The gcd of",m,"and",n,"is",gcd(m,n))