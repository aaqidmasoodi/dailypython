# this is all you'll need.
import os


# Change Directory (Folder)
os.chdir('/home/neo/Documents/Workshop/dailypython/Intermediate Python')

# get Current working Directory
print(os.getcwd()) # -> returns a path

# list all the directories
print(os.listdir()) # -->> you can also give a path


os.mkdir('myfoldernew') # creates a single folder
os.makedirs('newfolder/myfold/myfold3') # creates an entire directory tree


os.rmdir() # -->> remove a single empty directory
os.removemdirs() # -->> remove an entire directory tree
# you can only remove empty dirs


# stuxnet
# computer worm
# TO READ

# generate a file path
mypath = os.getcwd() + '/Intermediate Python/04 BuildIn Modules'

os.chdir(mypath)

# this file will always be created in the current working dir
with open('newfile.txt', 'w') as f:
    pass


os.rename('newfile.txt', 'renamed.txt') # rename files



# walk an entire directory structure
# from top dir



for dirpath, dirnames, filenames in os.walk(os.getcwd()): # traverse a tree structure
    print(f'DIR_PATHS: {dirpath}')
    print(f'DIR_NAMES: {dirnames}')
    print(f'FILE_NAMES: {filenames}')



# this has a problem
# we cannot hard code paths
mypath = os.getcwd() + '/Intermediate Python/04 BuildIn Modules'

# concatinate two file path irrespective of the os
print(os.path.join(os.getcwd(), 'newfolder')) # works for all systems

# better way
mypath = os.path.join(os.getcwd() + 'subfolder')
os.chdir(mypath)


# os.path has more functions
# isfile
# isdir


print(os.path.isfile('renamed.txt')) # -->> returns true or false
print(os.path.isdir('myfold')) # -->> returns true or false



mypath = '/home/neo/html/something.txt'

# return the lead
print(os.path.basename(mypath))

# returns the dir
print(os.path.dirname(mypath))


# spliting the extentions
filepath, ext = os.path.splitext(mypath)
print(ext)


# exists
print(os.path.exists('./something'))


print(os.environ.get('MYOWNVAR')) # very very useful
# it is python dict that keepng record of all env variables on the variable



os.system() # execute raw command
# it will be system specific

os.remove() # -->> remove all files 




# target system -->> DESKTOP --> Myfolder
# DO NOT HARD CODE PATH
# TRY THIS SIMPLE PROJECT USING PYTHON"S OS MODULE
# make a folder
# put files and folders into 
# copy all files (not folders) into another folder
# INTRODUCTION TO MALWARE