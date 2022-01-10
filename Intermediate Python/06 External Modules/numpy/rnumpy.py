import numpy as np


# initilizing different types of numpy arrays
# there are some functions in numpy
# helpers

# NEVER EVER EVER EVER HARD CODE VALUES UNLESS YOU NEED TO 

mat1 = np.array([[5,4,9],
                 [2,4,4]])
print(mat1.shape)

# zeros
myarr = np.zeros((500,500), dtype='int64')
# it inits the array will all zeros

myarr = np.ones((5,5), dtype='uint8')


myarr = np.full(mat1.shape, 6, dtype='int8') # what is happening here?


myarr = np.full_like(mat1, 6,  dtype='int8')

[[6,6,6],
[6,6,6]]

print(myarr)


# Without the use of full or full like 


# CREATE ARRAYS
# WORKING WITH ARRAYS
# INIT DIFFERENT TYPES 
# ARRAY MATH 
# LINEAR MATH - 3 functions - 100s when ? 
# REORGANIZATION (INDEX)
# BOOLEAN MASKING <- real deal!!