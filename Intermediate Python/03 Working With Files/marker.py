myfile = open('testfile.txt', 'w')


#print(myfile.tell())

myfile.write('Universe')

myfile.seek(5,1) # check it out





# marker --- file Handle
myfile.write('World')




myfile.close()
# you must close the file
# or else you will run over the system's file descriptor
# there will be file leaks
