# the matrix multipication
import numpy as np


# multiplying matricies - do not use a loop
arr1 = np.array([[1,2,7], [4,5,7], [2,4,8]]) # shape ? 2 * 2

# 2 * n

# 2 * 2 --- 2 * 4

# arr2 = np.full_like(arr1, 6, dtype='int8')

arr2 = np.array([[1,5,8,4],
                 [3,5,5,6],
                 [2,4,5,8]
                ])

output = np.matmul(arr1, arr2)

print(output)