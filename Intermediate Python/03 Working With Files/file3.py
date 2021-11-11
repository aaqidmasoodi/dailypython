f = open('story.txt', 'r')

for i in range(5):
    content = f.readline() # will not read the entire file
    print(content)

f.close()
