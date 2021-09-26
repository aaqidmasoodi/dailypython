'''Create a fucntion that accepts a list and search for an element
using linear search'''
# if '' in list
# return that element else return -1
'''do not create a list
(list, num)
return elemet
return -1
'''

def search(target_list, target_element):
    for element in target_list:
        if element == 8:
            return element
    return -1


# my_list = [5,[8], 'Dayim', 'Numair']

print(search(8, [5,3,7,9]))


# takes a list
# takes a number
