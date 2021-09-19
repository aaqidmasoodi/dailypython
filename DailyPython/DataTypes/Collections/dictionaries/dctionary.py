student = {'name':'Aaqid', 'age':21, 'semester':'7th'}


# a key error will be generated
# we must not use this syntax because a 'not found' key would result in a error
# print(student['8'])

print(student.get('67')) # you this prebrably

# dictionaries are mutable
student['gender'] = 'male' # changing a value

student.update({'name':'Dayim', 'marks':95}) # parsed

# to revove elements
# pop()
# popitem()
# del 
# name = student.pop('sdfsf')
# print(name)
# student.popitem()

# del student['gender']

print(student)