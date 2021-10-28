class Employee:

    raise_amt = 1.2 # class variables

    # this gets called when we create an object
    # a function that is called automattically by python
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f'{self.first_name}.{self.last_name}@gmail.com'
  
    @classmethod
    def create_from_str(cls, id_str):
        id_list = id_str.split('-')
 
        x = Employee(id_list[0],id_list[1],id_list[2])
        return x
        
e1 = Employee()

e1.create_from_str()