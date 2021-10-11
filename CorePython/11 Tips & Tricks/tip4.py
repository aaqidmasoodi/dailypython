names = ['Sidrat','Aaqid','Dayim','Mateen','Numair','Kaiser','Shugufta']
semesters = ['2nd','7th','5th']



# mega jugaad
# for i, name in enumerate(names):
#     sem = semesters[i]
#     print(name, sem)

for name, sem in zip(names, semesters):
    print(name, sem)


# itertools
# zip_longest