Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def Factorial():
	x = int(input("This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:"))
	for i in range(x, end=""):
		ans = i * (i - 1)
		break
	print("And the answer is",ans"!")
	
SyntaxError: invalid syntax
>>> def Factorial():
	x = int(input("This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:"))
	for i in range(x, end=""):
		ans = i * (i - 1)
		break
	print("And the answer is",ans)

	
>>> Factorial()
This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:8
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Factorial()
  File "<pyshell#7>", line 3, in Factorial
    for i in range(x, end=""):
TypeError: range() does not take keyword arguments
>>> def Factorial():
	x = int(input("This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:"))
	for i in [x]:
		ans = i * (i - 1)
		break
	print("And the answer is",ans)

	
>>> Factorial()
This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:8
And the answer is 56
>>> def Factorial():
	x = int(input("This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:"))
	for i in range(x,0):
		ans = i * (i - 1)
		break
	print("And the answer is",ans)

	
>>> Factorial()
This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:8
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Factorial()
  File "<pyshell#13>", line 6, in Factorial
    print("And the answer is",ans)
UnboundLocalError: local variable 'ans' referenced before assignment
>>> def Factorial():
	factorial = 1
	x = int(input("This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:"))
	for i in range(1,x + 1):
		factorial = factorial * i
		break
	print("And the answer is",factorial)

	
>>> Factorial()
This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:8
And the answer is 1
>>> def Factorial():
	factorial = 1
	x = int(input("This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:"))
	for i in range(1,x + 1):
		factorial = factorial * i
	print("And the answer is",factorial)

	
>>> Factorial()
This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:8
And the answer is 40320
>>> Factorial()
This program will help you quickly solve a factorial. Enter the factorial you wish to solve now:16
And the answer is 20922789888000
>>> 
