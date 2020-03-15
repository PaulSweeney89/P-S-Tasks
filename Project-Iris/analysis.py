#Project - Fischer's Iris Data Set
#Programming & Scripting Project 2020

import pandas as pd 
import matplotlib.pyplot as plth

df = pd.read_csv("iris.csv")

print(df['sepal_length'].describe())
print(df)


