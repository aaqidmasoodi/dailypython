import rectangle


# DRY - DONT REPEAT YOURSELF

my_rects = []
measures = [(14,12),(5,9),(16,17),(6,8),(15,64),(14,12),(5,9),(16,17),(6,8),(15,64)]

for i in range(10):
    my_rects.append(rectangle.Rectangle())

index = 0
for rect in my_rects:
    x, y = measures[index]
    rect.set_length(x)
    rect.set_breadth(y)
    index += 1 

for index, rect in enumerate(my_rects):
    x, y = measures[index]
    rect.set_length(x)
    rect.set_breadth(y)
    index += 1 


for rect in my_rects:
    print(rect.get_length())


