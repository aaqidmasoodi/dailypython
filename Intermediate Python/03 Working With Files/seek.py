myfile = open('story.txt', 'r')



for i in range(10):
    content = myfile.read(5) # reading like this has more control over what you are reading
    print(content, end='**')







myfile.close() # good practise
