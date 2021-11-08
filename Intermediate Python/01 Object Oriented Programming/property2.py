class Employee:
    
    def __init__(self,first,last):
        self.first = first
        self.last = last


    # PATCHING


    # Developer friendly code
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'


    # BEST PRACTICE
    @property
    def fullname(self):
        return f'{self.first} {self.last}' 


    @fullname.setter
    def fullname(self, new_value):
        
        first, last = new_value.split(' ')
        self.first = first
        self.last = last


    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None






e1 = Employee('kaisar', 'Sofi')
print(e1.first)
print(e1.last)
print(e1.email)
print(e1.fullname)
e1.fullname = 'Aaqid Masoodi' # is there a setter defined or not?
print(e1.fullname)


del e1.fullname