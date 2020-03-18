# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Using datasets downloaded from http://archive.ics.uci.edu/ml/datasets/Iris

# Datasets Review

import pandas as pd                         # Import pandas as pd 
import matplotlib.pyplot as plt             # Import matplotliv.pyplot as plt

# Note the given download link contains 3No. files:
# 1) bezdekIris.data - comma separated dataset 1
# 2) iris.data - comma separated dataset 2
# 3) iris.names - text file containing dataset information, note discrepancies between datasets highlighted in text file 

# read both datasets, bezdekIris.data & iris.data.
# insert missing header row for both datasets - sepal_length, sepal_width, petal_length, petal_width, class
 
df_1 = pd.read_csv("datasets/bezdekIris.data", sep=",", names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])
df_2 = pd.read_csv("datasets/iris.data", sep=",", names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# iris.names notes discrepancies for sample 35 & 38
# print & review rows 35 & 38 (index rows 34 to 37)

print(df_1.loc[34:37])
print(df_2.loc[34:37])

# Check all rows & values between datasets for other discrepancies / differences

# use pandas concatuate to combine df_1 & df_2 and drop_duplicates(keep=False) to remove all duplicate rows 

print(pd.concat([df_1,df_2]).drop_duplicates(keep=False))

# bezdekIris.data contains correct ammended sample values.
# use bezdekIris.data in project. 
