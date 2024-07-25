# Import numpy
import numpy as np
# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[ :  , 0])
# Print out the mean of np_height_in
print(np.mean(np_height_in))
# Print out the median of np_height_in
print(np.median(np_height_in))

"""
An average height of 1586 inches, that doesn't sound right, does it? However, the median does not seem affected by the outliers: 
74 inches makes perfect sense. It's always a good idea to check both the median and the mean, to get an idea about the overall 
distribution of the entire dataset.
"""
"""
Because the mean and median are so far apart, you decide to complain to the MLB. 
They find the error and send the corrected data over to you. 
It's again available as a 2D NumPy array np_baseball, with three columns.
The Python script in the editor already includes code to print out informative messages with the different summary statistics 
and numpy is already loaded as np. Can you finish the job? np_baseball is available.
"""
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))
# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))
# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))