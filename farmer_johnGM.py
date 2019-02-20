import turtle
import math

t = turtle.Turtle()

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
def shade(l):
    """Fill in the the area not enclosed by the circles"""
    t.color("black","gray")
    t.right(180)
    t.begin_fill()
    for i in range(4):
        t.circle(l / 2, 90)
        t.right(180)
    t.end_fill()
def area_square(l):
    x = l * l
    return x
def area_circle(l):
    a = math.pi * ((l / 2) ** 2)
    return a
def shaded_area(l):
    area = area_square(l) - area_circle(l)
    return area

def solution(l):
    wn = turtle.Turtle()
    sqrfield(l)
    sprinkler(l)
    shade(l)
    sol = shaded_area(l)
    print("The area not covered by the sprinklers is {0:.2f}".format(sol),"units squared")
    

while True:
    try:
        l = int(input("What is the length of one side of the field?"))
    except ValueError:
        print("I'm sorry, that is not a valid integer, please try again")
        pass
    else:
        break
if l <= 0:
    print("That is not a valid number, I'm sorry")
else:
    solution(l)