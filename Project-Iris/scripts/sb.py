# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Script for plotting & testing scatterplots using seaborn library


import pandas as pd          
import seaborn as sns                                                   
import matplotlib.pyplot as plt                                                 

head_row = ["sepal_length", "sepal_width", "petal_length",                      
            "petal_width", "class"]

df = pd.read_csv("../datasets/bezdekIris.data", names=head_row) 

# 3 No. scatterplots plotted with regression lines 

plt.figure(1)
plt.title("Petal Length vs Petal Width")
ax1 = sns.scatterplot(x="petal_length", y="petal_width", data=df, hue = 'class')                        # seaborn scatterplot 
ax1 = sns.regplot(x='petal_length', y='petal_width', data=df, scatter=False, color="red")               # seaborn regression plot, showing regression line only
ax1.set(xlabel="", ylabel = "")                                                                         # labels left blank
plt.savefig("add_outputs/Seaborn_Scatter_PLvPW")                                                        # plots saved to add_outputs folder

plt.figure(2)
plt.title("Sepal Length vs Petal Length")
ax2 = sns.scatterplot(x="sepal_length", y="petal_length", data=df, hue = 'class')
ax2 = sns.regplot(x='sepal_length', y='petal_length', data=df, scatter=False, color="red")
ax2.set(xlabel="", ylabel = "")
plt.savefig("add_outputs/Seaborn_Scatter_SLvPL")

plt.figure(3)
plt.title("Sepal Length vs Petal Width")
ax3 = sns.scatterplot(x="sepal_length", y="petal_width", data=df, hue = 'class')
ax3 = sns.regplot(x='sepal_length', y='petal_width', data=df, scatter=False, color="red")
ax3.set(xlabel="", ylabel = "")
plt.savefig("add_outputs/Seaborn_Scatter_SLvPW")

plt.show()

