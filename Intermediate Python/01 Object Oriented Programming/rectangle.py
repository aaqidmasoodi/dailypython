class Rectangle:

    def __init__(self, length=1, breadth=1):
        self.length = length
        self.breadth =  breadth


    def set_length(self, new_length):
        if new_length > 0:
            self.length = new_length

    def get_length(self):
        return self.length


    def set_breadth(self, new_breadth):
        if new_breadth > 0:
            self.breadth = new_breadth

    def get_breadth(self):
        return self.breadth


# my_rectangles = []

# for i in range(20):
#     my_rectangles.append(Rectangle())


# for i in range(20):
#     print(my_rectangles[i].get_length())

# print('+++')

# for my_rect in my_rectangles:
#     print(my_rect.get_length())

# print('+++')
# for rect in my_rectangles:
#     print(rect.get_length() * rect.get_breadth())
