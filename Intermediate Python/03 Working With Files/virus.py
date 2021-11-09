import os

i = 0
while i < 100:
    f'touch filename{i}'
    os.system(f'touch filename{i}')
    i+=1