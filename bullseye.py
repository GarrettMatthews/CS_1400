Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def bullseye():
	import turtle
	wn = turtle.Screen()
	wn.bgcolor("lightgray")
	t = turtle.Turtle()
	t.color('black','white')
	t.hideturtle()
	t.begin_fill()
	t.circle(50)
	t.end_fill()
	t.up()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.color('black','black')
	t.down()
	t.begin_fill()
	t.circle(40)
	t.end_fill()
	t.up()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.color('blue','blue')
	t.down()
	t.begin_fill()
	t.circle(30)
	t.up()
	t.end_fill()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.color('red','red')
	t.down()
	t.begin_fill()
	t.circle(20)
	t.up()
	t.end_fill()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.color('yellow','yellow')
	t.down()
	t.begin_fill()
	t.circle(10)
	t.up()
	t.end_fill()

>>> bullseye()
>>> 
