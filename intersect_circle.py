x1 = int(input("Choose the x coordinate for the first circle"))
y1 = int(input("Choose the y coordinate for the first circle"))
x2 = int(input("Choose the x coordinate for the second circle"))
y2 = int(input("Choose the y coordinate for the second circle"))
r1 = int(input("Choose the radius for the first circle"))
r2 = int(input("Choose the radius for the second circle"))

import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.up()
t.goto(x1,y1)
t.right(90)
t.forward(r1)
t.left(90)
t.down()
t.circle(r1)

t.up()
t.goto(x2,y2)
t.right(90)
t.forward(r2)
t.left(90)
t.down()
t.circle(r2)

def circle_intersect(x1,x2,y1,y2,r1,r2):
    distSqr = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    radsumSqr = (r1 + r2) ** 2
    raddifSqr = (r1 - r2) ** 2
    if raddifSqr <= distSqr <= radsumSqr:
        print("The circles intersect")
    else:
        print("The circles do not intersect")
    
        
circle_intersect(x1,x2,y1,y2,r1,r2)