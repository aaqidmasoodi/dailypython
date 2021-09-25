# create a function
# which has one default paramter
# it returns parater * 9

# alternatively the progerammer can override this value


def my_fun(default_val = 5):
    return default_val * 9


x = my_fun(98)
print(x)

# will be dicussed later
# *args --> it can accept arbitary number of positional arguments
# **kwargs -->> accept arbitary number of keywords