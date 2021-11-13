with open('story.txt','r') as myfile: # MSWODI
    contents = myfile.read()
    print(myfile.closed)
    print(contents)

print(myfile.closed)
y = myfile.read() # closed




# open files -->> closing them happens automatically
# open connections to data
# qureries apis
