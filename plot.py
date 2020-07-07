#!/usr/bin/env python

import matplotlib.pyplot as plt


# Declaring the points for first line plot
X1 = [1,2,3,4,5]
Y1 = [2,4,6,8,10]

# Setting the figure size
fig = plt.figure(figsize=(10,5))

# plotting the first plot
plt.plot(X1, Y1, label = "plot 1")

# Declaring the points for second line plot
X2 = [1,2,3,4,5]
Y2 = [1,4,9,16,25]

# plotting the second plot
plt.plot(X2, Y2, label = "plot 2")

# Labeling the X-axis
plt.xlabel('X-axis')

# Labeling the Y-axis
plt.ylabel('Y-axis')

# Give a title to the graph
plt.title('Two plots on the same graph')

# Show a legend on the plot
plt.legend()

#Saving the plot as an image
fig.savefig('line plotoriginal.jpg', bbox_inches='tight', dpi=150)

#Showing the plot
#plt.show()
