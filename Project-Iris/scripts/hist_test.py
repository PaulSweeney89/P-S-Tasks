# plotting histograms using subplots
import numpy as np
from numpy import arange
import pandas as pd                                                             
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick                                                 

head_row = ["sepal_length", "sepal_width", "petal_length",                     
            "petal_width", "class"]

df = pd.read_csv("../datasets/bezdekIris.data", names=head_row)

n_bins = 7

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True)
fig.suptitle("Histograms of Dataset Variables")

ax1.hist(df["sepal_length"], weights=np.ones(len(df["sepal_length"])) / len(df["sepal_length"]), bins=n_bins, facecolor='blue', ec="black", label="Sepal Length (cm)")
ax1.set(ylabel="Percentage of Samples")

start = min(df["sepal_length"])
end = max(df["sepal_length"])
step = (end - start) / n_bins
ax1.set_xticks(arange(start, (end + step) ,step))

ax1.legend()
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())


ax2.hist(df["sepal_width"], weights=np.ones(len(df["sepal_width"])) / len(df["sepal_width"]), bins=n_bins, facecolor='green', ec="black", label="Sepal Width (cm)") 

start = min(df["sepal_width"])
end = max(df["sepal_width"])
step = (end - start) / n_bins
ax2.set_xticks(arange(start, (end + step) ,step))

ax2.legend()
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())


ax3.hist(df["petal_length"], weights=np.ones(len(df["petal_length"])) / len(df["petal_length"]), bins=n_bins, facecolor='orange', ec="black", label="Petal Length (cm)")
ax3.set(ylabel="Percentage of Samples")

start = min(df["petal_length"])
end = max(df["petal_length"])
step = (end - start) / n_bins
ax3.set_xticks(arange(start, (end + step) ,step))

ax3.legend()
ax3.yaxis.set_major_formatter(mtick.PercentFormatter())

ax4.hist(df["petal_width"], bins=n_bins, weights=np.ones(len(df["petal_width"])) / len(df["petal_width"]), facecolor='red', ec="black", label="Petal Width (cm)")

start = min(df["petal_width"])
end = max(df["petal_width"])
step = (end - start) / n_bins
ax4.set_xticks(arange(start, (end + step) ,step))

ax4.legend()
ax4.yaxis.set_major_formatter(mtick.PercentFormatter(1))

#plt.tight_layout()
plt.show()
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
#plt.show()
#plt.savefig("add_outputs/histogram_by_flower_petal_width")
                                                                            
colour = ['r', 'g', 'b', 'c']                                                   
n = 0                                                                           
n_bins = 7                                                                      
                                                                                  
for n in range(0, 4): 
                                                           
    var = head_row[n]                                                           
    plt.figure(n)                                                               
    plt.hist(df[var], bins=n_bins, facecolor=colour[n], ec="black") 
    
    start = min(df[var])                                                                 
    end = max(df[var])                                                                   
    step = (end - start) / n_bins                                                   
    loc = arange(start, (end + step) ,step)
    plt.xticks(loc)
            
    plt.xlabel(var)                                                             
    plt.ylabel("Sample Freq")                                                 
    plt.title("Histogram of " + var)  
                                                                                                                                        
    n = n + 1
    #plt.show()                                                                                 



