# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Using datasets downloaded from http://archive.ics.uci.edu/ml/datasets/Iris

# Datasets Review Script
# Script to review the datasets involved in the Fischer's Iris Data Set

import pandas as pd                                                                 # Import pandas as pd 
import datetime                                                                     # Import datetime

# use pandas to read both datasets (csv's), bezdekIris.data & iris.data.

head_row = ["sepal_length", "sepal_width", "petal_length",                          # header row for datasets
            "petal_width", "class"]

df_1 = pd.read_csv("../datasets/bezdekIris.data", names=head_row)                   # use pandas to read csv & include header rows
df_2 = pd.read_csv("../datasets/iris.data", names=head_row)

f = open("add_outputs/review_output.txt", "w+")

print("***REVIEW OF DATASETS***", file=f)                                           # print title to output file
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=f)                # printing datestamp to output file
print("\n", file=f)

# print info for df_1 & df_2
print("dataset 1 (bezdekIris.data) info output:", file=f)
df_1.info(buf=f)
print("\n", file=f)                                                                 # provide blank line between outputs for ease of review
print("dataset 2 (iris.data) info output:", file=f)                                                                 
df_2.info(buf=f)
print("\n", file=f)

# check for any null or missing values within datasets
print("dataset 1 - missing values", file=f)
print(df_1.isnull().sum(), file=f)                                                  # print sum of all null values within the datasets
print("\n", file=f)                                                                 # to detemine if values missing within set
print("dataset 2 - missing values", file=f)
print(df_2.isnull().sum(), file=f)
print("\n", file=f)

# iris.names notes discrepancies for sample 35 & 38
# print & review rows 35 & 38 (index rows 34 to 37)
print("dataset 1 - rows 35 to 38", file=f)
print(df_1.loc[34:37], file=f)                                                      # pandas loc function to print rows 34 to 37 including all columns
print("\n", file=f)
print("dataset 2- rows 35 to 38", file=f)
print(df_2.loc[34:37], file=f)
print("\n", file=f)

# Check all rows & values between datasets for other discrepancies / differences
# use pandas concatuate to combine df_1 & df_2 and drop_duplicates(keep=False) to remove all duplicate rows 
# leaving ony rows with differences 
print("rows with discrepancies between datasets:", file=f)
print(pd.concat([df_1,df_2]).drop_duplicates(keep=False), file=f)

f.close()

# bezdekIris.data contains correct ammended sample values.
# use bezdekIris.data in project. 
