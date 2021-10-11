class Employee:

    no_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.no_of_emps += 1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


employee1 = Employee('Aaqid',100000)
employee2 = Employee('Kaisar',500000)

print(employee1.salary)
print(employee2.salary)

employee2.raise_amount = 1.08
employee1.apply_raise()
employee2.apply_raise()

print(employee1.salary)
print(employee2.salary)


print(employee1.__dict__)