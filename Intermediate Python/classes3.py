class Developer:

    def __init__(self,name, age, language):
       self.name = name
       self.age = age
       self.language = language


    def get_name_lang(self):
        return f'{self.name} | {self.language}'


d1 = Developer('Aaqid',21,'Python')
d2 = Developer('Asif',21,'C++')

d2.likes = 'Football'


print(d1.__dict__)
print(d2.__dict__)

print(d1.get_name_lang())
# print(d2.get_name_lang())

# print(Developer.get_name_lang(d1))
# print(d1.get_name_lang())