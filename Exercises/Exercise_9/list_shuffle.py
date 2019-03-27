# Randomly reorganizing a list
import random

# Just a simple list
myList = [1,2,3,4,5,6]
newlist = []
print("Original List",myList)
def shuffle(mylist):
    """Randomly reorganizes a list"""
    list = mylist[:]
    while True:
        try:
            for i in(mylist):
                value = random.choice(list)
                newlist.append(value)
                list.pop(list.index(value))
        except IndexError:
            pass
        else:
            return newlist
        
x = shuffle(myList)

print("New list",x)