# copying lists
list_1 = ['Numair', 'Aaqid', 'Dayim', 'Mateen']
list_2 = list_1.copy()


print(type(list_1))
print(type(list_2))
print("Priting the lists")
print(list_1)
print(list_2)

list_2[0] = 'Tabasum Maam'
print("Priting the lists again")
print(list_1)
print(list_2)
