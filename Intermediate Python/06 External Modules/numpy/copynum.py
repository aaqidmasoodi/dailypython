import numpy as np

# BE SUPER CAREFUL WHILE YOU ARE TRING TO COPY ARRAY OBJECTS

arr = np.array([1,2,3])


arr2 = arr.copy()


print(id(arr))
print(id(arr2))