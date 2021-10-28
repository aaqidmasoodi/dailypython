class MyClass:
    def __init__(self,name,age):
        self.myname = name
        self.age = age


    def get_name(self):
        return self.myname


    def set_name(self,new_name):
        self.myname = new_name

    


myobj = MyClass('Aaqid',22)
myobj2 = MyClass('kaisar',20)


print(myobj2.get_name())
print(myobj.get_name())

# myobj2.set_name('Numair')
MyClass.set_name(myobj2, 'Numair')

print(myobj2.get_name())
print(myobj.get_name())

# creating classes and object
# class varibles
# class method, static, instance
# inheritance (polymophism)
#

