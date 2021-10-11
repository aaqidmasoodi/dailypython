num_1 = 'Umer'
num_2 = 4


def add():
    # using a global scope
    
    own_varible = num_1
    # you can read a varible from outside the functions
    # print(num_1)
    # print(num_2)
    
    print(f'inside function: {own_varible}')

add()
print(num_1)


