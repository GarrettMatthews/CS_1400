Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def Factorial():
	factorial = 1
	x = int(input("This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:"))
	for i in range(1,x + 1):
		factorial = factorial * i
	print("And the answer is",factorial)
