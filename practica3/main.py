from tkinter import *
from tkinter import messagebox
from ventanas import *

from Controlador import *


def BorrarElemento(x):
    x.pack_forget()


def ReDibujarElemento(x):
    x.pack()


class App:
    def __init__(self):

        self.Btn_registrar = None
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
        self.Nombre = StringVar()
        self.contrasenia = StringVar()
        self.background = "#282A36"
        self.foreground_dark = "#262626"
        self.foreground_light = "#F8F8F2"
        self.button_azul = "#75D7EC"

        self.dibujarFrames()
        self.dibujarLabels()
        self.dibujarBotones()

        root.title("Banco")
        root.resizable(not True, not True)
        root.geometry("800x600")
        root.config(background=self.background)
        root.iconphoto(False, PhotoImage(file='tirano-saurio-rex.png'))
        root.mainloop()

    def dibujarFrames(self):
        self.frame_titulo = Frame(self.ventana, background=self.background, height=100)
        self.frame_titulo.pack(fill="x")

        self.F_opciones = Frame(self.ventana, background=self.background, width=200, height=400)
        self.F_opciones.pack(side=LEFT, anchor=N)

        self.F_principal = Frame(self.ventana, background=self.background, height=400, width=600)
        self.F_principal.pack()

        self.mantenerFrameBtnRE = Frame(self.F_opciones, background=self.background, width=200, height=50)
        self.mantenerFrameBtnRE.pack()

        self.F_btnRE = Frame(self.mantenerFrameBtnRE, width=200, height=50)
        self.F_btnRE.pack()

        self.mantenerFrameBtnA = Frame(self.F_opciones, background=self.background, width=200, height=50)
        self.mantenerFrameBtnA.pack()

        self.F_btnA = Frame(self.mantenerFrameBtnA, width=200, height=50)
        self.F_btnA.pack()

        self.mantenerFrameBtnC = Frame(self.F_opciones, background=self.background, width=200, height=50)
        self.mantenerFrameBtnC.pack()

        self.F_btnC = Frame(self.mantenerFrameBtnC, width=200, height=50)
        self.F_btnC.pack()

        self.mantenerFrameBtnR = Frame(self.F_opciones, background=self.background, width=200, height=50)
        self.mantenerFrameBtnR.pack()

        self.F_btnR = Frame(self.mantenerFrameBtnR, width=200, height=50)
        self.F_btnR.pack()

        self.mantenerFrameBtnS = Frame(self.F_opciones, background=self.background, width=200, height=50)
        self.mantenerFrameBtnS.pack()

        self.F_btnS = Frame(self.mantenerFrameBtnS, width=200, height=50)
        self.F_btnS.pack()

    def dibujarLabels(self):
        self.lbl_title = Label(self.frame_titulo, foreground=self.foreground_light, background=self.background,
                               text="Banco", font=("", 16))
        self.lbl_title.place(x=340, y=30, width=120)

        self.lbl_bienbenida = Label(self.F_principal, foreground=self.foreground_light, background=self.background,
                                    text="BIENVENIDO",
                                    font=("", 16))
        self.lbl_bienbenida.place(x=225, y=10, width=150)

        self.lbl_Nombre = Label(self.F_principal, foreground=self.foreground_light, background=self.background,
                                textvariable=self.Nombre,
                                font=("", 16))
        self.lbl_Nombre.place(x=225, y=60, width=150)

    def dibujarBotones(self):
        self.Btn_registrar = Button(self.F_btnRE, relief="flat", foreground=self.foreground_dark,
                                    background=self.button_azul,
                                    text="Registrar", command=lambda: self.popup())
        self.Btn_registrar.place(x=0, y=0, width=200, height=50)

        self.Btn_auth = Button(self.F_btnA, relief="flat", foreground=self.foreground_dark, background=self.button_azul,
                               text="Autenticar",
                               command=lambda: self.frameAuth())
        self.Btn_auth.place(x=0, y=0, width=200, height=50)

        self.Btn_consultar = Button(self.F_btnC, relief="flat", foreground=self.foreground_dark,
                                    background=self.button_azul, text="Retirar")
        self.Btn_consultar.place(x=0, y=0, width=200, height=50)

        self.Btn_retirar = Button(self.F_btnR, relief="flat", foreground=self.foreground_dark,
                                  background=self.button_azul, text="Retirar")
        self.Btn_retirar.place(x=0, y=0, width=200, height=50)

        self.Btn_salir = Button(self.F_btnS, relief="flat", foreground=self.foreground_dark,
                                background=self.button_azul, text="Salir",
                                command=lambda: self.salir())
        self.Btn_salir.place(x=0, y=0, width=200, height=50)

    def frameAuth(self):
        self.frame_Auth = Frame(self.F_principal, background=self.background, height=400, width=600)
        self.frame_Auth.pack(padx=100, pady=100)
        self.lbl_Auth_nombre = Label(self.frame_Auth, text="Nombre de usuario:  ", font=("", 12),
                                     background=self.background,
                                     foreground=self.foreground_light)
        self.lbl_Auth_nombre.place(x=0, y=30)

        self.entryNombre = Entry(self.frame_Auth, textvariable=self.nombre, width=100, font=("", 12))
        self.entryNombre.place(x=0, y=60)

        self.lbl_Auth_contrasenia = Label(self.frame_Auth, text="Contraseña:  ", font=("", 12),
                                          background=self.background,
                                          foreground=self.foreground_light)
        self.lbl_Auth_contrasenia.place(x=0, y=90)

        self.entryContrasenia = Entry(self.frame_Auth, textvariable=self.contrasenia, width=100, font=("", 12))
        self.entryContrasenia.place(x=0, y=120)

        self.btn_auth_iniciar_sesion = Button(self.frame_Auth, relief="flat", foreground=self.foreground_light,
                                              background=self.button_azul, text="Iniciar Sesión",
                                              command=lambda: self.autenticar())
        self.btn_auth_iniciar_sesion.place(x=140, y=160)

    def autenticar(self):
        user = self.controlador.autenticar(self.nombre.get(), self.contrasenia.get())
        if user == False:
            self.popup_mensaje = popup_mensaje(self.ventana,"Error", "Datos incorrectos")
            self.ventana.wait_window(self.popup_mensaje.ventana)
            self.nombre.set("")
            self.contrasenia.set("")
        else:
            self.Nombre.set(user[1])
            self.popup_datos = popup_datos(self.ventana, user)
            self.ventana.wait_window(self.popup_datos.ventana)
            self.dibujarLabels()

    def popup(self):
        self.w = popup_registrar(self.ventana)
        self.ventana.wait_window(self.w.ventana)

    def salir(self):
        self.ventana.destroy()


aplicacion = App()
