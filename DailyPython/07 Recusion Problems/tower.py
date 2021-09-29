def tower(disks, start, end, middle):
    if disks == 1:
        print(f'Move Disk from {start} to {end}') 
    else:
        tower(disks-1, start, middle, end)
        print(f'Move Disk from {start} to {end}')
        tower(disks-1, middle, end, start)



tower(3,'A','C','B')