import os
import numpy as np

sales_data = np.genfromtxt('./sales_data.txt', dtype='int32', delimiter=',')

# TIP OF THE DAY

# it is used to whether or not all or any values are truthy in a numpy array
print(np.all(sales_data, axis=1))



# can you in a numpy make all the values 0 which are greater than lets say 150
