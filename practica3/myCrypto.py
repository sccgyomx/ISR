# RECURSO0S
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# CARGAR CLAVE
def cargar_clave(nombre,tipo):
    return RSA.import_key(open(nombre+"_clave_"+tipo+".pem", "rb").read())


# ESCRIBIR Y GUARDAR CLAVE
def genera_clave(nombre):
    clave = RSA.generate(2048)
    private_key = clave.export_key()
    with open(nombre + "_clave_privada.pem", "wb") as archivo_clave:
        archivo_clave.write(private_key)
        archivo_clave.close()

    public_key = clave.public_key().export_key()
    with open(nombre+"_clave_publica.pem", "wb") as archivo_clave:
        archivo_clave.write(public_key)
        archivo_clave.close()


# ENCRIPTAR datos
def crypt(datos, clave):
    cipher_rsa = PKCS1_OAEP.new(clave)
    encrypted_datos = cipher_rsa.encrypt(datos)
    return encrypted_datos

def decrypt(datos, clave):
    cipher_rsa = PKCS1_OAEP.new(clave)
    datos = cipher_rsa.decrypt(datos)
    return datos