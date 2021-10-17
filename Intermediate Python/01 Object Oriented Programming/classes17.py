# bare with the naming
class A:
    def add(self):
        print('method in class A')


class B:
    # def add(self):
    #     print('method in class B')
    pass



class C:
    def add(self):
        print('method in class C')


class D(B,A,C):

    def add(self):
        A.add(self) # possible but not something you should do
        print('Gotcha!!')
    
# d1 = D()
# d1.add()
# # print(help(d1))
# print(D.__mro__)
# # d1.add()

d1 = D()
# print(D.__mro__)
d1.add()



# you can use all the function in the classes



