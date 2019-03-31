# Importing libraries
import pandas
# Reading the data in
df = pandas.read_csv("/home/garrett/Desktop/Git_Repositories/Python_Practice/Exercises/Exercise_10/station.csv", delimiter = ',')
#Checking to see if the data is numeric or character
print(df["DrainageAreaMeasure/MeasureValue"].head())
# Filtering the data
drain = (df["DrainageAreaMeasure/MeasureValue"] > 0)
df1 = df[drain]
# Checking if the filter worked
print(df1["DrainageAreaMeasure/MeasureValue"].head())
# Writing to CSV
df1.to_csv("/home/garrett/Desktop/Git_Repositories/Python_Practice/Exercises/Exercise_10/stations-filtered.csv")