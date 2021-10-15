class User:
    
    no_of_user = 0


    def __init__(self,username, password, type):
        self.username = username
        self.__password = password
        self.type = type
        self.__is_admin = False


    def __set_admin_privileges(self):
        self.__is_admin = True

    def __change_password(self, new_password):
        self.__password = new_password

    def get_username(self):
        return self.username


    def __get_password(self):
        return self.__password



class Student(User):

    def __init__(self,username, password, type, semester):
        super().__init__(username, password, type)
        self.semester = semester




s1 = Student('mateen','1234','student')

print(s1.username)