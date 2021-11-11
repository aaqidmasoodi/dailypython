myfile = open('testfile.txt', 'w')


myfile.tell()

myfile.write('AaqidMasoodi')
print(myfile.tell())
myfile.seek(0)
myfile.write('YO') # overwrite whatever it needs to overwrite
print(myfile.tell())





myfile.close()
