import numpy as np


arr = np.identity(4, dtype='int8')

# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

det_arr = np.linalg.det(arr)

print(dir(np))

# if you know what a matrix dot product is you can do these operations as well
# np.dot()

# https://numpy.org/doc/stable/reference/routines.linalg.html

# print(det_arr)

# print(dir(arr))
# print(arr)