import pandas

df = pandas.read_csv("/home/garrett/Desktop/Git_Repositories/Python_Practice/Exercises/Exercise_11/world-cities-population.csv")

cent = dict([(i,[a]) for i, a, in zip(df['Country or Area'],df['City'])])

cent_am = ["Belize","Costa Rica","El Salvador","Guatemala","Honduras","Nicaragua","Panama"]

city_cent_am = list()

for i in cent_am:
    city_cent_am.append(cent.get(i,("No cities listed from {0:}".format(i))))
    
    
print(city_cent_am)