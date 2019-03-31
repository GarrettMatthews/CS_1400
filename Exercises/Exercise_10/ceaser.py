
def caeser():
    shift = int(input("Enter a value between 1 and 26 you would like the phrase shifted:"))
    print("On the following line please enter the name of the file you wish ciphered (Absolute path for anywhere on your machine, relative path if it is stored with your python program):")
    file_name = str(input())
    cipher = ""
    file = open(file_name,'r')
    text = file.readline()
    for line in text:
        o = ord(line)
        new = o + shift
        ltr = str(chr(new))
        cipher += ltr
    return cipher

x = caeser()
print("Your textciphered is",x)