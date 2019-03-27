# Garrett Matthews 
# Project 3 - Farmer John's Field
# Importing the necessary libraires
import turtle
import math

t = turtle.Turtle()
# Drawing the square
def sqrfield(l):
    """Make a square of length l"""
    for i in("A","B","C"):
        t.write(i)
        t.forward(l)
        t.right(90)
    for i in ("D"):
        t.write(i, align = "right")
        t.forward(l)
        t.right(90)
# Drawing the four sprinklers    
def sprinkler(l):
    """Draw a circle of radius l"""
    t.right(90)
    t.forward(l / 2)
    t.right(-90)
    t.circle(l / 2)
    t.circle(- l / 2)
    t.left(90)
    t.forward(l / 2)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l / 2)
    t.right(-90)
    t.circle(l / 2)
    t.circle(- l / 2)
# Filling in the region not covered by the sprinklers
def shade(l):
    """Fill in the the area not enclosed by the circles"""
    t.color("black","gray")
    t.right(180)
    t.begin_fill()
    for i in range(4):
        t.circle(l / 2, 90)
        t.right(180)
    t.end_fill()
# Calculating the area of the square
def area_square(l):
    """Find the area of a squareof length l"""
    x = l * l
    return x
# Calculating the area of one of the sprinklers (circle)
def area_circle(l):
    """Find the area of a radius l /2"""
    a = math.pi * ((l / 2) ** 2)
    return a
# The shaded area in the center of the square is the same
# amount of area that would have been left had a single circle
# been in the middle of the square, so the area left over is
# equal to the area of the square minus the area of the circle
def shaded_area(l):
    """Find the area not covered by the sprinklers"""
    area = area_square(l) - area_circle(l)
    return area
# Putting everything together for the drawing and the
# mathmatical solution
def solution(l):
    """Putting everything together, and printing the answer"""
    wn = turtle.Turtle()
    sqrfield(l)
    sprinkler(l)
    shade(l)
    sol = shaded_area(l)
    print("The area not covered by the sprinklers is {0:.2f}".format(sol),"units squared")
    
#Ensuring that value entered in is an integer
while True:
    try:
        l = int(input("What is the length of one side of the field?"))
    except ValueError:
        print("I'm sorry, that is not a valid integer, please try again")
        pass
    else:
        break
# Ensuring the length of a side of the field is a valid input -
# Meaning that is larger than 0
if l <= 0:
    print("That is not a valid number, I'm sorry")
else:
    solution(l)
