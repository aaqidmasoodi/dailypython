f = open('story.txt', 'r')

content = f.read(10)

while len(content) > 0:# boolean false
    print(content, end='')
    content = f.read(10) # update it

# ceaser shift # encryption algorithm
f.close()
