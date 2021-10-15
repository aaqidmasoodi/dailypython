class Animal:
    def speak(self):
       return 'Animail is Speaking'


class Dog(Animal):
    def speak(self):
       return 'Dog is Speaking'
    pass


class Cat(Animal):
    pass



a1 = Animal()
print(a1.speak())

d1 = Dog()
print(d1.speak())

c1 = Cat()
print(c1.speak())