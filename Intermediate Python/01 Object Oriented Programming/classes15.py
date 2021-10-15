# simple inheritance

# multi level -->> 
# multiple -->>
class Employee:

    raise_amount = 1.04

    def __init__(self,name='',salary=0):
        self.name = name
        self.salary = salary


    def get_name(self):
        return self.name


    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        
class Developer(Employee): # inherit

    raise_amount = 1.5

    def __init__(self,name='',salary=0, language=''): # this cannot be avoided
        # Employee.__init__(self, name, salary) # hard coding
        super().__init__(name,salary) # best practice
        self.language = language
    


class Pion(Employee):

    def __init__(self,name='',salary=0, rooms=None):
        super().__init__(name,salary)
        self.rooms = rooms


e1 = Employee('Kaisar',50000)
d1 = Developer('Mateen',10000,'Python') # you'll see a lot happening



p1 = Pion('Abdul',5000,['A','B','U'])


print(p1.__dict__)

# d1.raise_amount = 1.8

# d1.apply_raise()

# print(d1.__dict__)
# print(d1.salary)
print(d1.language)

print(d1.__dict__)