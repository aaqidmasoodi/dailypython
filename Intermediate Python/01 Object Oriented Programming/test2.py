class Dog:


    def __init__(self,name, age):
        self.name = name
        self.age = age


    def __repr__(self):
        return f'Dog(\'{self.name}\',{self.age})'


    def __str__(self):
        return f'{self.name}'



    # Operator Overloading
    # change the default behavours of python buildins

    def __add__(self,other): # the left operand should be called self and the other should be called other
        return self.age + other.age


    def __sub__(self,other):
        return self.age - other.age


    def __len__(self):
        return len(self.name)


   


d1 = Dog('BurnoMars',2)
d2 = Dog('Tommy',5)



print(len(d1))  # __len__


print(dir(d1))


'''
__add__ (self, other)
__sub__ (self, other)
__mul__ (self, other)
__div__ (self, other)
__mod__ (self, other)
__divmod__ (self, other)
__pow__ (self, other[, modulo])
'''