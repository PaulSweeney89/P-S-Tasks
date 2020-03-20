import pandas as pd                                                             
import matplotlib.pyplot as plt                                                 

head_row = ["sepal_length", "sepal_width", "petal_length",                      
            "petal_width", "class"]

df = pd.read_csv("../datasets/bezdekIris.data", names=head_row) 

# scatter plots all variables in different combinations

sl = df["sepal_length"]
sw = df["sepal_width"]
pl = df["petal_length"]
pw = df["petal_width"]
        
plt.figure(1)         
plt.scatter(sl, sw, marker='.', c='b', label="SL v SW") 
plt.scatter(sl, pl, marker='.', c='g', label="SL v PL")
plt.scatter(sl, pw, marker='.', c='m', label="SL v PW")  
plt.scatter(sw, pl, marker='.', c='c', label="SW v PL")
plt.scatter(sw, pw, marker='.', c='r', label="SW v PW") 
plt.scatter(pl, pw, marker='.', c='y', label="PL v PW")
plt.legend(fontsize="x-small", markerscale=2, edgecolor="black")
plt.title("Scatter Plots of Variables") 
                                                                                    
#plt.show()

# dataframes by flower class

seto = df.loc[df["class"] == "Iris-setosa"]
vir = df.loc[df["class"] == "Iris-virginica"]
ver = df.loc[df["class"] == "Iris-versicolor"]

# scatter plots grouped by flower class

plt.figure(2)
plt.scatter(seto["sepal_length"], seto["sepal_width"], marker='o', c='b', alpha=0.3) 
plt.scatter(seto["sepal_length"], seto["petal_length"], marker='o', c='g', alpha=0.3)
plt.scatter(seto["sepal_length"], seto["petal_width"], marker='o', c='r', alpha=0.3)  
plt.scatter(seto["petal_length"], seto["sepal_width"], marker='o', c='y', alpha=0.3)
plt.scatter(seto["petal_length"], seto["petal_width"], marker='o', c='c', alpha=0.3) 
plt.scatter(seto["sepal_width"], seto["petal_width"], marker='o', c='m', alpha=0.3) 

plt.scatter(vir["sepal_length"], vir["sepal_width"], marker='.', c='b') 
plt.scatter(vir["sepal_length"], vir["petal_length"], marker='.', c='g')
plt.scatter(vir["sepal_length"], vir["petal_width"], marker='.', c='r')  
plt.scatter(vir["petal_length"], vir["sepal_width"], marker='.', c='y')
plt.scatter(vir["petal_length"], vir["petal_width"], marker='.', c='c') 
plt.scatter(vir["sepal_width"], vir["petal_width"], marker='.', c='m')

plt.scatter(ver["sepal_length"], ver["sepal_width"], marker='+', c='b', alpha=0.6) 
plt.scatter(ver["sepal_length"], ver["petal_length"], marker='+', c='g', alpha=0.6)
plt.scatter(ver["sepal_length"], ver["petal_width"], marker='+', c='r', alpha=0.6)  
plt.scatter(ver["petal_length"], ver["sepal_width"], marker='+', c='y', alpha=0.6)
plt.scatter(ver["petal_length"], ver["petal_width"], marker='+', c='c', alpha=0.6) 
plt.scatter(ver["sepal_width"], ver["petal_width"], marker='+', c='m', alpha=0.6)

plt.legend

#plt.show()

# scatter plots subplots

f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
f.suptitle("Scatter Plots of Variables")

ax1.scatter(sl, sw, marker='.', c='b', label="SL v SW")
ax1.legend(fontsize="x-small", markerscale=2, edgecolor="black")

ax2.scatter(sl, pl, marker='.', c='g', label="SL v PL")
ax2.legend(fontsize="x-small", markerscale=2, edgecolor="black")

ax3.scatter(sl, pw, marker='.', c='m', label="SL v PW")
ax3.legend(fontsize="x-small", markerscale=2, edgecolor="black")

ax4.scatter(sw, pl, marker='.', c='c', label="SW v PL")
ax4.legend(fontsize="x-small", markerscale=2, edgecolor="black")

ax5.scatter(sw, pw, marker='.', c='r', label="SW v PW")
ax5.legend(fontsize="x-small", markerscale=2, edgecolor="black")

ax6.scatter(pl, pw, marker='.', c='y', label="PL v PW")
ax6.legend(fontsize="x-small", markerscale=2, edgecolor="black")

plt.show()

