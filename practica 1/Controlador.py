from conexionMysql import *

class Controlador:

    def __init__(self):
        self.data_base = DataBase()

    def autenticar(self,username,passwd):
        self.users = self.data_base.buscar(username)
        if(len(self.users)>0):
            for user in self.users:
                if (user[2]==passwd and user[1]==username):
                    return user[1]
            return False
        else:
            return False