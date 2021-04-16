from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox


import Inicio
import PaginaInicial
import Conexion
from tkinter import ttk

class BD(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,width = 1000,height =600)
        self.barraMenu = Menu(self)
        self.master.config(menu = self.barraMenu)
        self.Inicio = Menu(self.barraMenu,tearoff=0)
        self.Inicio.add_command(label="Pagina principal",command=lambda: master.switch_frame(PaginaInicial.PaginaInicial))
        self.Inicio.add_command(label="Base de datos")
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
        Conexion.conexionBD()
        self.Mostrar()

    def contenedor(self):
        font_datos = tkFont.Font(family="Lucida Grande", size=40)
        font_Texto = tkFont.Font(family="Lucida Grande", size=15)
        font_Subtitulos = tkFont.Font(family="Lucida Grande", size=16)
        Label(self,text = "Consulta de datos",font=font_Subtitulos).grid(row=1,column=0,columnspan=2,padx=30)
        Label(self,text = "Fecha Inicio",font=font_Texto).grid(row=2,column=0,sticky=W,padx=50)
        Label(self,text = "Fecha Final",font=font_Texto).grid(row=3,column=0,sticky=W,padx=50)
        Button(self,text="Descargar",font=font_Texto,command=self.DescargarDatos).grid(row=5,column=0)


        self.Tabla = ttk.Treeview(self)
        self.Tabla['columns'] = ("Temperatura","Humedad","Lux","Fecha")
        
        self.Tabla.column("#0",width=120,minwidth=25)
        self.Tabla.column("Temperatura",width=120,anchor= CENTER)
        self.Tabla.column("Humedad",width=120,anchor= CENTER)
        self.Tabla.column("Lux",width=120,anchor= CENTER)
        self.Tabla.column("Fecha",width=120,anchor= CENTER)
        self.Tabla.heading("#0",text = "ID",anchor=W)
        self.Tabla.heading("Temperatura",text = "Temperatura",anchor=W)
        self.Tabla.heading("Humedad",text = "Humedad",anchor=W)
        self.Tabla.heading("Lux",text = "Lux",anchor=W)
        self.Tabla.heading("Fecha",text = "Fecha",anchor=W)
        self.Tabla.grid(row=1,column=3,columnspan=7,rowspan=9,padx=50)
        # temperatura.config(text=Conexion.TemperaturaActual())
        # humedad.config(text=Conexion.HumedadActual())
        # lux.config(text=Conexion.LuxActual())


    def DescargarDatos(self):
        self.limpiar()
        data  = Conexion.getDatos()
        Humedad=""
        Temperatura=""
        Lux=""
        Fecha=""
        for k in data:
            Humedad = Conexion.getHumedad(k)
            Temperatura = Conexion.getTemperatura(k)
            Lux = Conexion.getLux(k)
            Fecha = Conexion.getFecha(k)
            Conexion.CrearBD(k,Temperatura,Humedad,Lux,Fecha)
        self.Mostrar()

    def limpiar(self):
        registro = self.Tabla.get_children()
        for elementos in registro:
            self.Tabla.delete(elementos)

    def Mostrar(self):
        self.limpiar()
        datos = Conexion.mostrar()
        for row in datos:
            self.Tabla.insert(parent='',index='end',iid=row[0],text=row[0],values=(row[1],row[2],row[3],row[4]))
   
    def Informacion(self):
        messagebox.showinfo("Estacion meteorologica","Estacion meteorologica basica\nVersion 1.0\n Proyecto computacionl II ")
    def Contactos(self):
        messagebox.showinfo("Contactos","Envie correo a BPC2020106@est.univalle.edu")

    def Cerrar(self):
        valor = messagebox.askokcancel("Cerrar","Deseas cerrar la aplicacion")
        if valor:
            self.master.destroy()