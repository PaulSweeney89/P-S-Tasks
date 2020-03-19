# Project Iris #

**Programming & Scripting Project 2020**

*Research of the Fisher's Iris dataset and the developement of a program to read and analyize the dataset.*

## Introduction ##

This project forms part of the programming & scripting module for 2020, please refer to the [project.pdf](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/project.pdf) document included in this repository for the full project outline & instructions.

The project is conducted under 3 main sections:

- Research & download of the Fisher's Iris dataset, including an overview & review of the dataset & a brief description of any new topics or terminologies encountered within the subject matter.

- Development & writing of the python program for the import, cleaning & analysis of the dataset, including explanations of the code developed, reasons for choice of code used along with highlighting any limitations within code. 

- Analysis of the dataset & review of the program outputs, reporting on & summarizing any findings within the dataset & project.

## Research ##

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

## Download & Review of Dataset ##

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

To review & identify the above discrepencies a simple script *review_data.py* has been written & included as part of this project.

The script was used to read & compare both *bezdekIris.data* and *iris.data* datasets, identify the known discrepencies and to determine which dataset to use as part of this project.

**Review Script**

- import pandas python library
```
import pandas as pd
```
- Read in both datasets *bezdekIris.data* and *iris.data* as df_1 & df_2 respectively using pandas **read_csv()** function, include the missing datasets header rows - (sepal length, sepal width etc.) 
```
head_row= ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

df_1 = pd.read_csv("bezdekIris.data", sep=",", names=head_row)
df_2 = pd.read_csv("iris.data", sep=",", names=head_row)
```
- Review rows 35 & 38 (index rows 34 to 37) in both datasets for discrepencies noted in *iris.names* text file, using pandas **loc** function to access the required rows within the dataframe.
```
print(df_1.loc[34:37])
print(df_2.loc[34:37])
```
- Output of rows 35 to 38 (index rows 34 to 37) & review:

![review_datasets](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Review%20Datasets.png)

df_1 - *bezdekIris.data* appears to contain the corrected sample values.

- Further compare datasets, using pandas concatuate **concat()** function to fully combine df_1 & df_2, followed by the **drop_duplicates(keep=False)** function to remove all dublicate rows within the combined dataset.
```
print(pd.concat([df_1,df_2]).drop_duplicates(keep=False))- [x]- [x]- [x]
```

![review_datasets_drop_dup](https://github.com/PaulSweeney89/P-S-Tasks/blob/master/Project-Iris/Images/Review%20Datasets%20-%20drop_duplicates.png)

Only index rows 34 & 37 remain, therefore there are no other discrepencies between the datasets.

- Following the review of the 2 datasets from the UCL archive, it was found that *bezdekIris.data* contains the correct ammended sample values and will therefore be used in this project. 

# Development of the Program *analysis.py*

As part of the project, the 3 main tasks of the program is:

1.  - [x] output a summary of each variable to a single text file.
2.  - [ ] saves a histogram of each variable to png files.
3.  - [ ] outputs a scatter plot of each pair of variables.

1. **Summaries of Dataset Variables** 

- Import pandas & matplotlib python libraries to be used as part of the program & analysis of the Iris dataset.
```
import pandas as pd
import matplotlib.pyplot as plt
```
- read the dataset using pandas **read_csv()** function, incuding the dataset's header row, as previously done in the *review_data.py* script
```
head_row = ["sepal_length", "sepal_width", "petal_length",
            "petal_width", "class"]

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
>   DATASET VARIABLES SUMMARIES:

>        sepal_length  sepal_width  petal_length  petal_width
>   count    150.000000   150.000000    150.000000   150.000000
>   mean       5.843333     3.057333      3.758000     1.199333
>   std        0.828066     0.435866      1.765298     0.762238
>   min        4.300000     2.000000      1.000000     0.100000
>   25%        5.100000     2.800000      1.600000     0.300000
>   50%        5.800000     3.000000      4.350000     1.300000
>   75%        6.400000     3.300000      5.100000     1.800000
>   max        7.900000     4.400000      6.900000     2.500000

2. **Histograms of Variables**













References:

[Iris Data Set Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set)

[Wiki Commons Flower Images](https://commons.wikimedia.org/wiki/File:Iris_versicolor_3.jpg)

Note: Text added to images from Wiki Commons using GIMP - GNU Image Manipulation Program

[Statistics4u - Linear Discriminant Analysis](http://www.statistics4u.com/fundstat_eng/cc_lda_intro.html)

[Pandas Difference between Dataframes](https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/)

[Writing output to text file](https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python)


 
 

