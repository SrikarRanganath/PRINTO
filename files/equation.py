from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
 
# define the true objective function
def objective(x, a, b, c, d, e, f):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f
 
# load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
dataframe = read_csv(url, header=None)
data = dataframe.values
# choose the input and output variables
y = [5, 9, 9, 9, 14, 15, 20, 20, 20, 20, 22, 24, 28, 30, 39, 41, 44, 54, 54, 66, 74, 73, 83, 86, 91, 91, 98, 98, 102, 106, 107, 106, 109, 112, 112, 117, 117, 119, 117, 119, 121, 126, 127, 127, 127, 131, 131, 139, 142, 137, 139, 137, 147, 147, 153, 153, 153, 157, 158, 158, 158, 158, 163, 163, 165, 163, 163, 164, 168, 168, 168, 168, 173, 173, 173, 173, 178, 183, 178, 188, 178, 181, 182, 183, 185, 183, 185, 188, 194, 193, 193, 193, 198, 198, 198, 204, 204, 204, 209, 209, 209, 214, 213, 214, 214, 219, 219, 219, 220, 219, 224, 224, 224, 224, 229, 229, 233, 229, 234, 234, 236, 240, 242, 247, 249, 253, 255]


x = [0, 1, 2, 3, 5, 6, 13, 15, 16, 17, 20, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 43, 44, 45, 46, 50, 51, 54, 57, 58, 59, 60, 61, 64, 66, 67, 69, 70, 76, 78, 79, 80, 82, 83, 84, 90, 91, 96, 98, 99, 102, 103, 105, 110, 111, 114, 118, 119, 120, 121, 124, 126, 129, 130, 132, 134, 138, 139, 140, 149, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 164, 165, 166, 169, 173, 176, 177, 186, 189, 190, 197, 200, 202, 208, 210, 212, 213, 217, 219, 221, 222, 223, 229, 230, 231, 233, 237, 238, 239, 240, 241, 242, 243, 246, 247, 248, 249, 250, 251]


# curve fit
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b, c, d, e, f = popt
print(a," ",b," ",c," ",d," ",e," ",f)
# plot input vs output
pyplot.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, b, c, d, e, f)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()
