# any

# any() # -->> any element in a iterable is True


list1 = [1,0,5,6]
list2 = ["",True,2<3]
list3 = ["Aaqid","Kaiser","Mateen","Dayim"]
list4 = ['',0,{},[],5>12,5]


print(any(list4)) # whether there is a true value in an iterable | OR

mark1 = 15
mark2 = 95
mark3 = 12
mark4 = 16
'''
.
.
.
.
'''

checks = [
    mark1 > 18, 
    mark2 > 13, 
    mark3 > 10, 
    mark4 > 5
]

if any(checks):
    print('Hello World')
