# is operator

# one case

my_list1 = [37, 27, 15, 100]
my_list2 = my_list1

print('CONTENTS OF LISTS')
print(my_list1)
print(my_list2)

print('ADDRESSES OF LISTS')
print(id(my_list1))
print(id(my_list2))

if my_list1 is my_list2: # whether these two are the same # checking whether ids are the same
    print('asdfs')