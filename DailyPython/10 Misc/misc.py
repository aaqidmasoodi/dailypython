# slicing & scope

# Regarding ---->> CERTIFICATION
# Module --> COREPYTHON


list1 = [1,2,3,4,5,6,7,8,9] # index --> string --> lists --> tuple
#                  ^   ^


# each element has two indicies

# print(list1[2:-3])

# print(list1[5])
# print(list1[-4])

# print(list1[-7:-9:-1]) # -->> step

# print(list1[-2:-4:-1]) # returns an empty list

# site_url = 'https://dailypythno.org'

# [start:end:step]
#        ^
#        | Exclusive

# domain = site_url[8:-4]

# domain = site_url[-5:9:-1]

# domain = site_url[-15:-4]

# print(list1[-1::-1])


site_url = 'https://dailypythno.org'

top_level_domin  = site_url[-4:]

print(top_level_domin)

# print(domain)
