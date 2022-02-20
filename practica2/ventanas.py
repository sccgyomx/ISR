from tkinter import *
from Controlador import Controlador


class popup_registrar:
    def __init__(self, master):
        self.passwd = StringVar()
        self.name = StringVar()
        self.frame_label_name = None

        self.background = "#282A36"
        self.foreground_dark = "#262626"
        self.foreground_light = "#F8F8F2"
        self.button_rojo = "#E64747"
        self.button_verde = "#42E66C"

        self.controlador = Controlador()

        self.ventana = Toplevel(master)
        self.dibujar_grid()
        self.ventana.title("Insertar")
        self.ventana.resizable(not True, not True)
        self.ventana.config(background=self.background)

    def dibujar_grid(self):
        self.frame_label_name = Frame(self.ventana, background=self.background, height=100, width=200)
        self.frame_label_name.grid(row=0, column=0, padx=5, pady=5)

        self.label_name = Label(self.frame_label_name, text=" Nombre de usuario:  ", font=("", 12),
                                background=self.background,
                                foreground="white")
        self.label_name.pack()

        self.frame_entry_name = Frame(self.ventana, background=self.background, height=100, width=200)
        self.frame_entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.entry_name = Entry(self.frame_entry_name, textvariable=self.name, font=("", 12))
        self.entry_name.pack()

        self.frame_label_pass = Frame(self.ventana, background=self.background, height=100, width=200)
        self.frame_label_pass.grid(row=1, column=0, padx=5, pady=5)

        self.label_pass = Label(self.frame_label_pass, text=" Contraseña:  ", font=("", 12), background=self.background,
                                foreground="white")
        self.label_pass.pack()

        self.frame_entry_pass = Frame(self.ventana, background=self.background, height=100, width=200)
        self.frame_entry_pass.grid(row=1, column=1, padx=5, pady=5)
        self.entry_pass = Entry(self.frame_entry_pass, textvariable=self.passwd, font=("", 12))
        self.entry_pass.pack()

        self.frame_button_save = Frame(self.ventana, background=self.background, height=100, width=200)
        self.frame_button_save.grid(row=2, column=0, padx=5, pady=5)

        self.button_save = Button(self.frame_button_save, background=self.button_verde, text="Guardar", relief="flat",
                                  foreground=self.foreground_dark, command=lambda: self.insertar())
        self.button_save.pack()

        self.frame_button_cancel = Frame(self.ventana, background=self.background, height=100, width=200)
        self.frame_button_cancel.grid(row=2, column=1, padx=5, pady=5)

        self.button_cancel = Button(self.frame_button_cancel, background=self.button_rojo, text="Cancelar",
                                    relief="flat", foreground=self.foreground_dark, command=lambda: self.cancelar())
        self.button_cancel.pack()

    def insertar(self):
        self.controlador.insertar(self.name.get(), self.passwd.get())
        self.ventana.destroy()

    def cancelar(self):
        self.ventana.destroy()


class popup_datos():
    def __init__(self, master, user):
        self.label_passwd_cryp = None
        self.label_passwd = None
        self.label_name = None
        self.background = "#282A36"
        self.foreground_dark = "#262626"
        self.foreground_light = "#F8F8F2"
        self.button_verde = "#42E66C"

        self.ventana = Toplevel(master)
        self.dibujar_elementos(user)
        self.ventana.title("Datos")
        self.ventana.resizable(not True, not True)
        self.ventana.config(background=self.background)

    def dibujar_elementos(self, user):
        self.label_name = Label(self.ventana, text="Nombre: " + user[1], font=("", 18), background=self.background,
                                foreground=self.foreground_light)

        self.label_passwd = Label(self.ventana, text="Contraseña: " + user[2], font=("", 18),
                                  background=self.background,
                                  foreground=self.foreground_light)

        self.label_passwd_cryp = Label(self.ventana, text="Contraseña cifrada:\n" + user[3], font=("", 18),
                                       background=self.background,
                                       foreground=self.foreground_light)

        self.button_ok = Button(self.ventana, background=self.button_verde, text="Ok", relief="flat",
                                foreground=self.foreground_dark, command=lambda: self.salir())

        self.label_name.pack()
        self.label_passwd.pack()
        self.label_passwd_cryp.pack()
        self.button_ok.pack()

    def salir(self):
        self.ventana.destroy()


class popup_mensaje():
    def __init__(self, master,title, message):
        self.label_message = None
        self.background = "#282A36"
        self.foreground_dark = "#262626"
        self.foreground_error = '#E64747'
        self.button_verde = "#42E66C"

        self.ventana = Toplevel(master)
        self.dibujar_elementos(message)
        self.ventana.title(title)
        self.ventana.resizable(not True, not True)
        self.ventana.config(background=self.background)

    def dibujar_elementos(self, message):
        self.label_message = Label(self.ventana, text=message, font=("", 18), background=self.background,
                                   foreground=self.foreground_error)
        self.button_ok = Button(self.ventana, background=self.button_verde, text="Ok", relief="flat",
                                foreground=self.foreground_dark, command=lambda: self.salir())
        self.label_message.pack()
        self.button_ok.pack()

    def salir(self):
        self.ventana.destroy()
