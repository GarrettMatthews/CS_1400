Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def c2f()
SyntaxError: invalid syntax
>>> def c2f():
	for i in range(0,101,10):
		celsius = i
		fahrenheit = 9/5 * celsius + 32
		print("Temperatures in Celsius:".rjust(2),"Temperatures in Fahrenheit:".rjust(4))
		print("{0:.2f}".format(celsius).rjust(2),"{0:.2f}".format(fahrenheit).rjust(28))

		
>>> c2f()
Temperatures in Celsius: Temperatures in Fahrenheit:
0.00                        32.00
Temperatures in Celsius: Temperatures in Fahrenheit:
10.00                        50.00
Temperatures in Celsius: Temperatures in Fahrenheit:
20.00                        68.00
Temperatures in Celsius: Temperatures in Fahrenheit:
30.00                        86.00
Temperatures in Celsius: Temperatures in Fahrenheit:
40.00                       104.00
Temperatures in Celsius: Temperatures in Fahrenheit:
50.00                       122.00
Temperatures in Celsius: Temperatures in Fahrenheit:
60.00                       140.00
Temperatures in Celsius: Temperatures in Fahrenheit:
70.00                       158.00
Temperatures in Celsius: Temperatures in Fahrenheit:
80.00                       176.00
Temperatures in Celsius: Temperatures in Fahrenheit:
90.00                       194.00
Temperatures in Celsius: Temperatures in Fahrenheit:
100.00                       212.00
>>> 
