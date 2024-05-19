# pands-project

## Discussion

The *Iris* dataset (also known as Fisher's Iris dataset) is a dataset made famous by Fisher in his paper *The uses of multiple measurements in taxonomic problems*, published in September 1936<sup>1</sup>. The dataset consists of 150 samples of iris flowers and records their species, sepal length and width, and petal length and width. Originally collected by Anderson for his 1936 discussion<sup>2</sup> of the species problem<sup>3</sup>, Fisher used the dataset to demonstrate linear discriminant analysis<sup>4</sup>.

Of the three species listed in the dataset, two had samples collected from the same colony (*Iris setosa* and *Iris veriscolor*), while samples of the third (*Iris virginia*) were collected from a different colony. Fisher notes in Section VI of his paper that this "might considerably disturb both the mean values and their variabilities".

## Code

The aim of the analysis.py program is to produce an analysis of the *Iris* dataset. Currently, the program performs four functions:
    - Summarises each variable and outputs this summary to a .txt file.
    - Creates a histogram for each variable and saves them as .png files.
    - Creates a scatter plot (with line of best fit) of each pair of variables and saves them as .png files.
    - Calculates the correlation coefficient for each pair of variables and adds this to the aforementioned .txt file.

### Required Software

The code for the analysis.py program is written in Python, meaning you'll need to have Python installed to run it. I've used [Anaconda](https://www.anaconda.com/download) as the installer, with [Visual Studio Code](https://code.visualstudio.com/) as the code editor, but you can use whatever you prefer. 

## References

1. *The uses of multiple measurements in taxonomic problems*, R. Fisher, 1936, *Annals of Eugenics*, Volume 2, Issue 7, pages 179-188 https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
1. *The species problem in Iris*, E. Anderson, 1936, *Annals of the Missouri Botanical Garden*, Volume 23, Issue 3, pages 457-469, 471-483, 485-501, 503-509 https://www.jstor.org/stable/2394164?origin=crossref%3Forigin%3Dcrossref&seq=1
1. *Introduction to the Species Problem*, F. E. Zachos, 2016, *Species Concepts in Biology* https://link.springer.com/chapter/10.1007/978-3-319-44966-1_1
1. *PCA versus LDA*, A. M. Martinez and A. C. Kak, 2001, *IEEE Transactions on Pattern Analysis and Machine Intelligence*, Volume 23, Issue 2, pages 228-233 https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=908974
1. https://archive.ics.uci.edu/dataset/53/iris (UCI Machine Learning Repository - Iris dataset)
1. https://www.w3schools.com/python/python_file_write.asp (how to have the program create a txt file)
1. https://flexiple.com/python/python-new-line (how to insert line breaks when writing to a txt file)
1. https://seaborn.pydata.org/generated/seaborn.heatmap.html (seaborn documentation on heatmaps)