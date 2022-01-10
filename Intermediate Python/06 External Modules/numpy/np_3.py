import numpy as np

# matrix multiplication
# inputs * weight + bias
# some of the important functions
# ask user for 5 numbers and save it inside a numpy array then print it

user_input = np.array([0,0,0,0,0])
numbers = int(input('How many numbers? '))

for i in range(numbers):
    num = int(input(f'Enter Number {i+1}: '))
    user_input[i] = num

print(user_input) # __str__
