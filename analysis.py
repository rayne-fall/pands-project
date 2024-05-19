# analysis
# Author: Sylvia Chapman Kent
# analyses Fisher's Iris data set

# importing the modules we'll use during the analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load the iris data set
df = pd.read_csv("iris.csv")

# create the file we'll save a summary of the variables in and open it in write mode
file = open("Variable Summary.txt", "w")
# give an overview of the data and add the averages for each variable to the text file
file.write(f"This is an overview of the data in the set: \n\n{df}\n\n150 specimens were observed, with each having five physical characteristics recorded.\n\nThese are the average values for each of the variables in this dataset: \n\n{df.describe()}\n\nCalculating the correlation coefficients for each pair of variables allows us to see if there's any correlation between them.\nThe closer the coefficient is to 1/-1, the stronger the correlation.\nThe closer the coefficient is to 0, the weaker the correlation")
# close the text file
file.close()

# creating a function to generate histograms as we'll need one for each variable
def generate_hist(variable):
    fig, ax = plt.subplots() # stateless setup required as stateful setup plots each histogram on the one set of axes
    histogram_data = variable # get the data for the histogram
    histogram_data = histogram_data.to_numpy() # convert data frame to array so we can plot it
    ax.hist(histogram_data) # create the histogram
    ax.set_xlabel(plot_name) # label the x axis based on the variable we're looking at
    ax.set_ylabel("Number of flowers") # label the y axis
    ax.set_title(plot_name) # put a title on the plot
    fig.savefig(f"{plot_name}.png") # save the plot as a PNG file 

variable = df["sepal_length"] # choose the variable to plot
plot_name = ("Sepal Length (cm)") # give a filename for the PNG
histogram = generate_hist(variable) # call the histogram function defined earlier

variable = df["sepal_width"] 
plot_name = ("Sepal Width (cm)") 
histogram = generate_hist(variable) 

variable = df["petal_length"] 
plot_name = ("Petal Length (cm)") 
histogram = generate_hist(variable) 

variable = df["petal_width"] 
plot_name = ("Petal Width (cm)") 
histogram = generate_hist(variable) 

# creating another function to generate scatter plots
def generate_scatter(variable1,variable2): 
    fig, ax = plt.subplots()
    # get the x and y coordinates
    x_scatter = variable1 
    y_scatter = variable2
    # convert the data frames to arrays
    x_scatter = x_scatter.to_numpy()
    y_scatter = y_scatter.to_numpy()
    # define m and c for a line of best fit. the 1 means the highest exponent for x will be 1, giving a straight line.
    m, c = np.polyfit(x_scatter, y_scatter, 1)
    # create the scatter plot
    ax.scatter(x_scatter,y_scatter,) 
    # plot the line of best fit
    ax.plot(x_scatter, m*x_scatter +c, color = "hotpink")
    # label the axes
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    # give the plot a title
    ax.set_title(f"{x_axis} vs. {y_axis}")
     # save the scatter plot as a PNG file
    fig.savefig(f"{x_axis} vs. {y_axis}.png")
    # open the txt file from earlier in amend mode
    file = open("Variable Summary.txt", "a")
    # add correlation coefficient of x and y values
    file.write(f"\n\nThis is the correlation between {x_axis} and {y_axis}: \n\n{np.corrcoef(x_scatter, y_scatter)}")
    # close the txt file
    file.close()

# choose the variables to plot
variable1 = df["sepal_length"]
variable2 = df["sepal_width"]
# label the axes
x_axis = ("Sepal Length (cm)")
y_axis  = ("Sepal Width (cm)")
# call the scatter function
scatter = generate_scatter(variable1,variable2)

variable1 = df["petal_length"]
variable2 = df["petal_width"]
x_axis = ("Petal Length (cm)")
y_axis  = ("Petal Width (cm)")
scatter = generate_scatter(variable1,variable2)

variable1 = df["sepal_length"]
variable2 = df["petal_width"]
x_axis = ("Sepal Length (cm)")
y_axis  = ("Petal Width (cm)")
scatter = generate_scatter(variable1,variable2)

variable1 = df["petal_length"]
variable2 = df["sepal_width"]
x_axis = ("Petal Length (cm)")
y_axis  = ("Sepal Width (cm)")
scatter = generate_scatter(variable1,variable2)

variable1 = df["sepal_length"]
variable2 = df["petal_length"]
x_axis = ("Sepal Length (cm)")
y_axis  = ("Petal Length (cm)")
scatter = generate_scatter(variable1,variable2)

variable1 = df["petal_width"]
variable2 = df["sepal_width"]
x_axis = ("Petal Width (cm)")
y_axis  = ("Sepal Width (cm)")
scatter = generate_scatter(variable1,variable2)
