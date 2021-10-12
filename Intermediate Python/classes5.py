class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.no_of_obj = 0


    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary




    # def __str__(self):
    #     return f'Employee: {self.name}'


emp1 = Employee('Aaqid',100000)
emp2 = Employee('Asif',50000)

print(emp1.get_salary())
print(emp2.get_salary())


# Employee.get_salary(emp1)

# emp2.set_salary(5000)

# print(emp1.get_salary())
# print(emp2.get_salary())

Employee.set_salary(emp1, 6000) # you will not use it
emp1.set_salary(12000) # auto passing of instance


print(emp1.get_salary())
print(emp2.get_salary())


# FACTORY
