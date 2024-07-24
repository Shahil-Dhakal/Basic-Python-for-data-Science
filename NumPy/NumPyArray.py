#Unlike lists, you can perform operations to each iteam of numpy array easily as shown below.
# Import numpy
import numpy as np
height_in = [45,25,85,85,45,45,65,98,85,42,78,89,68,69,91,23,64,47,89]
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)
# Print out np_height_in
print(np_height_in)
# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254 #performs this line of code to each iteams of array
# Print np_height_m
print(np_height_m)