import numpy as np

# testarr = np.array([
#  [5,6,7,8,9,1],
#  [6,3,4,8,7,2],
#  [8,7,3,4,6,4],
#  [5,7,3,9,7,5]
# ])

# [
#  [6,3],
#  [8,7]
# ]
# ------------------*---*-----*
testarr = np.array([4,8,2,3,4,9])

print(testarr)
# [True, False, False, False, True, True]

# print(testarr[[True, False, False, False, True, True]])

# print(testarr > 5)

print(testarr[testarr > 5])

# print(testarr[[0,2,-1]])

# > < != ==
# return boolean masks

# range 
# list
# mix
# ------------range, range

# BOOLEAN MASK

# print(testarr[[1,2],[2,3]])

