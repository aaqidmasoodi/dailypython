import numpy as np  # essentially provides your arrays in python        

# sys.getsizeof(arr)

arr = np.array([1,2,3], dtype='float64') # it will take one object 
# you should for the most part specify a data type

# attributes about numpy arrays are:
print(arr.nbytes) # 
print(arr.ndim) # 2 -->> 
print(arr.shape) # return the m*n (3,3)
print(arr.size) # how many element are there
print(arr.dtype)
print(arr.itemsize) # In Bytes

print(arr)