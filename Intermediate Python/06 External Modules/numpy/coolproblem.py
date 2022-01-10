import numpy as np


# rescaling an image without keeping the aspect 
#

# Given Matrix
mat1 = np.identity(6)
print(mat1)
        W     H
# must  3840 × 2160 

# 120
# 1
for i in range(mat1.shape[0]):
 for j in range(mat1.shape[1]):
  if i == j:
   mat1[i][j] *= 6


mat1*6

# # Given Matrix
# mat1 = np.array([[5,4,9],
#                  [2,4,4]])

# #                              always specify this
# output = np.zeros(mat1.shape, dtype='uint8')
# print(output+6)
# #
# output = np.ones(mat1.shape, dtype='int8')
# print(output*6)
# #


# WTHOUT KEEPING --->> DiSTORTION