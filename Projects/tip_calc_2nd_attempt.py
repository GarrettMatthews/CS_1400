Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip[,2digits]))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex[,2digits]),"for a total of $",tip + Ex)
	print("For average service tip $",round(Av[,2digits]),"for a total of $",tip + Av)
	print("For poor service tip $",round(Po[,2digits]),"for a total of$",tip + Av)
	
SyntaxError: invalid syntax
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip[2digits]))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex[2digits]),"for a total of $",tip + Ex)
	print("For average service tip $",round(Av[2digits]),"for a total of $",tip + Av)
	print("For poor service tip $",round(Po[2digits]),"for a total of$",tip + Av)
	
SyntaxError: invalid syntax
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip[2 digits]))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex[2 digits]),"for a total of $",tip + Ex)
	print("For average service tip $",round(Av[2 digits]),"for a total of $",tip + Av)
	print("For poor service tip $",round(Po[2 digits]),"for a total of$",tip + Av)
	
SyntaxError: invalid syntax
>>> round(12.4939329[, 2digits])
SyntaxError: invalid syntax
>>> round(12.4939292[ 2digits])
SyntaxError: invalid syntax
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip[2]))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex[2]),"for a total of $",tip + Ex)
	print("For average service tip $",round(Av[2]),"for a total of $",tip + Av)
	print("For poor service tip $",round(Po[2]),"for a total of$",tip + Av)

	
>>> Tip_Calc()
Enter the total amount for the meal: $12.57
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Tip_Calc()
  File "<pyshell#6>", line 3, in Tip_Calc
    print("Cost of the meal: $",round(tip[2]))
TypeError: 'float' object is not subscriptable
>>> Tip_Calc()
Enter the total amount for the meal: $15.00
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Tip_Calc()
  File "<pyshell#6>", line 3, in Tip_Calc
    print("Cost of the meal: $",round(tip[2]))
TypeError: 'float' object is not subscriptable
>>> def Tip_Calc():
	tip = int(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip[2 digits]))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex[2 digits]),"for a total of $",tip + Ex)
	print("For average service tip $",round(Av[2 digits]),"for a total of $",tip + Av)
	print("For poor service tip $",round(Po[2 digits]),"for a total of$",tip + Av)
	
SyntaxError: invalid syntax
>>> def Tip_Calc():
	tip = int(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip[2]))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex[2]),"for a total of $",tip + Ex)
	print("For average service tip $",round(Av[2]),"for a total of $",tip + Av)
	print("For poor service tip $",round(Po[2]),"for a total of$",tip + Av)

>>> Tip_Calc()
Enter the total amount for the meal: $15.00
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Tip_Calc()
  File "<pyshell#10>", line 2, in Tip_Calc
    tip = int(input("Enter the total amount for the meal: $"))
ValueError: invalid literal for int() with base 10: '15.00'
>>> Tip_Calc()
Enter the total amount for the meal: $10
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Tip_Calc()
  File "<pyshell#10>", line 3, in Tip_Calc
    print("Cost of the meal: $",round(tip[2]))
TypeError: 'int' object is not subscriptable
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round( tip [2]))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round( Ex [2]),"for a total of $",tip + Ex)
	print("For average service tip $",round( Av [2]),"for a total of $",tip + Av)
	print("For poor service tip $",round( Po [2]),"for a total of$",tip + Av)

>>> Tip_Calc()
Enter the total amount for the meal: $15.00
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Tip_Calc()
  File "<pyshell#13>", line 3, in Tip_Calc
    print("Cost of the meal: $",round( tip [2]))
TypeError: 'float' object is not subscriptable
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip,2))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex,2),"for a total of $",tip + Ex)
	print("For average service tip $",round(Av,2),"for a total of $",tip + Av)
	print("For poor service tip $",round(Po,2),"for a total of$",tip + Av)

>>> Tip_Calc()
Enter the total amount for the meal: $15.00
Cost of the meal: $ 15.0
For excellent service tip $ 3.0 for a total of $ 18.0
For average service tip $ 2.25 for a total of $ 17.25
For poor service tip $ 1.5 for a total of$ 17.25
>>> Tip_Calc
<function Tip_Calc at 0x751c5c90>
>>> Tip_Calc()
Enter the total amount for the meal: $15.87
Cost of the meal: $ 15.87
For excellent service tip $ 3.17 for a total of $ 19.044
For average service tip $ 2.38 for a total of $ 18.2505
For poor service tip $ 1.59 for a total of$ 18.2505
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip,2))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex,2),"for a total of $",round(tip + Ex,2))
	print("For average service tip $",round(Av,2),"for a total of $",round(tip + Av,2))
	print("For poor service tip $",round(Po,2),"for a total of$",round(tip + Av,2))

	
>>> Tip_Calc()
Enter the total amount for the meal: $15.87
Cost of the meal: $ 15.87
For excellent service tip $ 3.17 for a total of $ 19.04
For average service tip $ 2.38 for a total of $ 18.25
For poor service tip $ 1.59 for a total of$ 18.25
>>> Tip_Calc()
Enter the total amount for the meal: $16.00
Cost of the meal: $ 16.0
For excellent service tip $ 3.2 for a total of $ 19.2
For average service tip $ 2.4 for a total of $ 18.4
For poor service tip $ 1.6 for a total of$ 18.4
>>> 
