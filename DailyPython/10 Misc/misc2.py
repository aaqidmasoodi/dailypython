'''
SCOPE IN PYTHON

LEGB
LOCAL - ENCLOSING - GLOBAL - BUILIN
'''
# import builtins

# print(dir(builtins))
# x = 'g var'
# y = '100'

# __name__ = 5

# print(__name__)

# def my_fun():
#     # y = 'l var'

#     print(y)

# my_fun()
# print(x)


# list1 = [1,2,3,4,5,6,7,8,9]


# # def sum(a,b):
# #     return a + b

# print(sum(list1))


x = 'g var'
y = 'Aaqid'

def my_fun():
    global y
    y = 'l var'


    print(y)


my_fun()
print(x)
print(y)
