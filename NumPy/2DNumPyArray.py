# Import numpy
import numpy as np
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)

"""
Subsetting 2D NumPy Arrays
If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.
# numpy
import numpy as np
np_x = np.array(x)
np_x[:, 0]
The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.
"""

# Import numpy package
import numpy as np
# Create np_baseball (2 cols)
np_baseball = np.array(baseball)
# Print out the 50th row of np_baseball
print(np_baseball[ 49 , : ])
# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[ : , 1 ]

# Print out height of 124th player
print(np_baseball[123, 0])

"""
---------2D ARITHMETIC----------
2D numpy arrays can perform calculations element by element, like numpy arrays.
np_baseball is coded for you; it's again a 2D numpy array with 3 columns representing height (in inches), weight (in pounds) and age (in years). baseball is available as a regular list of lists and updated is available as 2D numpy array.
"""

# Import numpy package
import numpy as np
# Create np_baseball (3 cols)
np_baseball = np.array(baseball)
# Print out addition of np_baseball and updated
print(np_baseball + updated)
# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])
# Print out product of np_baseball and conversion
print(np_baseball * conversion)