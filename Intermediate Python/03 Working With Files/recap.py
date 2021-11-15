# open() functions -->> builtin
# open('filename.ext','mode') -->> make it verbose
# files -->> do provide the extention
# mode -->> access mode
# r ->> read
# w ->> write
# a ->> append
# r+ ->> read/write
# wb ->> write binary
# rb ->> read binary



# r -->> if file does not exist --->> will through an error

# .read() -->> to read the enitre file
# .readlines() --->> list of lines
# .readline() --->> reads the next line in the file

# w -->> it overwrite the file
#    --->> it will create the file


# .write() -->> write a string to a file
# .close()


# marker --->> file handle
# .tell() --->> get the location of the pointer
# .seek() -->> change the position of the marker

#.seek(offset, from_where) -->> 0,1 --->> from_what default to the start of the file 0
             #0,1,2


             # 0 -->> from start of file
             # 1 -->> current location
             # 2 -->> end of file
#seek(0)

# context manager -->> with obj as something:
with open('filename', 'mode') as f:
    # your code here


# a -->> MODE -->> add to the file without clearing it
