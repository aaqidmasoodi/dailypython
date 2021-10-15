# User()

class User:

    users = 0
    all = []

    def __init__(self, username='', password=''):
        self._username = username
        self.__password = password
        User.users += 1
        User.all.append(self) # common practice



    def _get_password(self):
        return self.__password


    def _update_username(self, new_username):
        self._username = new_username

u1 = User('aaqidmasoodi','pass123')