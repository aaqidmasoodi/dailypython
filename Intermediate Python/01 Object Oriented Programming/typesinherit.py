class Animal:
    def __init__(self):
        print('Animal Class Init')


class Dog(Animal):

    pass

    
class GermanShepherd(Dog):

    def __init__(self):
        super().__init__() # it is again lookup
        print('Using its init')
    


# super() returns a a super object -->> points to the parent class

g1 = GermanShepherd()



print(help(g1))




