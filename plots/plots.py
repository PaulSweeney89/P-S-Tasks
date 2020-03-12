# plots - Fuctions of X

import numpy as np                              # import numpy library as np.

import matplotlib.pyplot as plt                 # import matplot library as plt.

x = np.arange(0, 4, 0.25)                       # numpy arange for values for x, starting x = 0 upto but not including x = 4 at 0.25 increments.

f = x                                           # Function 1: f(x) = x
g = x**2                                        # Function 2: g(x) = x^2 (squared)
h = x**3                                        # Function 3: h(x) = x^3 (cubed)    

plt.plot(x, f, "b.", label="f(x) = x")          # plotting x vs f(x) as blue dots & label "f(x) = x"
plt.plot(x, g, "r.", label="g(x) = x**2")       # plotting x vs g(x) as blue dots & label "g(x) = x**2"
plt.plot(x, h, "g.", label="h(x) = x**3")       # plotting x vs h(x) as blue dots & label "h(x) = x**3"

plt.legend()                                    # include legend in plot.
plt.title("Functions of X")                     # add title to plot.

#plt.savefig("plots.png")                       # option to save plot as .png file.

plt.show()                                      # display plot.
