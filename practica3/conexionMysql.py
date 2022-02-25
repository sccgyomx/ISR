import pymysql


class DataBase:

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='toor',
            db='cajero'
        )
        self.cursor = self.conn.cursor()

    def insertar(self,username,passwd,passwdCryp):
        sql = """insert into users (username,passwd,passwdCryp) values (%s,%s,%s)"""
        self.cursor.execute(sql,(username,passwd,passwdCryp))
        self.conn.commit()

    def mostrar(self):
        sql = "select * from users"
        self.cursor.execute(sql)
        users = self.cursor.fetchall()
        return users

    def actualizar(self,nombre,nuevo_nombre):
        sql ="update users set username = '{}' where username = '{}'".format(nuevo_nombre,nombre)
        self.cursor.execute(sql)
        self.conn.commit()


    def buscar(self,nombre):
        sql =  "SELECT * FROM users WHERE username =%s"
        self.cursor.execute(sql,nombre)
        users = self.cursor.fetchall()
        return users
