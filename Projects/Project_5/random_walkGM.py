# Garrett Matthews. Random Walk. CS 1400. The problem here is to write a program that takes user input for the number of steps to take, and then randomly moves a graphical
#object (in this case a turtle) that number of steps, generating random angles for each step. Then, the program should display the distance moved, both straight line and actual.

# Import libraries
import math 
import random 
import turtle

# Initial greeting and explanation of the program
print("This program will randomly walk a turtle object a number steps based off of your input. It will then tell you how far the turtle traveled.")

# Asking for user input, and then ensuring that value entered in is an integer
while True:
    try:
        steps = int(input("How many steps should this turtle take?"))
        if steps < 0:
            print("I'm sorry, please only enter a positive number. Please try again")
            continue
    except ValueError:
        print("I'm sorry, that is not a valid input, please try again. Please only use whole numbers.")
        pass
    else:
        break
# Randomly generating an angle    
def random_angle():
    """Randomly generates an angle to be used to later generate positions"""
    angle = random.random() * 2 * math.pi
    return angle
# Generating the x location
def x_local(x, angle):
    """Generate the x location based off an inputted angle"""
    x = x + math.cos(angle)
    return x
# Generating the y location
def y_local(y, angle):
    """Generate the y location based off an inputted angle"""
    y = y + math.sin(angle)
    return y
# Putting these three programs together to generate the values to draw the picture, and calculate the distance traveled by the turtle
def location(x,y,distance):
    """This program generates random location, as well as the distance traveled"""
    angle = random_angle()
    # Saving the initial x and y for accumalating the total distance traveled
    w = x
    z = y
    x = x_local(x,angle)
    y = y_local(y,angle)
    distance = (((w-x) ** 2)+((z-y) ** 2) ** 0.5) + distance
    return x,y, distance

# Now that all the background work is done, we can use the turtle package to draw the random walk of the turtle, and using this calculate the straight line and total distances

def random_walk(steps):
    """This program randomly walks a turtle a number of steps equal to the requested amount inputted by the user"""
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.shape("turtle")
    t.turtlesize(0.5)
    wn.screensize(100,100)
    # Initializing the relevant values to zero
    x = 0
    y = 0
    distance = 0
    # Getting the values for the random walk, as well as the accumulating distance
    for i in range(steps):
        t.setposition(x,y)
        x,y,distance = location(x,y,distance)
    # Finding the straight line distance- as the origin point is 0,0, only the final location is used for the distance formula
    dist_2 = (((x) ** 2) + ((y) ** 2)) ** 0.5
    print("The total distance traveled is {0:.0f}".format(distance),"units, and the straight line distance traveled is {0:.0f}".format(dist_2),"units.")
    

random_walk(steps)

# I gained much more experience using nested functions to make the overall program much more simple and conciese. I also learned more about utilizing accumulator patterns
# across different functions.
# Testing along the way allowed me to successfully complete this project. There were many instances that I wrote the program wrong, generating errors. However, because I was
# doing this one function at a time, ensuring each function did what I needed it to before progressing to the next step. Following the spiral design I also increased my functions
# in complexity until I got the desired result. 



