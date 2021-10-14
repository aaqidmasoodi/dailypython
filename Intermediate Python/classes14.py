class User:

    users = 0
    all = []


    def __init__(self, username='', password=''):
        self._username = username
        self.__password = password
        User.users += 1
        User.all.append(self) # considered a good practise



    def _get_password(self):
        return self.__password


    def _update_username(self, new_username):
        self._username = new_username


# u1 = User()
# u2 = User()
# u3 = User()
# u4 = User()
# u5 = User()


# print(User.all)

# enimes = []

# for i in range(15):
#     enimes.append(Enimy())


# for enimy in enimes:
#     #
#     ##
    #
    #
    #