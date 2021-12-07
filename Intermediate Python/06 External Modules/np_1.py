import numpy as np


arr1 = np.array([1,2,3,4,5]) 

# Accessing/Modifying Elements
# start:end:step
print(arr1[0:])

# run a loop from 0 to the size of the array
print(len(arr1))
print(arr1.size) # will only work in arrays

[1,2,3] # 1 millions times i have get


# make a numpy array and iterate over 
# using a for in loop and for in range()

# this is possible
for num in arr1:
    print(num)

# this is also possible
for i in range(arr1.size):
    print(arr1[i])

arr1[2] = 4

for num in arr1:
    print(num)