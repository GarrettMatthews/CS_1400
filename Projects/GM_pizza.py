Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def Pizza():
    print("This program will tell you how much a pizza costs per square inch")
    p = float(input("What is the total cost of the pizza? $"))
    d = float(input("What is the diameter of the pizza in inches?"))
    r = d / 2
    a = math.pi * (r ** 2)
    sqin = p / a
    print("The pizza costs ${0:.2f}".format(sqin),"per square inch")
