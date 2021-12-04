import numpy as np  # essentially provides your arrays in python        

# sys.getsizeof(arr)

arr = np.array([[1,2,3],
 [4,5,6],
 [7,8,9]], dtype='int8') # it will take one object

# dtype options for int
# int8
# int16
# int32
# int64


# 3*3

[[1,2,3],
 [4,5,6],
 [7,8,9]]

# three attributes about numpy arrays are:
print(arr.nbytes) # 
print(arr.ndim) # 2 -->> 
print(arr.shape) # return the m*n (3,3)
print(arr.size) # how many element are there