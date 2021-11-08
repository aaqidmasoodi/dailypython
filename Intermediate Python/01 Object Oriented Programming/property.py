class Employee:
    
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@company.com'





    def fullname(self):
        return f'{self.first} {self.last}'



    

e1 = Employee('Mateen','Alam')
e2 = Employee('Dayim', 'Shah')

print(e1.fullname)
print(e2.fullname)


e2.first = 'Aaqid'
print(e1.email) # FOR DEVELOPERS WHO WERE USING IT LIKE THIS 
print(e2.email) # THEY ARE DOOMED


print(e1.fullname())
print(e2.fullname())


print(e1.__dict__)
print(e2.__dict__)

