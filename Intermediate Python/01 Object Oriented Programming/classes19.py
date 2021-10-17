# Special Methods
class Employee:

    # INIT - DUNDER INIT
    def __init__(self,name='',salary=0, time=0):
        self.name = name 
        self.salary = salary 


    # IMPLEMENTED

    # CONVENTION

    def __repr__(self): # represenation for the developers # UNABIGIOUS # AS CONVENTION IT SHOULD BE ELABORATE
        return "Employee('{self.name}, {self.salary}')" # MORE ELABORABLE

    # def __str__(self): # human readble form of this object # HUMAN READBLE FORM
    #     return f'{self.name}'

# it first looks for repr -->> str -->> object address

e1 = Employee('Aaqid',50000)
print(e1) # if __str__ is defined or not
print(str(e1)) # if __str__ is defined or not

print(repr(e1)) # it sees if __repr__ is defined or not

# # print(str(e1)) # string represenation of object

# print(dir(e1))
print(repr(e1))

list1 = [1,5,3]

print(str(list1)) # string represtatin of this object

print(dir(list1))

l1 = '[1,2,3]'


print(str(l1))
print(repr(l1))

# HOW THEY DEVELOPES hAVE PRINTED IS IMPRO