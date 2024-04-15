# analysis
# Author: Sylvia Chapman Kent
# analyses Fisher's Iris data set

# Program currently layers each histogram over the previous ones: this is unintended 

# importing the modules we'll use during the analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# loading the iris data set
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# creating a function to generate histograms as we'll need one for each variable
def generate_hist(variable):
    histogram_data = variable # gets the data for the histogram
    histogram_data = histogram_data.to_numpy() # converts data frame to array so we can plot it
    plt.hist(histogram_data) # creates the histogram
    plt.savefig(plot_name) # saves the plot as a PNG file 
'''   
# creating another function to generate scatter plots
def generate_scatter(x,y):
    x = np.array[()]
    y = np.array[()]
    plt.scatter(x,y) # creates the scatter plot
    plt.show() # shows the scatter plot
'''

variable = df["sepal_length"] # we want to plot the sepal lengths
plot_name = ("Sepal Length") 
histogram = generate_hist(variable)

variable = df["sepal_width"] # we want to plot the sepal widths
plot_name = ("Sepal Width") 
histogram = generate_hist(variable) 

variable = df["petal_length"] # we want to plot the petal lengths
plot_name = ("Petal Length") 
histogram = generate_hist(variable) 

variable = df["petal_width"] # we want to plot the petal widths
plot_name = ("Petal Width") 
histogram = generate_hist(variable) 
