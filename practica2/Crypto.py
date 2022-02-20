# RECURSO0S
from cryptography.fernet import Fernet


# CARGAR CLAVE
def cargar_clave(nombre):
    return open(nombre+"clave.key", "rb").read()


# ESCRIBIR Y GUARDAR CLAVE
def genera_clave(nombre):
    clave = Fernet.generate_key()
    with open(nombre+"clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)


# ENCRIPTAR datos
def crypt(datos, clave):
    f = Fernet(clave)
    return f.encrypt(datos)

def decrypt(datos, clave):
    f = Fernet(clave)
    return f.decrypt(datos)