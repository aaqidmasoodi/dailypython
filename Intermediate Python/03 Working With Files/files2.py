myfile = open('story.txt','r') # overwriiten

contents = myfile.readlines()


for content in contents:
    print(content, end='')


print('Dayim\nMateen\nSidrat\nTawqeer\n')



myfile.close()
