from firebase import firebase
from tkinter import messagebox
import sqlite3
# put the name of your database where the ***** are
address = "https://estacion-meteorologica-6a5e1-default-rtdb.firebaseio.com/"
fb = firebase.FirebaseApplication(address)

def conexionBD():
    conexion=sqlite3.connect("Estacion")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
        CREATE TABLE Datos(
            Id varchar(50) PRIMARY KEY,
            Temperatura FLOAT,
            Humeda FLOAT,
            Iluminacion FLOAT,
            Fecha VARCHAR(50)
        )
        ''')
        messagebox.showinfo("CONEXION","BASE DE DATOS CREADA")
    except:
        messagebox.showinfo("CONEXION","CONEXION EXITOSA")


def CrearBD(index,temperatura,humedad,lux,fecha):
    conexion=sqlite3.connect("Estacion")
    cursor = conexion.cursor()
    try:
        datos = index,temperatura,humedad,lux,fecha
        cursor.execute("INSERT INTO Datos VALUES(?,?,?,?,?)",(datos))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","OCURRIO UN ERROR EN EL REGISTRO")
        pass

def mostrar():
    conexion=sqlite3.connect("Estacion")
    cursor = conexion.cursor()
    datos = cursor.execute("SELECT * FROM Datos")
    return datos


def TemperaturaActual():
    temperatura =fb.get("/Estacion/Fijos/Temperatura","")
    return temperatura

def HumedadActual():
    humedad =fb.get("/Estacion/Fijos/Humedad","")
    return humedad

def LuxActual():
    lux = fb.get("/Estacion/Fijos/LUX","")
    return lux
def getDatos():
    data = fb.get(address, "/Estacion/BD/Datos")
    return data
def getTemperatura(id):
    dato = fb.get(address, "/Estacion/BD/Datos/"+id+"/Temperatura")
    return dato
def getLux(id):
    dato = fb.get(address, "/Estacion/BD/Datos/"+id+"/LUX")
    return dato
def getHumedad(id):
    dato = fb.get(address, "/Estacion/BD/Datos/"+id+"/Humedad")
    return dato
def getFecha(id):
    dato=""
    ano = str(fb.get(address, "/Estacion/BD/Datos/"+id+"/Año"))
    mes = str(fb.get(address, "/Estacion/BD/Datos/"+id+"/Mes"))
    dia = str(fb.get(address, "/Estacion/BD/Datos/"+id+"/Dia"))
    hora = str(fb.get(address, "/Estacion/BD/Datos/"+id+"/Hora"))
    minuto = str(fb.get(address, "/Estacion/BD/Datos/"+id+"/Minuto"))
    segundo =str(fb.get(address, "/Estacion/BD/Datos/"+id+"/Segundo"))
    dato += dia+"/"+mes+"/"+ano+"/"+"-"+hora+":"+minuto+":"+segundo
    return dato