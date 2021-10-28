class Employee:

    # INIT - DUNDER INIT
    def __init__(self,name='',salary=0, time=0):
        self.name = name 
        self.salary = salary 


    # WHENEVER YOU CREATE CLASS:
    # ALWAYS DEFINE THESE THE METHODS
    # THESE ARE BOTH USE TO REPRESENT YOUR OBJECT AS A STRING

    def __repr__(self): # unambigous to other developer
        return f"Employee('{self.name}',{self.salary})"

    def __str__(self): # human readable
        return f'{self.name} | {self.salary}'


e1 = Employee('Aaqid',500000)
e2 = Employee('Kaisar',100000)
e3 = Employee('Aaqid',500000)

print(e1)
print(e2)


print(help('__str__')) # but always use help to see the prototype 

print(str(e1))
print(repr(e1))


