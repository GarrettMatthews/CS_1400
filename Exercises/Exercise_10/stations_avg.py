import pandas as pd
import numpy as np

df = pd.read_csv("/home/garrett/Desktop/Git_Repositories/Python_Practice/Exercises/Exercise_10/stations-filtered.csv", delimiter = ',')

avg = (df["DrainageAreaMeasure/MeasureValue"].mean())

out = open("/home/garrett/Desktop/Git_Repositories/Python_Practice/Exercises/Exercise_10/drainage-area-avg.txt", "w")
out.write(str(avg))
out.close()