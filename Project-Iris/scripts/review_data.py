# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Using datasets downloaded from http://archive.ics.uci.edu/ml/datasets/Iris

# Datasets Review Script

import pandas as pd                         # Import pandas as pd 

# use pandas to read both datasets (csv's), bezdekIris.data & iris.data.

head_row = ["sepal_length", "sepal_width", "petal_length",                      # header row for datasets
            "petal_width", "class"]

df_1 = pd.read_csv("datasets/bezdekIris.data", names=head_row)                  # use pandas to read csv & include header rows
df_2 = pd.read_csv("datasets/iris.data", names=head_row)

# iris.names notes discrepancies for sample 35 & 38
# print & review rows 35 & 38 (index rows 34 to 37)

print(df_1.loc[34:37])                      # pandas loc function to print rows 34 to 37 including all columns
print(df_2.loc[34:37])

# Check all rows & values between datasets for other discrepancies / differences

# use pandas concatuate to combine df_1 & df_2 and drop_duplicates(keep=False) to remove all duplicate rows 

print(pd.concat([df_1,df_2]).drop_duplicates(keep=False))

# bezdekIris.data contains correct ammended sample values.
# use bezdekIris.data in project. 
