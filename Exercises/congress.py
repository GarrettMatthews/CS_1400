x = int(input("What is your age?"))
y = int(input("How long have you been a U.S. citizen?"))

if x >= 30:
    if y >= 9:
        print("You are elligible to become a US senator")
    else:
        z = 9 - y
        print("You are",z,"years away from being elligible to become a senator")
elif x >= 25:
    if y >= 7:
        print("You are elligible to become a member of the House of Representatives")
    else:
        w = 7 - y
        print("You are",w,"years away from becoming elligible for the House.")
else:
    print("You are not yet elligible for the house or the senate")