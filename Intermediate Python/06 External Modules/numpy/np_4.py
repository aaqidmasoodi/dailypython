# SOME OF THE USEFUL FUNCTIONS
import numpy as np

# zeros -->> returns an numpy.ndarray with all zero (floats)
# my_arr = np.zeros((9,9), dtype='int64') # what is shape?? (2,3) rows & column

# ones -->> return an numpy.ndarray with all once
# my_arr = np.ones((9,9))

# full and full like
matrix = np.array([[4,1,2,3],[4,8,16,3]])
# my_arr = np.full(matrix.shape, 1)
# my_arr = np.full_like(matrix, 5)

# random numbers
# my_arr = np.random.rand(9,9) # directly specify the shape # it is super duper userful

# --------------------------L,H -shape
# my_arr = np.random.randint(1,3, size=(3,3)) # this also works


# make a (2,3) array of ones and try to do some math on it
# overloading

# basic math operations do work!!!
print(matrix)


matrix += 2 # this is optimized

print(dir(matrix))
# numpy can work with any type of data as long all elements have the same

# try to multiply and add two matricies (check what is up with the shape of the matrcies)

# ShapeError
