from conexionMysql import *
import Crypto

class Controlador:

    def __init__(self):
        self.data_base = DataBase()

    def autenticar(self,username,passwd):
        self.users = self.data_base.buscar(username)
        if(len(self.users)>0):
            for user in self.users:
                if user[1] == username:
                    clave = Crypto.cargar_clave(user[1])
                    passwd_decryp = Crypto.decrypt(bytes(user[3],'UTF-8'),clave).decode()
                    if passwd == passwd_decryp:
                        return user
            return False
        else:
            return False

    def insertar(self,username,passwd):
        Crypto.genera_clave(username)

        clave = Crypto.cargar_clave(username)

        passwdCryp = Crypto.crypt(bytes(passwd, 'UTF-8'), clave).decode()

        self.data_base.insertar(username, passwd, passwdCryp)