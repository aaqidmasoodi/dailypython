import numpy as np


testarr = np.array([
 [5,6,7,8,9,1],
 [6,3,4,8,7,2],
 [8,7,3,4,6,4],
 [5,7,3,9,7,5]
])

# replace [4,8,7],[3,4,6]
# multiply all number < 4 by 8
# multiply number greater or equal to 6 by 2
# create a new numpy array of numbers less than 3
# -------------list
# print(testarr[[1,2], 2:5])

# testarr[[1,2], 2:5] = [
#  [6,5,6],
#  [6,8,4]
# ]

# print(testarr)

testarr[testarr < 4] *= 8

between_2_5 = (testarr >= 2) & (testarr <= 5)

print(testarr[between_2_5])