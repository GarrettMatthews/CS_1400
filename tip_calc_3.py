def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: $",round(tip,2))
	Ex = ( .20 * tip )
	Av = ( .15 * tip )
	Po = ( .10 * tip )
	print("For excellent service tip $",round(Ex,2),"for a total of $",round(tip + Ex,2))
	print("For average service tip $",round(Av,2),"for a total of $",round(tip + Av,2))
	print("For poor service tip $",round(Po,2),"for a total of$",round(tip + Po,2))

	
