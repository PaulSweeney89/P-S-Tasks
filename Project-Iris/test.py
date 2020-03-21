
import pandas as pd                                                             
import matplotlib.pyplot as plt                                                 

head_row = ["Sepal Length", "Sepal Width", "Petal Length",                      
            "Petal Width", "Class"]

df = pd.read_csv("datasets/bezdekIris.data", names=head_row)                    
# Histograms of Variables
                                                                           
colour = ['r', 'g', 'b', 'c']                                                  
n = 0                                                                           
 
                                                                 
for n in range(0, 4):                                                            

    var = head_row[n] 
    l_var = len(df[var])                                                                  
    plt.figure(n)                                                               
    plt.hist(df[var], bins=7, facecolor=colour[n], ec="black")                  
    plt.xlabel(var)                                                             
    plt.ylabel("Sample Freq")                                                   
    plt.title("Histogram of " + var)                                                                                                                        
    print(var) 
    print(len(df[var]))                       
    n = n + 1  

    plt.show()  
