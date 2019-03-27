def name_count():
    name = input("Please enter your name:").lower()
    sum = 0
    for i in name:
        if i.isalpha():
            sum = sum + (ord(i) - 96)
    return sum
        
print(name_count())
