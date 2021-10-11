def generate_merit(sub1,sub2,sub3):
    if sub1 > 95 and sub2 > 95 and sub3 > 95:
        print(sub1)
        print(sub2)
        print(sub3)
        return True
    else:
        return False

# positional Arguments
# generate_merit(96,5,96)


# keywords arguments
# generate_merit(sub2=96, sub1=97, sub3=97)

# generate_merit(sub3=94, 24, 36)

# generate_merit(21,sub1=94, sub2=94)

# generate_merit(21, sub3=95, 64)

