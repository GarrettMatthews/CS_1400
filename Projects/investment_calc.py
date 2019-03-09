Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program calculates the future value")
	print("of an investment after a number of years.")

	
>>> def main():
	print("This program calculates the future value")
	print("of an investment after a number of years.")
	years = int(input("Enter the number of years the investment is for:")

	principal = float(inupt("Enter the initial principal: "))
		    
SyntaxError: invalid syntax
>>> def main():
    print("This program calculates the future value")
    print("of an investment after a number of years.")
    
    years = int(input("Enter the number of years the investment is for: "))
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in",years,"years is: {0:.2f}".format{principal})
    
SyntaxError: invalid syntax
>>> def main():
    print("This program calculates the future value")
    print("of an investment after a number of years.")
    
    years = int(input("Enter the number of years the investment is for: "))
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in",years,"years is: {0:.2f}".format {principal})
    
SyntaxError: invalid syntax
>>> def main():
    print("This program calculates the future value")
    print("of an investment after a number of years.")
    
    years = int(input("Enter the number of years the investment is for: "))
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in",years,"years is: {0:.2f}".format(principal))

    
>>> main()
This program calculates the future value
of an investment after a number of years.
Enter the number of years the investment is for: 7
Enter the initial principal: 23.10
Enter the annualized interest rate: .005
The value in 7 years is: 23.92
>>> 
