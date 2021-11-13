
with open('story.txt', 'r') as f:
    content = f.read(10)

    while len(content) > 0:# boolean false
        print(content, end='')
        content = f.read(10) # update it

    # ceaser shift # encryption algorithm
