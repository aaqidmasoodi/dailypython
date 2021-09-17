# [] ->> lists
# () -->> tuple


# a simple thing
my_list = [1,2,4]
my_tup = (1,2,4)

print(type(my_list))
print(type(my_tup))

for id, item in enumerate(my_list):
    print(id, item, 'list')

for id, item in enumerate(my_tup):
    print(id, item, 'tup')
