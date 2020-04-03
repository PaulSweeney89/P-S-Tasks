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

The Iris flower dataset or Fisher's Iris dataset was introduced by the British statistician and biologist Ronald Fisher in 1936. The dataset is also known Anderson's Iris data set, as it was originally collected by the American botanist, Edgar Anderson. 
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
 
Therefore there is 50 samples for each of the 3 species of Iris, with 5 attributes giving a total number of 750 data points within Fischer's dataset.

From the dataset Fisher developed a linear discriminant model to distinguish the 3 species from each other.

*linear discriminant model* - is a statisical model that is developed to discriminate between or separate two or more groups of samples in order to develop a classifier.

Fisher's analysis of the Iris dataset was able to group or classify the samples into 1 of the 3 species (Iris Setosa, Iris Versicolor, Iris Virginica) based on the observed features of the flower from the sample data (sepal length, sepal width, pedal length, pedal width). 

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
- Output of sum of missing values - no missing values within both datasets.

![review_datasets](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Review%20null%20values.png)

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

As part of the project, the 3 main tasks of the program is to:

1.  - [x] output a summary of each variable to a single text file 
2.  - [x] save a histogram of each variable to png files
3.  - [x] output a scatter plot of each pair of variables 

**1. Summary of Dataset Variables** 

- Import pandas & matplotlib python libraries to be used as part of the program & analysis of the Iris dataset. Numpy was imported to use np.arange() & np.ones() functions,matplotlib.ticker module was also imported for configuring & formatting the axes ticks of the histograms.  
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
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
    - in the interest of keeping the project repository clean & organised all project outputs are saved in the *outputs* folder.
```
with open('outputs/summary.txt', 'w') as f:
    print("DATASET VARIABLES SUMMARIES:\n\n", df.describe(), file=f) 
```
- *summary.txt* output:

![summary](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Summary.png)

**2. Histograms of Dataset Variables**

- Each of the dataset's variables or column arrays have been assigned a name, to help simipfy the reading & writing of the code & project program.
```
sl = df["Sepal Length"]
sw = df["Sepal Width"]
pl = df["Petal Length"]
pw = df["Petal Width"]
```
- To produce the histograms for the 4no. variables within the dataset, a **for** loop has been written to complete the task, keeping the code short, concise & hopefully clear.
```
colour = ['b', 'g', 'm', 'r']
n = 0
n_bins = 7 
```
- The list *colour* will be used within the for loop to produce a different colour histogram for each of the dataset variables, "b" blue,  "g" green, & "m" magenta & "r" red.
- n = 0, the starting value for n in the **for** loop.
- The number of bins (n_bins) to be used in all histograms has been set to 7, following the review of a number histograms with different options, 7 bins appear to display practical distribution shape for the histograms. 
``` 
for n in range(0, 4): 
                                                           
    var = head_row[n]
    plt.figure(n)
    plt.hist(df[var], bins=n_bins, facecolor=colour[n], ec="black")

    start = min(df[var])
    end = max(df[var])
    step = (end - start) / n_bins
    plt.xticks(arange(start, (end + step) ,step))
                                                      
    plt.xlabel(var)
    plt.ylabel("Sample Freq")
    plt.title("Histogram of " + var)
    plt.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
    plt.savefig(fname="outputs/" + var + " histogram")
    n = n + 1
```
- The **for** loop will complete 4no. iterations - (n=0, n=1, n=2, n=3), 1no. iteration for each of the 4 variables in the dataset.
- For each internation the **for** loop will:
    - Retrieve the name of the variable from the *head_row* list, e.g var = head_row[n=1] = "Sepal Width", which will also be used to input the histogram's array, histograms label, histogram title and the output file name. 
    - Produce a figure(n=0 to n=3, 4no.) for plotting a individual historgram for each variable.
    - Plot a historgram with the dataframe's variable column as an array, with the number of histogram bins being set to 7, the colour of the histogram being set by the colour list and the edgecolour set to black to improve the visual display of the histograms.
    - plot the histogram bin range values or xtick values, starting with the minimum variable value & finishing with the max vaiable value and all the bin range values inbetween which are determined by the width of the bins or the number of bins used for the histogram. The **numpy.arange()** function was used to plot the xtick values.
    - Plot the labels for the histograms, xlabel = variable name & ylabel = sample frequency.
    - Plot the title of the histogram with the individual variable name.
    - plot a horizontal grid off the y-axis tick values, setting the linestyle and lineweight.
    - Save the histogram as a .png file in the outputs folder of the repository with the filename including the variable name.
- n = n+1 to continue to the next step of **for** loop iteration. 

**Plotting Combined Histograms on Single Figure**

- An additional useful plot displaying the 4 No. variable histograms combined together on a single figure has also been included in the *outputs* folder.
- Similarlly to the code for producing the scatter plots below, Matplotlib's **.subplots()** method has been used to create a number of subplots on a single figure.
- Creating a single figure, *fig*, with 4no. subplots or axes, *ax1*, *ax2*...etc. The figure will consist of 2 rows of 2 axes or subplots. 
*sharey=True*, y-axis to be shared between plots on each row, i.e ax1 & ax3 and ax2 & ax4 will use the same y-axis, which will help produce clear & legible plots and will also accomodate ease of comparision between the histograms or variables.
```
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True)
```
- Specifying the variable sl (sepal length) for the first histogram plot on axes ax1 of the figure. Number of bins for the histogram set to the previously assigned value, n_bins = 7. edge colour set to black to help distinguish between the bins of the histogram.
- The bin count values of the histogram were weighted so the results are displayed as a precentage of the total sample number rather than showing the sample number. 
- Setting the label of the y-axis of ax1 which is share with ax3. 
```
ax1.hist(sl, weights=np.ones(len(sl)) / len(sl),
            bins=n_bins, facecolor='blue', ec="black",                          
            label="Sepal Length (cm)")
ax1.set(ylabel="Percentage of Samples")
```
- As from the histograms above, plotting or setting the histogram bin range values or xtick values.
```
start = min(sl)
end = max(sl)
step = (end - start) / n_bins
ax1.set_xticks(arange(start, (end + step) ,step)) 
```
- In addition to displaying the xtick or bin ranges values on the x-axis of the subplots, another very useful and practical application is to use the matplotlib.ticker (imported as mtick) module to format the histogram axes ticks. 
In this incidence using the **PercentFormatter()** to with the weighted count values sets the y-axis and histogram sample counts as a percentage of the total sample counts, which helps improve the insights into the dataset and comparisions between the histograms.
```
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
```
- Adding a horizontal grid off the y-axis tick values, setting the linestyle and lineweight.
```
ax1.grid(which='major', axis='y', linestyle='dotted', alpha=0.8)
```
- Applying a legend to axes ax1, to help distinguish between the 4no. variable histograms.
```
ax1.legend()
```
- The above configuring of ax1, is similarly repeated for each of the axes or subplots, *ax2*, *ax3*...etc.
- matplotlib **tight_layout()** to automatically adjust the subplot parameters so the subplots fits witin the figure area
- Save the histogram as a .png file in the outputs folder of the repository
```
plt.tight_layout()
plt.savefig(fname="outputs/Combined Histograms") 
```

**3. Scatter Plots of Pairs of Dataset Variables**

- To produce the scatter plots for all pairs of the dataset variables, a total number of 6 scatter plots will be required:
    
1. Sepal Length (SL) v Sepal Width (SW)
2. Sepal Length (SL) v Petal Length (PL)
3. Sepal Length (SL) v Petal Width (PW) 
4. Sepal Width (SW) v Petal Length (PL)
5. Sepal Width (SW) v Petal Width (PW)
6. Petal Lenth (PL) v Petal Width (PW)

- Matplotlib's **.subplots()** method has been used to create a number of subplots on a single figure, providing a clear and compact plot for reviewing all the scatter plots.
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
Setting the markerstyle, the colour c='b' and label for each of the scatter plots. 
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
- As part of this project's requirements, a total number of 7 plots have been produced, all saved as the default .png file in the *outputs* folder.
    - Sepal Length histogram.png
    - Sepal Width histogram.png
    - Petal Length histogram.png
    - Petal Width histogram.png
    - Combined Histograms.png
    - Scatter Plots - Pairs of Variables.png
    - Combined Scatter Plots - Pairs of Variables.png

**Note:** during the undertaking of this project and to aid with the development of the program, additional scripts and plots have been produced, these files can be found in the *scripts* folder and the *add_outputs* folder.

- - - - - - - - -
## Analysis & Review of Program Outputs ##
- - - - - - - - -
- Review of the iris dataset summary, shows that the sepal lengths & sepal widths of the plant are larger than the petal lengths and widths.
    - The mean sepal length is approx 1.5 times longer than the mean petal length.
    - The mean sepal width is approx 2.5 times wider than the mean petal width.
    - This would be as expected as the sepal of a flower forms the protective encasing layer of a flower in bud, and is the first layers of a flower to open during bloom.

![summary](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Summary.png)

- Review of the histograms:
    - The sepal length histogram shows a wide spread distribution with only small variations in the number of samples between the different ranges of lengths. The peak of the histogram occurs at the sepal length range of approx. 5.3 - 5.8cm with approx. 23% of the samples (~34 No.)  occuring within this range. From the summary output it can be seen that the mean sepal length ~ 5.8cm.
    - The sepal width histogram has a more definite peak, with almost 40% of the samples (~59 No.) occuring within the width range of approx. 2.6 - 3.0cm. From the summary output it can be seen that the mean sepal width ~ 3.1cm.
    - The petal length histogram displays 2 peaks, the first in the approx. range 1.0 - 1.8cm with approx 32% of the samples (~48 No.) occurring here and the second occurring in the approx. range 4.3 - 5.2cm, with just under 30% (~43 No.) of the samples occurring within this range. The 2 peaks in the histogram may indicate a distinctive difference between the petal length variables, one cluster made up of samples within the first shorter petal length range and a second cluster of samples with longer length petals.
    - Similar to the petal length histogram the petal width histogram follows a similar shape with 2 peaks, which may also indicate 2 distinctive clusters of samples within the dataset. The first hisogram peak occurs at the petal width range of approx 0.1 - 0.4cm with a sample number of approx. 32% (~48 No.), while the second peak in the range of petal width of 1.4 - 1.8cm with 20% of the samples (30 No.)

![histograms combined](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/outputs/Combined%20Histograms.png)

- Review of scatterplots:
    - From reviewing the scatter plots it can be seen that a number of the variable pairs display various levels of linear correlation, while other variable pairs don't appear to show a distinct relationship.
    - Sepal Length (SL) vs Petal Length (PL) shows a moderate positve linear correlation.
    - Sepal Length (SL) vs Petal Length (PW) shows a moderate positve linear correlation.
    - Petal Length (PL) vs Petal Width (PW) shows a strong positve linear correlation. 
    - The remaining 3 No. scatterplots of pairs of variables, Sepal Length (SL) vs Sepal Width (SW), Sepal Width vs Petal Length (PL) & Sepal Width vs Petal Width (PW) appear random and do not display a clear relationship between variables.

![scatter plots paired](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/outputs/Scatter%20Plots%20-%20Pairs%20of%20Variables.png)

- To further investigate the relationship between the pairs of variables within the dataset, a number of additional scatterplots have been included with this project.
- The seaborn python library has been used to include scatterplots displaying the data points grouped by 'class' i.e flower species and also display the scatterplot's 'best fit line' or regression line. 

![seabornPLvPW](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/scripts/add_outputs/Seaborn_Scatter_PLvPW.png)
![seabornSLvPL](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/scripts/add_outputs/Seaborn_Scatter_SLvPL.png)
![seabornSLvPW](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/scripts/add_outputs/Seaborn_Scatter_SLvPW.png)

- 

References:

[Iris Data Set Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set)

[Wiki Commons Flower Images](https://commons.wikimedia.org/wiki/File:Iris_versicolor_3.jpg)

[Statistics4u - Linear Discriminant Analysis](http://www.statistics4u.com/fundstat_eng/cc_lda_intro.html)

[Pandas Difference between Dataframes](https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/)

[Writing output to text file](https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python)

[Real Python Matplotlib](https://realpython.com/python-matplotlib-guide/)

[Histogram Y-axis as Percentage](https://stackoverflow.com/questions/51473993/plot-an-histogram-with-y-axis-as-percentage-using-funcformatter)

[Histogram adding grids](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.grid.html)

**Additional Notes:** 
- Text & mark-ups added to images & screenshots using GIMP - GNU Image Manipulation Program.
 

