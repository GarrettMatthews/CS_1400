def name_count():
    name = input("Please enter your name:")
    sum = 0
    for i in name:
        sum = sum + ord(i)
    return sum

print(name_count())

