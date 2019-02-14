x = int(input("What speed were you traveling at?"))
y = int(input("What is the speed limit in that area?"))

if x < y:
    print("That is a legal speed limit")
else:
    if x < 90:
        z = 50 + ( 5 * (x - y))
        print("That is an illegal speed, and the fine is $",z)
    else:
        w = 250 + (5 * (x - y))
        print("That is an illegal speed, and the fine is $",w)