# try the combinations
def transform(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    return a, b, c



my_var = transform(5,2,7,84,95,84,95,84,654,'asdfa','asdfasdf', choice=94, asdf=54)
# print(type(my_var))
# print(my_var)


# unless you define *args, and **kwargs