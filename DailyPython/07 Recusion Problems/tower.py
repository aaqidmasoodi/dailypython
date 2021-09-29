def tower(n, start, end, middle):
    if n == 1:
        print(f'Move Disk from {start} to {end}') 
    tower(n-1, start, middle, end)
    print(f'Move Disk from {start} to {end}')
    tower(n-1, middle, end, start)