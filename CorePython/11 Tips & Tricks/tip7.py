# all


list1 = [1,0,5,6]
list2 = ["",True,True]
list3 = ["Aaqid","Kaiser","Mateen","Dayim"]
list4 = ['',0,{},[]]



mark1 = 50
mark2 = 25
mark3 = 13
mark4 = 0

checks = [
    mark1 > 18, 
    mark2 > 13, 
    mark3 > 10, 
    mark4 > 5,
]

if all(checks):
    print('Hello World')