from conexionMysql import *

class Controlador:

    def __init__(self):
        self.data_base = DataBase()

    def autenticar(self,username,passwd):
        print(username)
        print(passwd)
        self.user = self.data_base.buscar(username)
        if(len(self.user)>0):
            print(self.user[0])
            return self.user[0][1]
        else:
            return False