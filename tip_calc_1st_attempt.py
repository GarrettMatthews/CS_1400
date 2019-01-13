Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def Tip_Calc()
SyntaxError: invalid syntax
>>> def Tip_Calc():
	tip = int(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",tip)
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",Ex,"for a total of $",tip + Ex)
	print("For average service tip $",Av,"for a total of $",tip + Av)
	print("For poor service tip $",Po,"for a total of$",tip + Av)

	
>>> Tip_Calc()
Enter the total amount for the meal: $15.00
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Tip_Calc()
  File "<pyshell#10>", line 2, in Tip_Calc
    tip = int(input("Enter the total amount for the meal: $"))
ValueError: invalid literal for int() with base 10: '15.00'
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",tip)
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",Ex,"for a total of $",tip + Ex)
	print("For average service tip $",Av,"for a total of $",tip + Av)
	print("For poor service tip $",Po,"for a total of$",tip + Av)

	
>>> Tip_Calc()
Enter the total amount for the meal: $15.00
Cost of the meal: $ 15.0
For excellent service tip $ 3.0 for a total of $ 18.0
For average service tip $ 2.25 for a total of $ 17.25
For poor service tip $ 1.5 for a total of$ 17.25
>>> 
