def add(x = 0, y = 0):
    return x + y

def sub(x = 0, y = 0):
    return x - y

def mul(x = 0, y = 0):
    return x * y

def div(x = 0, y = 1):
    return x / y


print('Hello World')
print('Hello Tawqeer')

# print(__name__)

# writing tests
# show the usage
if __name__ == '__main__':
    x = add(5,3)
    print(x)