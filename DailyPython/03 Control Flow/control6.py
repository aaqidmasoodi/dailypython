list1 = [1,2,3]
list2 = list1

list2[0] = 8

print(list2)

if list1 is list2:
    print('Same Object')