class Employee:

    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self,name='',salary=0):
        name = name
        self.salary = salary
        Employee.no_of_emps += 1


    # make a method for updating the class variable raise_amount
    # def update_raise_amount(self, new_raise_amount):
    #     Employee.raise_amount = new_raise_amount

    @classmethod
    def update_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount


    def say_hello():
        return 'hello world'


emp1 = Employee('Aaqid',50000)
emp1.raise_amount = 2.2


print(emp1.raise_amount)

emp1.update_raise_amount(1.09)

print(emp1.raise_amount)

emp2 = Employee('Kaisar',100000)

print(emp2.raise_amount)


print(emp1.__dict__)
print(emp2.__dict__)

