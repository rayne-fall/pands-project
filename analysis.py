# analysis
# Author: Sylvia Chapman Kent
# analyses Fisher's Iris data set

# importing the modules we'll use during the analysis
import matplotlib as plt
import numpy as np
import pandas as pd

# creating a function to generate histograms as we'll need one for each variable
def generate_hist(hist_title):
    histogram_data = ()
    plt.hist(histogram_data) # creates the histogram
    plt.savefig(hist_title) # this function will save a plot as a PNG file 

# creating another function to generate scatter plots
def generate_scatter(x,y):
    x = np.array[()]
    y = np.array[()]
    plt.scatter(x,y) # creates the scatter plot
    plt.show # shows the scatter plot