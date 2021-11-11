try:
    myfile = open('story.txt','r')
    contents = myfile.read()
    print(contents)
    myfile.close()
except FileNotFoundError:
    print('This file does not exist or has been moved.')
except:
    print('Something Went')



