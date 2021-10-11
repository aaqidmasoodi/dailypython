def tower(disks, start, end, middle):
    if disks == 1:
        print(f'Move Disk from {start} to {end}') 
        return
    
    tower(disks-1, start, middle, end)
    print(f'Move Disk from {start} to {end}')
    tower(disks-1, middle, end, start)

## bitwise solution

tower(5,'A','C','B')
