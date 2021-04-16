from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import Conexion
import Inicio
import BaseDeDatos

class PaginaInicial(Frame): 
    def __init__(self,master):
        Frame.__init__(self,master,width = 1000,height =600)
        self.barraMenu = Menu(self)
        self.master.config(menu = self.barraMenu)
        self.Inicio = Menu(self.barraMenu,tearoff=0)
        self.Inicio.add_command(label="Pagina principal")
        self.Inicio.add_command(label="Base de datos",command=lambda: master.switch_frame(BaseDeDatos.BD))
        self.Inicio.add_separator()
        self.Inicio.add_command(label="Cerrar",command=self.Cerrar)
        self.Descargas = Menu(self.barraMenu,tearoff=0)
        self.Descargas.add_command(label="Base de datos")
        self.Descargas.add_command(label="Graficos de prediccion")


        self.Ayuda = Menu(self.barraMenu,tearoff=0)
        self.Ayuda.add_command(label="Manual de uso")
        self.Ayuda.add_command(label="Informacion",command=self.Informacion)
        self.Ayuda.add_command(label="Contactos",command=self.Contactos)

        self.barraMenu.add_cascade(label="Inicio",menu = self.Inicio)
        self.barraMenu.add_cascade(label="Descargas",menu = self.Descargas)
        self.barraMenu.add_cascade(label="Ayuda",menu = self.Ayuda)
        self.contenedor()

    def contenedor(self):
        font_datos = tkFont.Font(family="Lucida Grande", size=40)
        font_Texto = tkFont.Font(family="Lucida Grande", size=15)
        font_Subtitulos = tkFont.Font(family="Lucida Grande", size=16)
        Label(self,text = "ESTADO DE SENSORES",font=font_Subtitulos).place(x=37, y=20)
        Label(self,text = "Sensor de temperatura",font=font_Texto).place(x=45, y=62)
        Label(self,text = "Sensor de humedad",font=font_Texto).place(x=45, y=94)
        Label(self,text = "Sensor de ilumnación",font=font_Texto).place(x=45, y=126)

        Label(self,text = "ESTADO DE LA ESTACION",font=font_Subtitulos).place(x=37, y=175)
        Label(self,text = "En funcionamiento",font=font_Texto).place(x=45, y=217)


        Label(self,text = "DATOS ACTUALES",font=font_Subtitulos).place(x=590, y=20)
        Label(self,text = "Temperatura",font=font_Texto).place(x=467, y=160)
        Label(self,text = "Humedad",font=font_Texto).place(x=635, y=160)
        Label(self,text = "Lux",font=font_Texto).place(x=818, y=160)

        temperatura = Label(self,font=font_datos)
        humedad = Label(self,font=font_datos)
        lux = Label(self,font=font_datos)

        temperatura.place(x=500, y=70)
        humedad.place(x=650, y=70)
        lux.place(x=800, y=70)

        temperatura.config(text="15")
        humedad.config(text="15")
        lux.config(text="30")
        
        # temperatura.config(text=Conexion.TemperaturaActual())
        # humedad.config(text=Conexion.HumedadActual())
        # lux.config(text=Conexion.LuxActual())
    def Informacion(self):
        messagebox.showinfo("Estacion meteorologica","Estacion meteorologica basica\nVersion 1.0\n Proyecto computacionl II ")
    def Contactos(self):
        messagebox.showinfo("Contactos","Envie correo a BPC2020106@est.univalle.edu")

    def Cerrar(self):
        valor = messagebox.askokcancel("Cerrar","Deseas cerrar la aplicacion")
        if valor:
            self.master.destroy()
