class Employee:

    # there are no access modifiers whatso ever

    # best practices
    def __init__(self,name='',salary=0, time=0):
        self.name = name # public
        self._salary = salary # protected
        self.__time = time # name mangling # private #
        # print(self.__time) 




e1 = Employee('Aaqid',500000,315)

print(e1.name)
print(e1._salary)
# print(e1._Employee__time)

print(dir(e1))
       