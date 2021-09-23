name = "Dawood"
age = 20

# Hi Dawwood you are 20 years old
# 4  different ways of doing this

# Method 1
print("Hi",name,"You are",age,"years old.")

# Methord 2
# concat + (two strings you can join)
# casting
print("Hi "+name+" you are "+str(age)+" years old")

# Methord 3
print("Hi {} you are {} years old".format(name,age))

# Method 4
# personal preference
print(f"Hi {name} you are {age} years old.")
# this will only work in python 3.6 and above


