class Dog:

    # access specifer - python does not have access specifer
    def regular_method(self): # instances
        pass

    @classmethod # 
    def class_method(cls): # create object from files/csv/strings
        pass

    @staticmethod
    def say_hello(): # cannot modify instance
        return 'Hello World' # helpers 

# 
print(Dog.say_hello())


# Inheritance