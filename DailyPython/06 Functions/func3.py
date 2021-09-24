num_1 = 5



def add():
    global num_1
    num_1 = 15

    num_1 += 5
    num_1 *= 10
    print(f'Inside Function: {num_1}')
    

add()
print(num_1)