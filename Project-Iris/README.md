# Project Iris #
- - - - - - - - - 
**Programming & Scripting Project 2020**

*Research of the Fisher's Iris dataset and the developement of a program to read and analyize the dataset.*

- - - - - - - - -
## Introduction ##
- - - - - - - - -

This project forms part of the programming & scripting module for 2020, please refer to the [project.pdf](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/project.pdf) document included in this repository for the full project outline & instructions.

The project is conducted under 3 main sections:

- Research & download of the Fisher's Iris dataset, including an overview & review of the dataset & a brief description of any new topics or terminologies encountered within the subject matter.

- Development & writing of the python program for the import, cleaning & analysis of the dataset, including explanations of the code developed, reasons for choice of code used along with highlighting any limitations within code. 

- Analysis of the dataset & review of the program outputs, reporting & summarizing any findings within the dataset & project.

- - - - - - - - -
## Research ##
- - - - - - - - -

The Iris flower dataset or Fisher's Iris dataset was introduced by the British statistician and biologist Ronald Fisher in 1936.
There are over 250 varieties of the iris flower and they come in a wide range of colours, the greek word iris means rainbow.

Fisher's data set contains 3 species of the Iris plant: 

- Iris Setosa 
- Iris Virginica 
- Iris Versicolor

| Iris Setosa | Iris Versicolor | Iris Virginica  |
|----------------------------------------|----------------------------------------|----------------------------------------|
| ![setosa](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Iris%20Setosa%20-%20resized.jpeg) | ![versicolor](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Iris%20Versicolor%20-%20resized.jpeg) | ![virginica](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Iris%20Virginica%20-%20resized.jpeg) |
 
50 samples of each of the 3 species were taken, with 4 characteristics of the flowers measured, the species of the flower was also included as a 5th attribute within the dataset.

1. sepal length (cm)
2. sepal width (cm)
3. pedal length (cm)
4. pedal width (cm)
5. species
 
Therefore there is 50 samples for each of the 3 species of Iris, each with 5 attributes giving a total number of 750 data points within Fischer's dataset.

From the dataset Fisher developed a linear discriminant model to distinguish the 3 species from each other.

*linear discriminant model* - is a statisical model that is developed to discriminate between or separate two or more groups of samples in order to develop a classifier.

e.g Fisher's analysis of the Iris dataset was able to classify the Iris flowers into 1 of the 3 species (Iris Setosa, Iris Versicolor, Iris Virginica) based on the observed features of the flower from the sample data (sepal length, sepal width, pedal length, pedal width). 

- - - - - - - - -
## Download & Review of Dataset ##
- - - - - - - - -

The dataset has been downloaded from the University of California (UCL), Center for Machine Learning and Intelligent Systems repository website found [here](http://archive.ics.uci.edu/ml/datasets/Iris).

The archive contains the following files:

- Index                     (text file containing the list of files within the directory along with the files creation dates)
- bezdekIris.data           (dataset with comma-separated values)
- iris.data                 (dataset with comma-separated values)
- iris.names                (README text file with dataset info)

On review of the README text file, it notes that the dataset contains some discrepencies, identified by Steve Chadwick.

> The 35th sample should be: 4.9, 3.1, 1.5, 0.2, "Iris-setosa"
> where the error is in the fourth feature.

> The 38th sample: 4.9, 3.6, 1.4, 0.1, "Iris-setosa"
> where the errors are in the second and third features.

To review & identify the above discrepencies a simple script *review_data.py* has been written & included as part of this project, which can be found in the script folder in this reposirory. 

The script was used to read & compare both *bezdekIris.data* and *iris.data* datasets, identify the known discrepencies and to determine which dataset to use as part of this project.

**Review Script**

- Import pandas python library
```
import pandas as pd
```
- Read in both datasets *bezdekIris.data* and *iris.data* as df_1 & df_2 respectively using pandas **read_csv()** function, include the missing datasets header rows - (sepal length, sepal width etc.) 
```
head_row= ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

df_1 = pd.read_csv("bezdekIris.data", sep=",", names=head_row)
df_2 = pd.read_csv("iris.data", sep=",", names=head_row)
```
- All outputs of the review script written to a text file *review_output.txt* in the *add_outputs* folder.
```
f = open("add_outputs/review_output.txt", "w+")
```
- Dataset info for df_1 & similar for df_2, print heading & write output to text file.
```
print("dataset 1 (bezdekIris.data) info output:", file=f)
df_1.info(buf=f)
```
- Check for any null or missing values within the datasets, using the **isnull()** function and **sum()** function to sum the number of missing values per dataset columns, print heading & write to text file. 
```
print("dataset 1 - missing values", file=f)
print(df_1.isnull().sum(), file=f)
```

![review_datasets](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/ )

- Review rows 35 & 38 (index rows 34 to 37) in both datasets for discrepencies noted in *iris.names* text file, using pandas **loc** function to access the required rows within the dataframe, written to text file.
```
print(df_1.loc[34:37], file=f)
print(df_2.loc[34:37], file=f)
```
- Output of rows 35 to 38 (index rows 34 to 37) & review:

![review_datasets](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Review%20Datasets.png)

df_1 - *bezdekIris.data* appears to contain the corrected sample values.

- Further compare datasets, using pandas concatuate **concat()** function to fully combine df_1 & df_2, followed by the **drop_duplicates(keep=False)** function to remove all dublicate rows within the combined dataset, written to text file.
```
print(pd.concat([df_1,df_2]).drop_duplicates(keep=False), file=f)
```

![review_datasets_drop_dup](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Review%20Datasets%20-%20drop_duplicates.png)

Only index rows 34 & 37 remain, therefore there are no other discrepencies between the datasets.

- Following the review of the 2 datasets from the UCL archive, it was found that, both datasets contain no missing values and that *bezdekIris.data* contains the correct ammended sample values and will therefore be used in this project. 

----------------------------------------------------------------------------------------------------------------------------
## Development of the Program *analysis.py* ##
----------------------------------------------------------------------------------------------------------------------------

As part of the project, the 3 main tasks of the program is:

1.  - [x] output a summary of each variable to a single text file 
2.  - [x] saves a histogram of each variable to png files
3.  - [x] outputs a scatter plot of each pair of variables 

**1. Summary of Dataset Variables** 

- Import pandas & matplotlib python libraries to be used as part of the program & analysis of the Iris dataset.
```
import pandas as pd
import matplotlib.pyplot as plt
```
- Read the dataset using pandas **read_csv()** function, incuding the dataset's header row, as previously done in the *review_data.py* script
```
head_row = ["Sepal Length", "Sepal Width", "Petal Length",
            "Petal Width", "Class"]

df = pd.read_csv("datasets/bezdekIris.data", names=head_row)
```
- To output a summary of each variable within the dataset & save within a text file.
    - use python's **with** statement to **open** & automatically close a writeable 'w' text file named *summary.txt*
    - use pandas **dataframe.describe()** method to print the dataset variables summaries to *summary.txt*
    - in the interest of keeping the project repository clean & organised all project outputs are to be saved in the *outputs* folder.
```
with open('outputs/summary.txt', 'w') as f:
    print("DATASET VARIABLES SUMMARIES:\n\n", df.describe(), file=f) 
```
- *summary.txt* output:

![summary](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Summary.png)

**2. Histograms of Dataset Variables**

- To produce the histograms for the 4no. variables within the dataset, a **for** loop has been written to complete the task, keeping the code short, concise & hopefully clear.
```
colour = ['r', 'g', 'b', 'c']
n = 0
```
- The list *colour* will be used within the for loop to produce a different colour histogram for each of the dataset variables, "r" red, "g" green, "b" blue & "c" cyan.
- n = 0, the starting value for n in the **for** loop.
``` 
for n in range(0, 4): 
                                                           
    var = head_row[n]
    plt.figure(n)
    plt.hist(df[var], bins=7, facecolor=colour[n], ec="black")
    plt.xlabel(var)
    plt.ylabel("Sample Freq")
    plt.title("Histogram of " + var)
    plt.savefig(fname="outputs/" + var + " histogram") 
    n = n + 1
```
- The **for** loop will complete 4no. iterations - (n=0, n=1, n=2, n=3), 1no. iteration for each of the 4 variables in the dataset.
- For each internation the **for** loop will:
    - Retrieve the name of the variable from the *head_row* list, e.g var = head_row[n=1] = "Sepal Width", which will also be used to input the histogram's array, histograms label, histogram title and the output file name. 
    - Produce a figure(n=0 to n=3, 4no.) for plotting a individual historgram for each variable.
    - Plot a historgram with the dataframe's variable column as an array, with the number of histogram bins being set to 7, the colour of the histogram being set by the colour list and the edgecolour set to black to improve the visual display of the histograms.
    - Plot the labels for the histograms, xlabel = variable name & ylabel = sample frequency.
    - Plot the title of the histogram with the individual variable name.
    - Save the histogram as a .png file in the outputs folder of the repository with the filename including the variable name.
- n = n+1 to continue to the next step of **for** loop iteration. 

**3. Scatter Plots of Pairs of Dataset Variables**

- To produce the scatter plots for all pairs of the dataset variables, a total number of 6 scatter plots will be required:
    
    1. Sepal Length (SL) v Sepal Width (SW)
    2. Sepal Length (SL) v Petal Length (PL)
    3. Sepal Length (SL) v Petal Width (PW) 
    4. Sepal Width (SW) v Petal Length (PL)
    5. Sepal Width (SW) v Petal Width (PW)
    6. Petal Lenth (PL) v Petal Width (PW)

- Matplotlib's **.subplots()** method has been used to create a number of subplots on a single figure, providing a clear and compact plot for reviewing all the scatter plots.
- Each of the dataset's variables or column arrays have been assigned a name, to help simipfy the reading & writing of the code.
```
sl = df["Sepal Length"]
sw = df["Sepal Width"]
pl = df["Petal Length"]
pw = df["Petal Width"]
```
- Creating a single figure, *f*, with 6no. subplots or axes, *ax1*, *ax2*...etc. The figure will consist of 3 rows of 2 axes or subplots. 
```
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
```
- Providing a title to the figure.
```
f.suptitle("Scatter Plots - Pairs of Variables") 
```
- Specifying the x & y axis for each scatter plot, e.g x=sl & y=sw (X-axis = Sepal Length, Y-axis = Sepal Width). 
Setting the plot marker style, '.' for small dots for the data points. 
Setting the colour for the data points c='b' blue, and applying a label to the plot. This is similarlly repeated for *ax2*, *ax3*...etc.
```
ax1.scatter(sl, sw, marker='.', c='b', label="SL v SW") 
```
- Applying a legend for each subplot, for clarity & to prevent clashes with the data points on the plot, the frontsize has been set to 'extra small'.
The markerscale has been increased by 2 to distinguish the label point from the datapoints on the plot.
The edge colour of the legend box has been set to black, again for clarity. Similarly this is repeated for each of the subplots, *ax2*, *ax3*...etc. 
```
ax1.legend(fontsize="x-small", markerscale=2, edgecolor="black")
```
- Following specifying each of the 6no. axes to be plotted on the figure, the figure is saved in the *outputs* folder in the repository.
```
plt.savefig(fname="outputs/Scatter Plots - Pairs of Variables")
```
- In addition to the subplots of each individual pair of variables, code has been writen to display all the pairs combined on a single scatter plot. 
```
plt.figure(5)
plt.scatter(sl, sw, marker='.', c='b', label="SL v SW") 
plt.scatter(sl, pl, marker='.', c='g', label="SL v PL")
plt.scatter(sl, pw, marker='.', c='m', label="SL v PW")
plt.scatter(sw, pl, marker='.', c='c', label="SW v PL")
plt.scatter(sw, pw, marker='.', c='r', label="SW v PW") 
plt.scatter(pl, pw, marker='.', c='y', label="PL v PW")
plt.legend(fontsize="x-small", markerscale=2, edgecolor="black")
plt.title("Combined Scatter Plots - Pairs of Variables")

plt.savefig(fname="outputs/Combined Scatter Plots - Pairs of Variables") 
```
- As part of this project's requirements, a total number of 6 plots have been produced, all saved as the default .png file in the *outputs* folder.
    - Sepal Length histogram.png
    - Sepal Width histogram.png
    - Petal Length histogram.png
    - Petal Width histogram.png
    - Scatter Plots - Pairs of Variables.png
    - Combined Scatter Plots - Pairs of Variables.png

**Note:** during the undertaking of this project and to aid with the main work of this project, additional scripts and plots have been produced for testing different code and experiementing with different plots and outputs. These files can be found in the *scripts* & *add_outputs* folders.

- - - - - - - - -
## Analysis & Review of Program Outputs ##
- - - - - - - - -


References:

[Iris Data Set Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set)

[Wiki Commons Flower Images](https://commons.wikimedia.org/wiki/File:Iris_versicolor_3.jpg)

[Statistics4u - Linear Discriminant Analysis](http://www.statistics4u.com/fundstat_eng/cc_lda_intro.html)

[Pandas Difference between Dataframes](https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/)

[Writing output to text file](https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python)

[Real Python Matplotlib](https://realpython.com/python-matplotlib-guide/)

**Additional Notes:** 
- Text & mark-ups added to images & screenshots using GIMP - GNU Image Manipulation Program.
 

