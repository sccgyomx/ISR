from tkinter import *
from conexionMysql import *
from Usuario import *


class App():
    def __init__(self):
        self.base_datos = DataBase()
        self.usuario = Usuario()
        root = Tk()
        self.ventana = root
        self.dibujarFrames()
        self.dibujarLabels()
        self.dibujarBotones()
        root.title("Banco")
        root.resizable(0, 0)
        root.geometry("800x600")
        root.config(background="#314252")
        root.mainloop()

        self.nombre = StringVar()
        self.nombre.set("Pedro")

    def dibujarFrames(self):
        self.frame_titulo = Frame(self.ventana, background="#314252", height=100)
        self.frame_titulo.pack(fill="x")

        self.F_opciones = Frame(self.ventana, background="#714252", width=200, height=400)
        self.F_opciones.pack(side=LEFT, anchor=N)

        self.F_principal = Frame(self.ventana, background="#314252", height=400, width=600)
        self.F_principal.pack()

        self.mantenerFrameBtnA = Frame(self.F_opciones, background="#314252", width=200, height=100)
        self.mantenerFrameBtnA.pack()
        self.F_btnA = Frame(self.mantenerFrameBtnA, width=200, height=100)
        self.F_btnA.pack()

        self.mantenerFrameBtnC = Frame(self.F_opciones, background="#314252", width=200, height=100)
        self.mantenerFrameBtnC.pack()
        self.F_btnC = Frame(self.mantenerFrameBtnC, width=200, height=100)
        self.F_btnC.pack()

        self.mantenerFrameBtnR = Frame(self.F_opciones, background="#314252", width=200, height=100)
        self.mantenerFrameBtnR.pack()
        self.F_btnR = Frame(self.mantenerFrameBtnR, width=200, height=100)
        self.F_btnR.pack()

        self.mantenerFrameBtnS = Frame(self.F_opciones, background="#314252", width=200, height=100)
        self.mantenerFrameBtnS.pack()
        self.F_btnS = Frame(self.mantenerFrameBtnS, width=200, height=100)
        self.F_btnS.pack()

    def dibujarLabels(self):
        self.lbl_title = Label(self.frame_titulo, foreground="white", background="#314252", text="Banco",
                               font=("", 16)).place(x=340, y=30, width=120)
        self.lbl_bienbenida = Label(self.F_principal, foreground="white", background="#314252", text="BIENVENIDO",
                                    font=("", 16)).place(x=225, y=30, width=150)
        self.lbl_Nombre = Label(self.F_principal, foreground="white", background="#314252", text=self.nombre.get(),
                                font=("", 16)).place(x=225, y=60, width=150)

    def dibujarBotones(self):
        self.Btn_auth = Button(self.F_btnA, relief="flat", foreground="white", background="#0051c8",
                               text="Autenticar", command=lambda: self.frameAuth()).place(x=0, y=0, width=200,
                                                                                          height=100)
        self.Btn_consultar = Button(self.F_btnC, relief="flat", foreground="white", background="#0051c8",
                                    text="Consultar", command=lambda: self.frameConsultar()).place(x=0, y=0, width=200,
                                                                                                   height=100)
        self.Btn_retirar = Button(self.F_btnR, relief="flat", foreground="white", background="#0051c8",
                                  text="Retirar", command=lambda: self.frameRetiro()).place(x=0, y=0, width=200,
                                                                                            height=100)
        self.Btn_salir = Button(self.F_btnS, relief="flat", foreground="white", background="#0051c8",
                                text="Salir", command=lambda: self.salir()).place(x=0, y=0, width=200, height=100)

    def BorrarBoton(self, x):
        x.pack_forget()

    def ReDibujarBoton(self, x):
        x.pack()

    def frameAuth(self):
        #self.frame_Auth = Frame(self.F_principal, background="#414252", height=400, width=600)
        #self.frame_Auth.pack()
        #self.BorrarBoton(self.F_btnA)
        self.nombre.set("Juan")

    def frameConsultar(self):
        self.frame_Consultar = Frame(self.F_principal, background="#414252", height=400, width=600)
        self.frame_Consultar.pack()
        self.BorrarBoton(self.F_btnC)

    def frameRetiro(self):
        self.frame_Retiro = Frame(self.F_principal, background="#414252", height=400, width=600)
        self.frame_Retiro.pack()
        self.BorrarBoton(self.F_btnR)

    def salir(self):
        self.ventana.destroy()


aplicacion = App()
