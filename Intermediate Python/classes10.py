class Dog:


    def regular_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def say_hello(): # cannot modify instance
        return 'Hello World' # helpers 


d1 = Dog()

print(d1.say_hello())
# print(Dog.say_hello()) 


# Inheritance