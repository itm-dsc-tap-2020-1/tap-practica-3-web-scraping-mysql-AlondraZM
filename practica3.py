import tkinter as Tk 
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector as mysql


conexion = mysql.connect( host='localhost', user= 'alondra', passwd='garu', db='practica3' )
operacion = conexion.cursor()
operacion.execute( "SELECT * FROM web" )

pag_inicial=input('INGRESE URL:  ')
url = urlopen(pag_inicial)


print("\nENLACES EXTRAIDOS DE LA PAGINA WEB: " + pag_inicial + "\n")
bs = BeautifulSoup(url.read(), 'html.parser')
lista_enlaces=bs.find_all("a")
for enlaces in lista_enlaces :
    for i in lista_enlaces:
        try:
            url: str=i["href"]
        except KeyError:
            continue
        if not url.startswith("http"):
            continue
        try:
            operacion.execute(f'INSERT INTO web VALUES ("{url}",false)')
        except mysql.errors.IntegrityError:
            continue
    print("href: {}".format(enlaces.get("href")))
print("\nFIN DE ENLACES ENCONTRADOS EN:  "+pag_inicial+"\n")
#mostrar tabla
for pagina,status,  in operacion.fetchall() :
    print (pagina,status)

for pagina,status,  in operacion.fetchall():
    url=pagina

    print("\nENLACES EXTRAIDOS DE LA PAGINA WEB: " + pag_inicial + "\n")
    bs = BeautifulSoup(url.read(), 'html.parser')
    lista_enlaces=bs.find_all("a")
    for enlaces in lista_enlaces :
        for i in lista_enlaces:
            try:
                url: str=i["href"]
            except KeyError:
                continue
            if not url.startswith("http"):
                continue
            try:
                operacion.execute(f'INSERT INTO web VALUES ("{url}",false)')
            except mysql.errors.IntegrityError:
                continue
    

        print("href: {}".format(enlaces.get("href")))
print("\nFIN DE ENLACES ENCONTRADOS EN:  "+pag_inicial+"\n")


conexion.close()

'''

