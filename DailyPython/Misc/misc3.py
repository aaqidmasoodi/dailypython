x = 'global var'


def outer():
    global x
    x = 'outer var'


    def inner():
        
        # nonlocal -->> will give access to enclosing scope

        x = 'inner var'

        print(x)
    inner()
    print(x)

outer()
print(x)
    