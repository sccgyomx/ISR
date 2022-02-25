from conexionMysql import *
import myCrypto
import binascii

class Controlador:

    def __init__(self):
        self.data_base = DataBase()

    def autenticar(self,username,passwd):
        self.users = self.data_base.buscar(username)
        if(len(self.users)>0):
            for user in self.users:
                if user[1] == username:
                    clave = myCrypto.cargar_clave(user[1],"privada")
                    passwd_decryp = myCrypto.decrypt(binascii.unhexlify(user[3]),clave).decode()
                    if passwd == passwd_decryp:
                        return user
            return False
        else:
            return False

    def insertar(self,username,passwd):
        myCrypto.genera_clave(username)

        clave = myCrypto.cargar_clave(username,"publica")

        passwdCryp = myCrypto.crypt(passwd.encode(), clave)
        passwdCryp = binascii.hexlify(passwdCryp).decode()
        self.data_base.insertar(username, passwd, passwdCryp)