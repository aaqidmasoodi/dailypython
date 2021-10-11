names = ['Aaqid', 'Dayim', 'Numair', 'Tawqeer', 'Mateen', 'Sidrat']

# Print upto somthing
for name in names:
    if name == 'Tawqeer':
        break
    print(name)

# whenever continue is encoutered, it skips to next iteration
for name in names:
   
    if name == 'Tawqeer':
        continue
    print(name)