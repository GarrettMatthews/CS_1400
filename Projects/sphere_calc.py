import math

def sphereArea(radius):
    """Find the area of a sphere of radius radius"""
    area = 4 * math.pi * radius ** 2
    return area
def sphereVolume(radius):
    """Find the volume of a sphere of radius radius"""
    volume = (4 / 3) * math.pi * radius ** 3
    return volume
def spherecalc():
    print("This code will find the volume and area of a sphere")
    print("to two decimal places.")
    radius = int(input("What is the radius of the sphere you wish to find the volume and area of?"))
    a = sphereArea(radius)
    v = sphereVolume(radius)
    print("The area is {0:.2f}".format(a) ,"units squared, and the volume is {0:.2f}".format(v),"units cubed")
    
print(spherecalc())