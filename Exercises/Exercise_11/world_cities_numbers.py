import pandas

df = pandas.read_csv("/home/garrett/Desktop/Git_Repositories/Python_Practice/Exercises/Exercise_11/world-cities-population.csv")

numb = list()

for x in df['Value']:
    try:
        numb.append(int(x))
    except ValueError:
        numb.append("Not a number")

city = dict([(i,[a,b]) for i, a,b in zip(df['City'],df['Country or Area'],numb)])


z = city.get("Zürich","City not found")
os = city.get("Osorno","City not found")
ly = city.get("Lysychansk", "City not found")

print("Zürich",z, "Osorno", os,"Lysychansk", ly)
