class Item:

    def __init__(self, item_name='', quantity=1):
        self._name = item_name
        self.__quantity = quantity

    def set_quantity(self, new_quantity): # setter
        self.__quantity = new_quantity


    def __private_method(self):
        pass

i1 = Item('Juice',1)

# print(i1.__quantity)
print(i1._Item__private_method())
# print(dir(i1))


