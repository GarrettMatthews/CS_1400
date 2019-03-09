import math

def trianglearea(a,b,c):
    """Find the area of a triangle by inputing the length of sides a b and c"""
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
a = int(input("What is the length of the first side?"))
b = int(input("What is the length of the second side?"))
c = int(input("What is the length of the third side?"))
area = trianglearea(a,b,c)
print("The area of the triangle is {0:.3f}".format(area))