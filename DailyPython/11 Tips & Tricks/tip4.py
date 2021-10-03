names = ['Sidrat','Aaqid','Dayim','Mateen','Numair','Kaiser']
semesters = ['2nd','7th','5th']
ages = [21,21,21,21,21,21]

# zip()
# for i, name in enumerate(names):
#     sem = semesters[i]
#     print(name, sem)

print('**********')
for name, sem, age in zip(names, semesters, ages): ### zip will only go upto ()
    print(name, sem, age)

# itertools
# ziplargest()