# classes and Instances (objects)
# class variables
# instance, class and static methods



# inheritance __single, (__multi_level, __multiple) # beware of overrding stuff accidently!
# special method __init__, __str__ , __repr__

# PASCAL CASING -->>> NameTwo
# nameTwo -->> camel casing
class Employee:

    raise_amt = 1.2 # class variables

    # this gets called when we create an object
    # a function that is called automattically by python
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f'{self.first_name}.{self.last_name}@gmail.com'
        

    # # INSTANCE
    # def apply_raise(self):
    #     self.pay = self.pay * self.raise_amt


    # def change_raise_amt(self, new_raise_amt): # CAN IT CHANGE?
    #     self.raise_amt = new_raise_amt # this is also hard coded
    #     print(self)



    # # INDUSTRY STANDARD WAY OF DOING IT
    # @staticmethod
    # # you will usually use these methods to make static calls
    # def say_hello(object):
    #     object.first_name = 'Hi'
        

    # @staticmethod
    def change_params(var1):
        var1.first_name = 'Kaisar'


    # GOOD JOB




# 
e1 = Employee('Aaqid','Masoodi',500000)
e2 = Employee('emp2','lstname',532210)



e1.change_params()



print(e1.first_name)
print(e2.first_name)



# ABSURD AGREED