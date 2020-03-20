# plotting histograms using subplots

import pandas as pd                                                             
import matplotlib.pyplot as plt                                                 

head_row = ["sepal_length", "sepal_width", "petal_length",                     
            "petal_width", "class"]

df = pd.read_csv("../datasets/bezdekIris.data", names=head_row)

n_bins = 7

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle("Histogram of Variables")

ax1.hist(df["sepal_length"], bins=n_bins, facecolor='blue', ec="black")
ax1.set(xlabel="Sepal Length(cm)", ylabel="No. Samples")

ax2.hist(df["sepal_width"], bins=n_bins, facecolor='green', ec="black")
ax2.set(xlabel="Sepal Width(cm)")

ax3.hist(df["petal_length"], bins=n_bins, facecolor='orange', ec="black")
ax3.set(xlabel="Petal Length(cm)", ylabel="No. Samples")

ax4.hist(df["petal_width"], bins=n_bins, facecolor='red', ec="black")
ax4.set(xlabel="Petal Width(cm)")

plt.tight_layout()
#plt.show()
#plt.savefig("add_outputs/histograms_combined",bbox_inches="tight")

# dataframes by flower class

seto = df.loc[df["class"] == "Iris-setosa"]
vir = df.loc[df["class"] == "Iris-virginica"]
ver = df.loc[df["class"] == "Iris-versicolor"]

# histograms sepal length

plt.figure(2)
plt.hist(seto["sepal_length"], bins=7, facecolor='b', ec="black", alpha=0.3, label="Setosa")
plt.hist(vir["sepal_length"], bins=7, facecolor='g', ec="black", alpha=0.3, label="Virginica")
plt.hist(ver["sepal_length"], bins=7, facecolor='r', ec="black", alpha=0.3, label="Versicolor")
plt.xlabel("Sepal Length")
plt.legend(prop={'size': 10})
#plt.show()
#plt.savefig("add_outputs/histogram_by_flower_sepal_length")

# histograms sepal width

plt.figure(3)
plt.hist(seto["sepal_width"], bins=7, facecolor='b', ec="black", alpha=0.3, label="Setosa")
plt.hist(vir["sepal_width"], bins=7, facecolor='g', ec="black", alpha=0.3, label="Virginica")
plt.hist(ver["sepal_width"], bins=7, facecolor='r', ec="black", alpha=0.3, label="Versicolor")
plt.xlabel("Sepal Width")
plt.legend(prop={'size': 10})
#plt.show()
#plt.savefig("add_outputs/histogram_by_flower_sepal_width")

# histograms petal length

plt.figure(4)
plt.hist(seto["petal_length"], bins=7, facecolor='b', ec="black", alpha=0.3, label="Setosa")
plt.hist(vir["petal_length"], bins=7, facecolor='g', ec="black", alpha=0.3, label="Virginica")
plt.hist(ver["petal_length"], bins=7, facecolor='r', ec="black", alpha=0.3, label="Versicolor")
plt.xlabel("Petal Length")
plt.legend(prop={'size': 10})
#plt.show()
#plt.savefig("add_outputs/histogram_by_flower_petal_length")

# histograms petal width

plt.figure(5)
plt.hist(seto["petal_width"], bins=7, facecolor='b', ec="black", alpha=0.3, label="Setosa")
plt.hist(vir["petal_width"], bins=7, facecolor='g', ec="black", alpha=0.3, label="Virginica")
plt.hist(ver["petal_width"], bins=7, facecolor='r', ec="black", alpha=0.3, label="Versicolor")
plt.xlabel("Petal Width")
plt.legend(prop={'size': 10})
plt.show()
#plt.savefig("add_outputs/histogram_by_flower_petal_width")

colour = ['r', 'g', 'b', 'c']                                                   
n = 0                                                                           
var = head_row[n]  
                                                                                 
for n in range(0, 4):                                                            
                                                                                
    plt.figure(n)                                                               
    plt.hist(df[var], bins=7, facecolor=colour[n], ec="black")                  
    plt.xlabel(var)                                                             
    plt.ylabel("Sample Freq")                                                   
    plt.title("Histogram of " + var)                                                                                                                         
    plt.savefig(fname="outputs/" + var + " histogram")                           
    n = n + 1   
