# isinstance
# insubclass

# print(help('isinstance'))

class Animal:
    pass

class Dog(Animal):
    pass

class GermanShepherd(Dog):
    pass


class Cat:
    pass


a1 = Animal()
d1 = Dog()

c1 = Cat()

g1 = GermanShepherd()

print(isinstance(a1, Dog)) # dog is an animal # a polymorphism example
print(isinstance(a1, Animal))
print(isinstance(g1, Dog))
print(isinstance(g1, Animal))


def allow_if_dog(obj):
    if isinstance(obj, Dog):
        return True
    
    return False


# Read Java or C++ # polymophism
# create a vechicle array

# Polymophism 