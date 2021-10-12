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

r1 = Rectangle()

print(f'Area of r1 = {r1.get_length() * r1.get_breadth()}')


print(r1)