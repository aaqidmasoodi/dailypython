with open('target.txt', 'r+') as mf:
    # the marker is at the S

    #mf.seek(0,2) # i want to go at the end of the file
    mf.seek(5) #--->>> but you should explore it more

    mf.write('Hello')
