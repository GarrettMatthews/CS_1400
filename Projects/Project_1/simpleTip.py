Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # Garrett Matthews. The problem here is to create a simple tip calculator that presents three possible tips, based on service, and the total if that tip is paid. The biggest issue I faced in coming up with this solution was how to insure the results were always printed with two decimal place values. The round() function could not accomplish this because it would drop trailing zeroes, resulting in imperfect results. I managed to solve this issue though through use of the format function.
>>> def Tip_Calc():
	tip = float(input("Enter the total amount for the meal: $"))
	print("Cost of the meal: ${0:.2f}".format(tip))
	ex = (.20 * tip)
	av = (.15 * tip)
	po = (.10 * tip)
	print("For excellent service tip ${0:.2f}".format(ex),"for a total amount of ${0:.2f}".format(ex + tip))
	print("For average service tip ${0:.2f}".format(av),"for a total amount of ${0:.2f}".format(av + tip))
	print("For poor service tip ${0:.2f}".format(po),"for a total amount of ${0:.2f}".format(po + tip))

	
>>> # I learned how to use the round() function, and it's limitations, as well as how to use the format function. The key to me understanding the format function was realizing the {0:.2f} needed to be part of a string to work. I also learned the importance of sometimes trying code out a few lines at a time in order to solve issues that may not be readily apparent. As the top comment mentioned, I struggled with coming up with a solution to always have two decimal places printed, as round() was limited in that regard. I also had issues with syntax that were solved by taking the code one step at a time, making sure each part worked before moving on.
