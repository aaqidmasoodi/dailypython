class Employee:

    no_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.no_of_emps += 1
        


employee1 = Employee('Aaqid',100000)
employee2 = Employee('Kaisar',500000)
employee3 = Employee('Asif',65113)


employee3.no_of_emps = 15

print(employee1.no_of_emps)
print(employee2.no_of_emps)
print(employee3.no_of_emps)

print(employee1.__dict__)
print(employee2.__dict__)
print(employee3.__dict__)




