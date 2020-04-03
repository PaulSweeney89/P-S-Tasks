# Project - Fischer's Iris Data Set
# Programming & Scripting Project 2020
# Script for plotting & testing various scatterplots

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
plt.close()

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
plt.close()

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
plt.close()


# scatter plots grouped by flower class
plt.figure(4)

seto_1 = plt.scatter(seto["petal_length"], seto["petal_width"], marker='o', c='b') 

vir_1 = plt.scatter(vir["petal_length"], vir["petal_width"], marker='o', c='g') 

ver_1 = plt.scatter(ver["petal_length"], ver["petal_width"], marker='o', c='r') 

plt.legend((seto_1, vir_1, ver_1),("Iris Setosa", "Iris Virginica", "Iris Versicolor"))
plt.title("Petal Length vs Petal Width")
#plt.savefig("add_outputs/Scatter_PLvPW")
#plt.show()
plt.close()

plt.figure(5)

seto_2 = plt.scatter(seto["sepal_length"], seto["petal_length"], marker='o', c='b') 

vir_2 = plt.scatter(vir["sepal_length"], vir["petal_length"], marker='o', c='g') 

ver_2 = plt.scatter(ver["sepal_length"], ver["petal_length"], marker='o', c='r') 

plt.legend((seto_2, vir_2, ver_2),("Iris Setosa", "Iris Virginica", "Iris Versicolor"))
plt.title("Sepal Length vs Petal Length")
#plt.savefig("add_outputs/Scatter_SLvPL")
#plt.show()
plt.close()


plt.figure(6)

seto_3 = plt.scatter(seto["sepal_length"], seto["petal_width"], marker='o', c='b') 

vir_3 = plt.scatter(vir["sepal_length"], vir["petal_width"], marker='o', c='g') 

ver_3 = plt.scatter(ver["sepal_length"], ver["petal_width"], marker='o', c='r') 

plt.legend((seto_3, vir_3, ver_3),("Iris Setosa", "Iris Virginica", "Iris Versicolor"))
plt.title("Sepal Length vs Petal Width")
#plt.savefig("add_outputs/Scatter_SLvPW")
#plt.show()
plt.close()

plt.figure(7)

seto_4 = plt.scatter(seto["sepal_length"], seto["sepal_width"], marker='o', c='b') 

vir_4 = plt.scatter(vir["sepal_length"], vir["sepal_width"], marker='o', c='g') 

ver_4 = plt.scatter(ver["sepal_length"], ver["sepal_width"], marker='o', c='r') 

plt.legend((seto_4, vir_4, ver_4),("Iris Setosa", "Iris Virginica", "Iris Versicolor"))
plt.title("Sepal Length vs Sepal Width")
#plt.savefig("add_outputs/Scatter_SLvSW")
#plt.show()
plt.close()

plt.figure(8)

seto_5 = plt.scatter(seto["sepal_width"], seto["petal_length"], marker='o', c='b') 

vir_5 = plt.scatter(vir["sepal_width"], vir["petal_length"], marker='o', c='g') 

ver_5 = plt.scatter(ver["sepal_width"], ver["petal_length"], marker='o', c='r') 

plt.legend((seto_3, vir_3, ver_3),("Iris Setosa", "Iris Virginica", "Iris Versicolor"))
plt.title("Sepal Width vs Petal Length")
#plt.savefig("add_outputs/Scatter_SWvPL")
#plt.show()
plt.close()

plt.figure(9)

seto_6 = plt.scatter(seto["sepal_width"], seto["petal_width"], marker='o', c='b') 

vir_6 = plt.scatter(vir["sepal_width"], vir["petal_width"], marker='o', c='g') 

ver_6 = plt.scatter(ver["sepal_width"], ver["petal_width"], marker='o', c='r') 

plt.legend((seto_6, vir_6, ver_6),("Iris Setosa", "Iris Virginica", "Iris Versicolor"))
plt.title("Sepal Width vs Petal Width")
#plt.savefig("add_outputs/Scatter_SWvPW")
#plt.show()
plt.close()


# 3 No. scatter plots subplots grouped by flower class
f, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.scatter(seto["sepal_length"], seto["petal_length"], marker='.', c='b', label="Iris Setosa")
ax1.scatter(vir["sepal_length"], vir["petal_length"], marker='.', c='g', label="Iris Virginica")
ax1.scatter(ver["sepal_length"], ver["petal_length"], marker='.', c='r', label="Iris Versicolor")
ax1.legend(fontsize="x-small", markerscale=2, edgecolor="black")
ax1.set_xlabel('Sepal Length')
ax1.set_ylabel('Petal Length')

ax2.scatter(seto["sepal_length"], seto["petal_width"], marker='.', c='b', label="Iris Setosa")
ax2.scatter(vir["sepal_length"], vir["petal_width"], marker='.', c='g', label="Iris Virginica")
ax2.scatter(ver["sepal_length"], ver["petal_width"], marker='.', c='r', label="Iris Versicolor")
ax2.legend(fontsize="x-small", markerscale=2, edgecolor="black")
ax2.set_xlabel('Sepal Length')
ax2.set_ylabel('Petal Width')

ax3.scatter(seto["petal_length"], seto["petal_width"], marker='.', c='b', label="Iris Setosa")
ax3.scatter(vir["petal_length"], vir["petal_width"], marker='.', c='g', label="Iris Virginica")
ax3.scatter(ver["petal_length"], ver["petal_width"], marker='.', c='r', label="Iris Versicolor")
ax3.legend(fontsize="x-small", markerscale=2, edgecolor="black")
ax3.set_xlabel('Petal Length')
ax3.set_ylabel('Petal Width')

plt.show()
