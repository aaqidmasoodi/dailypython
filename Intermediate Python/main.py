import rectangle


# DRY - DONT REPEAT YOURSELF

my_rects = []

for i in range(10):
    my_rects.append(rectangle.Rectangle())

for rect in my_rects:
    rect.set_length(5)
    rect.set_breadth(7)

for rect in my_rects:
    print(rect.get_length())


