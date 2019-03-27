#Printing the table headers
print("Table of Rabbit Pairs")
print("Month",'\t',"Adult",'\t',"Babies",'\t',"Total")
print("-----------------------------------")
# Setting up the variables I think will be useful here
x = 1
y = 1
w = 0
z = 1
a = 0
#Making the table
for i in range(14):
    print(x,'\t',y,'\t',w,'\t',z)
    #The month increases by one each run
    x = x + 1
    # I need to identify if there are any babies first
    if w > 0:
        #Giving the value of babies to a new variable, and
        #clearing the 'baby' variable
        a = w
        w = 0
    else:
        #This honestly was just a random variable to finish
        #the if/else pathway, and serves no other purpose
        b = 0
    # There is one baby for each pair that has been an adult
    # for one month
    w = y
    #Each baby from last month is added to the total adults
    y = y + a
    # This is just the total of babies and adults
    z = y + w
    
print("Cages will run out in month 14")
