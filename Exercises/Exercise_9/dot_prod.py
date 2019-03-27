x = [1,2,3,4,5]
y = [1,2,3,4,5]

def innerProd(x,y):
    """Find the dot product of two lists x and y"""
    return sum( i[0] * i[1] for i in zip(x,y))
z = innerProd(x,y)
print(z)