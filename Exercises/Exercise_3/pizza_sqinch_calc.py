Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def Pizza():
	print("This program will tell you how much a pizza costs per square inch")
	p = int(input("What is the total cost of the pizza? $"))
	d = int(input("What is the diameter of the pizza in inches?"))
	r = d / 2
	a = math.pi * (r ** 2)
	sqin = p / a
	print("The pizza costs ${0:.2f}",.format(sqin),"per square inch. Enjoy your meal!")
	
SyntaxError: invalid syntax
>>> def Pizza():
	print("This program will tell you how much a pizza costs per square inch")
	p = int(input("What is the total cost of the pizza? $"))
	d = int(input("What is the diameter of the pizza in inches?"))
	r = d / 2
	a = math.pi * (r ** 2)
	sqin = p / a
	print("The pizza costs ${0:.2f}".format(sqin)"per square inch. Enjoy your meal!")
	
SyntaxError: invalid syntax
>>> def Pizza():
	print("This program will tell you how much a pizza costs per square inch")
	p = int(input("What is the total cost of the pizza? $"))
	d = int(input("What is the diameter of the pizza in inches?"))
	r = d / 2
	a = math.pi * (r ** 2)
	sqin = p / a
	print("The pizza costs ${0:.2f}".format(sqin),"per square inch. Enjoy your meal!")

	
>>> Pizza()
This program will tell you how much a pizza costs per square inch
What is the total cost of the pizza? $12.72
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Pizza()
  File "<pyshell#10>", line 3, in Pizza
    p = int(input("What is the total cost of the pizza? $"))
ValueError: invalid literal for int() with base 10: '12.72'
>>> def Pizza():
	print("This program will tell you how much a pizza costs per square inch")
	p = float(input("What is the total cost of the pizza? $"))
	d = float(input("What is the diameter of the pizza in inches?"))
	r = d / 2
	a = math.pi * (r ** 2)
	sqin = p / a
	print("The pizza costs ${0:.2f}".format(sqin),"per square inch. Enjoy your meal!")

	
>>> Pizza()
This program will tell you how much a pizza costs per square inch
What is the total cost of the pizza? $12.72
What is the diameter of the pizza in inches?8
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Pizza()
  File "<pyshell#13>", line 6, in Pizza
    a = math.pi * (r ** 2)
NameError: name 'math' is not defined
>>> import math
>>> Pizza()
This program will tell you how much a pizza costs per square inch
What is the total cost of the pizza? $12.72
What is the diameter of the pizza in inches?8
The pizza costs $0.25 per square inch. Enjoy your meal!
>>> Pizza()
This program will tell you how much a pizza costs per square inch
What is the total cost of the pizza? $24.36
What is the diameter of the pizza in inches?23
The pizza costs $0.06 per square inch. Enjoy your meal!
>>> 
