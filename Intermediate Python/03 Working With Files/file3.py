with open('story.txt', 'r') as f:
    contents = f.readlines()
    contents.append('Hello World')
    print(contents)

