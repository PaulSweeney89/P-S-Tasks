# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Using datasets downloaded from http://archive.ics.uci.edu/ml/datasets/Iris

import numpy as np                                                              # import numpy as np
import pandas as pd                                                             # Import pandas as pd 
import matplotlib.pyplot as plt                                                 # Import matplotliv.pyplot as plt
import matplotlib.ticker as mtick                                               # Import matplotlib.ticker as mtick

head_row = ["Sepal Length", "Sepal Width", "Petal Length",                      # Header row for dataset
            "Petal Width", "Class"]

df = pd.read_csv("datasets/bezdekIris.data", names=head_row)                    # Use pandas to read csv & include header row.
                                                                                # note: dataset bedekIris.data used in Project. 

                                                                               
# Summary of Variables
               
with open('outputs/summary.txt', 'w') as f:                                     # Create a writeable text file named summary.txt
    print("DATASET VARIABLES SUMMARIES:\n\n", df.describe(), file=f)            # Use pandas df.describe() to print summary of each variable to summary text file


sl = df["Sepal Length"]                                                         # assigning each of the dataset's variables or column arrays a name
sw = df["Sepal Width"]                                                          # for ease of reading & writing of code
pl = df["Petal Length"]
pw = df["Petal Width"]


                         
# Histograms of the Dataset Variables
                                                                           
colour = ['r', 'g', 'b', 'c']                                                   # List of colours to be used for plotting different histograms.
n = 0                                                                           # Initialize for loop with n = 0
n_bins = 7                                                                      # setting the number of bins in each histogram = 7
                                                                                  
for n in range(0, 4): 
                                                           
    var = head_row[n]                                                           # For loop to iternate through variables in head_row, 4No. variables (0 to 3)
    plt.figure(n)                                                               # plotting a histogram for each variable, figures(0 - 3)
    plt.hist(df[var], bins=n_bins, facecolor=colour[n], ec="black")             # setting number of bins, applying different colours & a black edge colour to bins

    start = min(df[var])                                                        # the start value of the histogram bins (min value of variable)
    end = max(df[var])                                                          # the end value of the histogram bins (max value of variable)
    step = (end - start) / n_bins                                               # variable values between bins 
    plt.xticks(np.arange(start, (end + step) ,step))                               # applying bin values to the xticks of histogram           
                                                      
    plt.xlabel(var)                                                             # label x-axis (variable name)
    plt.ylabel("Sample Freq")                                                   # label y-axis (sample frequency)
    plt.title("Histogram of " + var)                                            # add titles                                                                             
    plt.savefig(fname="outputs/" + var + " histogram")                          # saving each plot as a individual file in the outputs folder 
    n = n + 1



# Combined Histograms of the Dataset Variables
# all variable histograms plotted on a single figure

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True)                 # using subplots to provide 4no histograms on a single figure (2 rows x 2 columns)
                                                                                # y axis shared between plots (sharey=True)
ax1.hist(sl, weights=np.ones(len(sl)) / len(sl),                                                                  
            bins=n_bins, facecolor='blue', ec="black",                          # axes 1 - Sepal Length (sl), no of bins, colour of plot, edge colour & label. 
            label="Sepal Length (cm)")                                          # weights added to display histogram as percentage.

ax1.set(ylabel="Percentage of Samples")                                         # applying the shared y axis label

start = min(sl)                                                                 # the start value of the histogram bins (min value of variable)
end = max(sl)                                                                   # the end value of the histogram bins (max value of variable)
step = (end - start) / n_bins                                                   # variable values between bins  
ax1.set_xticks(np.arange(start, (end + step) ,step))                            # applying bin values to the xticks of histogram         
ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1))                        # displaying the y-axis values as percentage of samples
ax1.legend()                                          

ax2.hist(sw, weights=np.ones(len(sw)) / len(sw),                                # axes 2 - Sepal Width (sw), no of bins, colour of plot, edge colour & label.
            bins=n_bins, facecolor='green', ec="black",                         # weights added to display histogram as percentage.
            label="Sepal Width (cm)")

start = min(sw)                                                                 # as per axes 1
end = max(sw)                                                                   
step = (end - start) / n_bins                                                   
ax2.set_xticks(np.arange(start, (end + step) ,step))                               
ax2.yaxis.set_major_formatter(mtick.PercentFormatter(1))                         
ax2.legend()

ax3.hist(pl, weights=np.ones(len(pl)) / len(pl),                                # axes 3 - Petal Length (pl), no of bins, colour of plot, edge colour & label.
            bins=n_bins, facecolor='orange', ec="black",                        # weights added to display histogram as percentage.
            label="Petal Length (cm)")

ax3.set(ylabel="Percentage of Samples")

start = min(pl)                                                                 # as per axes 1
end = max(pl)
step = (end - start) / n_bins
ax3.set_xticks(np.arange(start, (end + step) ,step))
ax3.yaxis.set_major_formatter(mtick.PercentFormatter(1))
ax3.legend()

ax4.hist(pw, weights=np.ones(len(pw)) / len(pw),                                # axes 4 - Petal Width (pw), no of bins, colour of plot, edge colour & label.
            bins=n_bins, facecolor='red', ec="black",                           # weights added to display histogram as percentage.
            label="Petal Width (cm)")

start = min(pw)                                                                 # as per axes 1
end = max(pw)
step = (end - start) / n_bins
ax4.set_xticks(np.arange(start, (end + step) ,step))
ax4.yaxis.set_major_formatter(mtick.PercentFormatter(1))
ax4.legend()

plt.tight_layout()                                                              # adjusts subplots so all fit within figure
plt.savefig(fname="outputs/Combined Histograms")                                # save file to outputs folder
                                                                    


# Scatter Plots - Pairs of Variables 
# all pairs of variables on individual subplots plotted
# on a 1 single figure
                                                           
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
        
plt.figure(6)                                                                   # combination of above plots on a single plot or axes
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


