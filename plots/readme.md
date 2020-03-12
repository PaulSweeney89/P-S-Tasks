# plots

**Simple script to  or program to create & plot 'X' vs 3 No. functions of 'X' on single graph or plot.**

*Week 8 task*

Program Overview:
- imports numpy library to use additional functions in python.
```
import numpy as np
```
- imports matplotlib library to use for plotting graphs in python.
```
import matplotlib.pyplot as plt
```
- program sets out the pre-defined range values of x to be plotted on the x-axis, using numpy arange.
    - start number: x = 0 (inclusive).
    - stop number: x = 4 (exclusive, does not include the value 4).
    - step number: 0.25 (step increment of 0.25, small increments results in a more defined plot shape)
```
x = np.arange(0, 4, 0.25)
```
- program solves the 3 No. pre-defined functions of x to be plotted on the y-axis.
  - Function 1: f(x) = x
  - Fucntion 2: g(x) = x\**2 (squared)
  - Function 3: h(x) = x\**3 (cubed)
```
f = x         #Function 1                                          
g = x**2      #Function 2                                       
h = x**3      #Function 3
```
- program plots x vs y (function of x), setting the colour of the plot points & legend labels.
```
plt.plot(x, f, "b.", label="f(x) = x")          # plotting x vs f(x) as blue dots
plt.plot(x, g, "r.", label="g(x) = x**2")       # plotting x vs g(x) as red dots
plt.plot(x, h, "g.", label="h(x) = x**3")       # plotting x vs h(x) as green dots
```
- program includes legend & title of plot.
```
plt.legend()                                    
plt.title("Functions of X") 
```
- program displays the plot of the 3 functions on a single graph, alternatively the plot can be saved as a .png file.
```
plt.show()
#plt.savefig("plots.png")                       # option to save plot as .png file.
```
Program output:

![plot](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/plots/plots.png)
