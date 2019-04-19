import turtle
import random
# Guidance from http://math.hws.edu/TMCM/java/labs/xTurtleLab3.html was followed

def mountain(x,y,c,t):
    """Draws a jagged mountain curve from current starting point to end point x , y. C is complexity, and t is the turtle"""
    if c > 0:
        x1 = (t.xcor() + x) / 2
        y1 = (t.ycor() + y) / 2
        y1 = y1 + (random.random() - 0.5) * (t.xcor() - x)
        t.goto(x1,y1)
        mountain(x,y,c - 1,t)
        

wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
mountain(70,0,150,t)