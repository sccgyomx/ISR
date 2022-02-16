from tkinter import *
from tkinter import messagebox

from Controlador import *


def BorrarBoton(x):
    x.pack_forget()


def ReDibujarBoton(x):
    x.pack()


class App:
    def __init__(self):
        self.btn_auth_iniciar_sesion = None
        self.entryContrasenia = None
        self.lbl_Auth_contrasenia = None
        self.lbl_Auth_nombre = None
        self.entryNombre = None
        self.F_btnS = None
        self.mantenerFrameBtnS = None
        self.F_btnR = None
        self.mantenerFrameBtnR = None
        self.F_btnC = None
        self.mantenerFrameBtnC = None
        self.F_btnA = None
        self.mantenerFrameBtnA = None
        self.F_principal = None
        self.F_opciones = None
        self.frame_titulo = None
        self.frame_Auth = None
        self.frame_Retiro = None
        self.frame_Consultar = None
        self.Btn_salir = None
        self.Btn_retirar = None
        self.Btn_consultar = None
        self.Btn_auth = None
        self.lbl_Nombre = None
        self.lbl_bienbenida = None
        self.lbl_title = None

        self.controlador = Controlador()
        root = Tk()
        self.ventana = root

        self.nombre = StringVar()
        self.contrasenia = StringVar()

        self.dibujarFrames()
        self.dibujarLabels()
        self.dibujarBotones()

        root.title("Banco")
        root.resizable(not True, not True)
        root.geometry("800x600")
        root.config(background="#314252")
        root.mainloop()

    def dibujarFrames(self):
        self.frame_titulo = Frame(self.ventana, background="#314252", height=100)
        self.frame_titulo.pack(fill="x")

        self.F_opciones = Frame(self.ventana, background="#314252", width=200, height=400)
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
        self.lbl_title = Label(self.frame_titulo, foreground="white", background="#314252", text="Banco", font=("", 16))
        self.lbl_title.place(x=340, y=30, width=120)

        self.lbl_bienbenida = Label(self.F_principal, foreground="white", background="#314252", text="BIENVENIDO",
                                    font=("", 16))
        self.lbl_bienbenida.place(x=225, y=10, width=150)

        self.lbl_Nombre = Label(self.F_principal, foreground="white", background="#314252", textvariable=self.nombre,
                                font=("", 16))
        self.lbl_Nombre.place(x=225, y=60, width=150)

    def dibujarBotones(self):
        self.Btn_auth = Button(self.F_btnA, relief="flat", foreground="white", background="#0051c8", text="Autenticar",
                               command=lambda: self.frameAuth())
        self.Btn_auth.place(x=0, y=0, width=200, height=100)

        self.Btn_consultar = Button(self.F_btnC, relief="flat", foreground="white", background="#0051c8",
                                    text="Consultar", command=lambda: self.frameConsultar())
        self.Btn_consultar.place(x=0, y=0, width=200, height=100)

        self.Btn_retirar = Button(self.F_btnR, relief="flat", foreground="white", background="#0051c8", text="Retirar",
                                  command=lambda: self.frameRetiro())
        self.Btn_retirar.place(x=0, y=0, width=200, height=100)

        self.Btn_salir = Button(self.F_btnS, relief="flat", foreground="white", background="#0051c8", text="Salir",
                                command=lambda: self.salir())
        self.Btn_salir.place(x=0, y=0, width=200, height=100)

    def frameAuth(self):
        self.frame_Auth = Frame(self.F_principal, background="#314252", height=400, width=600)
        self.frame_Auth.pack(padx=100,pady=100)

        BorrarBoton(self.F_btnA)

        self.lbl_Auth_nombre = Label(self.frame_Auth, text="Nombre de usuario:  ", font=("", 12), background="#314252",
                                     foreground="white")
        self.lbl_Auth_nombre.place(x=0,y=30)

        self.entryNombre = Entry(self.frame_Auth, textvariable=self.nombre, width=100, font=("", 12))
        self.entryNombre.place(x=0,y=60)

        self.lbl_Auth_contrasenia = Label(self.frame_Auth, text="Contraseña:  ", font=("", 12), background="#314252",
                                     foreground="white")
        self.lbl_Auth_contrasenia.place(x=0,y=90)

        self.entryContrasenia = Entry(self.frame_Auth, textvariable=self.contrasenia, width=100, font=("", 12))
        self.entryContrasenia.place(x=0,y=120)

        self.btn_auth_iniciar_sesion = Button(self.frame_Auth, relief="flat", foreground="white", background="#0051c8", text="Iniciar Sesión", command= lambda : self.autenticar())
        self.btn_auth_iniciar_sesion.place(x=140,y=160)

    def autenticar(self):
        self.return_Auth = self.controlador.autenticar(self.nombre.get(),self.contrasenia.get())
        if (self.return_Auth==False):
            messagebox.showinfo("Error", "Datos incorrectos")
            self.nombre=""
            self.contrasenia=""
        else:
            self.nombre=self.return_Auth
            BorrarBoton(self.frame_Auth)


    def frameConsultar(self):
        self.frame_Consultar = Frame(self.F_principal, background="#414252", height=400, width=600)
        self.frame_Consultar.pack()
        BorrarBoton(self.F_btnC)

    def frameRetiro(self):
        self.frame_Retiro = Frame(self.F_principal, background="#414252", height=400, width=600)
        self.frame_Retiro.pack()
        BorrarBoton(self.F_btnR)

    def salir(self):
        self.ventana.destroy()


aplicacion = App()
