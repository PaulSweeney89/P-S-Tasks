# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Using datasets downloaded from http://archive.ics.uci.edu/ml/datasets/Iris

import pandas as pd                                                             # Import pandas as pd 
import matplotlib.pyplot as plt                                                 # Import matplotliv.pyplot as plt

head_row = ["Sepal Length", "Sepal Width", "Petal Length",                      # Header row for dataset
            "Petal Width", "Class"]

df = pd.read_csv("datasets/bezdekIris.data", names=head_row)                    # Use pandas to read csv & include header row.
                                                                                # note: dataset bedekIris.data used in Project.
# Summary of Variables
               
with open('outputs/summary.txt', 'w') as f:                                     # Create a writeable text file named summary.txt
    print("DATASET VARIABLES SUMMARIES:\n\n", df.describe(), file=f)            # Use pandas df.describe() to print summary of each variable to summary text file

# Histograms of Variables
                                                                           
colour = ['r', 'g', 'b', 'c']                                                   # List of colours to be used for plotting different histograms.
n = 0                                                                           # Initialize for loop with n = 0
                                                                                  
for n in range(0, 4): 
                                                           
    var = head_row[n]                                                           # For loop to iternate through variables in head_row, 4No. variables (0 to 3)
    plt.figure(n)                                                               # plotting a histogram for each variable, figures(0 - 3)
    plt.hist(df[var], bins=7, facecolor=colour[n], ec="black")                  # setting number of bins, applying different colours & a black edge colour to bins
    plt.xlabel(var)                                                             # label x-axis (variable name)
    plt.ylabel("Sample Freq")                                                   # label y-axis (sample frequency)
    plt.title("Histogram of " + var)                                            # add titles                                                                             
    plt.savefig(fname="outputs/" + var + " histogram")                          # saving each individual plots in the outputs folder 
    n = n + 1                                                                   

# Scatter Plots - Pairs of Variables 
# all pairs of variables on individual subplots plotted
# on a 1 single figure

sl = df["Sepal Length"]                                                         # assigning each of the dataset's variables or column arrays a name
sw = df["Sepal Width"]                                                          # for ease of reading & writing of code
pl = df["Petal Length"]
pw = df["Petal Width"]
                                                                                    
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)                    # using subplots to provide 6no. plots on a single figure f (3 rows x 2 columns)
f.suptitle("Scatter Plots - Pairs of Variables")                                # title for figure

ax1.scatter(sl, sw, marker='.', c='b', label="SL v SW")                         # axes 1 - sepal length (SL) vs sepal width (SW), adjusting marker & colour, adding label
ax1.legend(fontsize="x-small", markerscale=2, edgecolor="black")                # legend for axes 1, adjusting textsize, marker scale & legend box colour.

ax2.scatter(sl, pl, marker='.', c='g', label="SL v PL")                         # axes 1 - sepal length (SL) vs petal length (PL)
ax2.legend(fontsize="x-small", markerscale=2, edgecolor="black")                # legend for axes 2

ax3.scatter(sl, pw, marker='.', c='m', label="SL v PW")                         # axes 1 - sepal length (SL) vs petal width (PW)
ax3.legend(fontsize="x-small", markerscale=2, edgecolor="black")                # legend for axes 3

ax4.scatter(sw, pl, marker='.', c='c', label="SW v PL")                         # axes 1 - sepal width (SW) vs petal length (PL)
ax4.legend(fontsize="x-small", markerscale=2, edgecolor="black")                # legend for axes 4

ax5.scatter(sw, pw, marker='.', c='r', label="SW v PW")                         # axes 1 - sepal width (SW) vs petal width (PW)
ax5.legend(fontsize="x-small", markerscale=2, edgecolor="black")                # legend for axes 5

ax6.scatter(pl, pw, marker='.', c='y', label="PL v PW")                         # axes 6 - petal length (PL) vs petal width (PW)
ax6.legend(fontsize="x-small", markerscale=2, edgecolor="black")                # legend for axes 6

plt.savefig(fname="outputs/Scatter Plots - Pairs of Variables")                 # saving plot in the outputs folder 

# Combined Scatter Plots - Pairs of Variables
# all pairs of vaiables combined on a single scatter plot 
        
plt.figure(5)                                                                   # combination of above plots on a single plot or axes
plt.scatter(sl, sw, marker='.', c='b', label="SL v SW") 
plt.scatter(sl, pl, marker='.', c='g', label="SL v PL")
plt.scatter(sl, pw, marker='.', c='m', label="SL v PW")  
plt.scatter(sw, pl, marker='.', c='c', label="SW v PL")
plt.scatter(sw, pw, marker='.', c='r', label="SW v PW") 
plt.scatter(pl, pw, marker='.', c='y', label="PL v PW")
plt.legend(fontsize="x-small", markerscale=2, edgecolor="black")                # adjusting legend properties
plt.title("Combined Scatter Plots - Pairs of Variables")                        # adding title to plot

plt.savefig(fname="outputs/Combined Scatter Plots - Pairs of Variables")        # saving plot in the outputs folder 

plt.show()                                                                      # plot to screen all plots


