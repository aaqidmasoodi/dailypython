# split - join
courses = ['Physics', 'Math', 'Geography']
# two sets of problems
# one - making a list from string
# eg : 'F-01-M-AAQID' ->> ['F', 01, 'M', 'AAQID']
# split
# second
# making a string from list
# join

string_list = ', '.join(courses) # '' separator
print(string_list)

print(f'Here are the course that you enrolled in:')
print(string_list)

# best is to use python docs

my_list = string_list.split(', ')
print(f'NEWLY CREATED LIST: {my_list}')

