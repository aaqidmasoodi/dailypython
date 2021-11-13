#org = open('target.txt', 'r')
#cpy = open('target_copy.txt', 'w')


#contents = org.read()

#cpy.write(contents)


#org.close()
#cpy.close()

with open('target.txt', 'r') as org:
    with open('new_target.txt', 'w') as cpy:
        org_content = org.read()
        cpy.write(org_content)
