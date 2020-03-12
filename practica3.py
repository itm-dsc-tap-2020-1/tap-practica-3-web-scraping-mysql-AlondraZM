import tkinter as Tk 
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector as mysql

#funcional
pag_inicial=input('INGRESE URL:  ')

url = urlopen(pag_inicial)
print("\nENLACES EXTRAIDOS DE LA PAGINA WEB: " + pag_inicial + "\n")
bs = BeautifulSoup(url.read(), 'html.parser')
for enlaces in bs.find_all("a"):
    print("href: {}".format(enlaces.get("href")))
print("\nFIN DE ENLACES ENCONTRADOS EN:  "+pag_inicial+"\n")

conexion = mysql.connect( host='localhost', user= 'alondra', passwd='garu', db='practica3' )
operacion = conexion.cursor()
operacion.execute( "SELECT * FROM web" )
for pagina,status,  in operacion.fetchall() :
    print (pagina,status)
conexion.close()

