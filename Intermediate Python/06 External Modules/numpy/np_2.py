import numpy as np


arr = np.array([1,2,3,4,5,6])

# you have of n elements
# you create a new array of 2n
# you copy elements of old array in the new array

# numpy arrays will throw an index error
# arr[5]

# this is also possible in numpy
arr[1:4] = [5,5,5]


print(dir(arr))