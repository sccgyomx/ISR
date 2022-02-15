class Usuario:
    nombre = str
    contrasenia = str
    saldo = str

    def setNombre(self,nombre):
        self.nombre=nombre

    def setContrasenia(self,contrasenia):
        self.contrasenia=contrasenia

    def setSaldo(self,saldo):
        self.saldo=saldo

    def getNombre(self):
        return self.nombre

    def getContrasenia(self):
        return self.contrasenia

    def getSaldo(self):
        return self.saldo
