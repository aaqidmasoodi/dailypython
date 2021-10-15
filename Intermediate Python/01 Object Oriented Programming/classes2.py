class Developer:
    pass

# # x = 5
# x = int() # using a constructor
# print(x)
# # f = 3.5
# f = float()
# print(f)
# # l = []
# l = list()
# print(l)

dev1 = Developer()
dev2 = Developer()



# making attr for dev1 # instance
dev1.name = 'Aaqid'
dev1.age = 21
dev1.language = 'Python'

# making attr for dev2 # instance
dev2.name = 'Asif'
dev2.age = 21
dev2.language = 'C++'
dev2.region = 'J&K'

print(dev1.name)
print(dev1.age)
print(dev1.language)
# print(dev1.region)



print(dev2.name)
print(dev2.age)
print(dev2.language)
print(dev2.region)