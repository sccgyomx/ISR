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

    def insertar(self,username,passwd):
        sql = """insert into users (username,passwd) values (%s,%s)"""
        self.cursor.execute(sql,(username,passwd))
        self.conn.commit()
        print("ingresado correctamente")

    def mostrar(self):
        sql = "select * from users"
        self.cursor.execute(sql)
        users = self.cursor.fetchall()
        for user in users:
            print("Nombre de usuario: ", user[1])

    def actualizar(self,nombre,nuevo_nombre):
        sql ="update users set username = '{}' where username = '{}'".format(nuevo_nombre,nombre)
        self.cursor.execute(sql)
        self.conn.commit()
