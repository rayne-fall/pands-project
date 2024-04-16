# analysis
# Author: Sylvia Chapman Kent
# analyses Fisher's Iris data set

# Program no longer layers each histogram over the previous ones

# importing the modules we'll use during the analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# loading the iris data set
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# creating a function to generate histograms as we'll need one for each variable
def generate_hist(variable):
    fig, ax = plt.subplots()
    histogram_data = variable # get the data for the histogram
    histogram_data = histogram_data.to_numpy() # convert data frame to array so we can plot it
    ax.hist(histogram_data) # create the histogram
    ax.set_xlabel("Number of flowers") # label the x axis
    ax.set_ylabel(f"{plot_name} (cm)") # label the y axis based on the variable we're looking at
    ax.set_title(plot_name) # put a title on the plot
    fig.savefig(plot_name) # save the plot as a PNG file 
'''   
# creating another function to generate scatter plots
def generate_scatter(x,y):
    x = np.array[()]
    y = np.array[()]
    plt.scatter(x,y) # creates the scatter plot
    plt.show() # shows the scatter plot
'''

variable = df["sepal_length"] # choose the variable to plot
plot_name = ("Sepal Length") # give a filename for the PNG
histogram = generate_hist(variable) # call the histogram function defined earlier

variable = df["sepal_width"] 
plot_name = ("Sepal Width") 
histogram = generate_hist(variable) 

variable = df["petal_length"] 
plot_name = ("Petal Length") 
histogram = generate_hist(variable) 

variable = df["petal_width"] 
plot_name = ("Petal Width") 
histogram = generate_hist(variable) 
