# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Using datasets downloaded from http://archive.ics.uci.edu/ml/datasets/Iris

import pandas as pd                                                             # Import pandas as pd 
import matplotlib.pyplot as plt                                                 # Import matplotliv.pyplot as plt

head_row = ["sepal_length", "sepal_width", "petal_length",                      # Header row for dataset
            "petal_width", "class"]

df = pd.read_csv("datasets/bezdekIris.data", names=head_row)                    # Use pandas to read csv & include header row.
                
with open('outputs/summary.txt', 'w') as f:                                     # Create a writeable text file named summary.txt
    print("DATASET VARIABLES SUMMARIES:\n\n", df.describe(), file=f)            # Use pandas df.describe() to print summary of each variable to summary text file

# Histograms

plt.figure(1)
plt.hist(df["sepal_length"], bins=7, facecolor="blue", ec="black")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sample Freq")
plt.savefig("outputs/sepal_length_histogram")

plt.figure(2)
plt.hist(df["sepal_width"], bins=7, facecolor="green", ec="black")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Sample Freq")
plt.savefig("outputs/sepal_width_histogram")

plt.figure(3)
plt.hist(df["petal_length"], bins=7, facecolor="orange", ec="black")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sample Freq")
plt.savefig("outputs/petal_length_histogram")

plt.figure(4)
plt.hist(df["petal_width"], bins=7, facecolor="red", ec="black")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Sample Freq")
plt.savefig("outputs/petal_width_histogram")

# plotting of histograms
#n_bins = 5

#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#fig.suptitle("Histogram of Variables")

#ax1.hist(df["sepal_length"], bins=n_bins, facecolor='blue', ec="black")
#ax1.set(xlabel="Sepal Length(cm)", ylabel="No. Samples")

#ax2.hist(df["sepal_width"], bins=n_bins, facecolor='green', ec="black")
#ax2.set(xlabel="Sepal Width(cm)")

#ax3.hist(df["petal_length"], bins=n_bins, facecolor='orange', ec="black")
#ax3.set(xlabel="Petal Length(cm)", ylabel="No. Samples")

#ax4.hist(df["petal_width"], bins=n_bins, facecolor='red', ec="black")
#ax4.set(xlabel="Petal Width(cm)")

#plt.tight_layout()
#plt.savefig("histograms.pdf",bbox_inches="tight")


