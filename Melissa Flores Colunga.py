from tkinter import *
from tkinter.ttk import *
from io import open

windows=Tk()
windows.title("Covid 2020")
selected=IntVar()

def click():
    if selected.get()==1:
        pantalla="""
Coahuila de Zaragoza:
Casos= 22,338
Recuperados= 16,967
Muertes= 1,452
"""
        archivo=open("coahuila.txt","w")
        archivo.write(pantalla)
        archivo=open("coahuila.txt","r")
        text=archivo.read()
        archivo.close()
        print(text)
        
    elif selected.get()==2:
        pantalla="""
Puebla:
Casos= 27,527
Recuperados= 17,538
Muertes= 3,620
"""
        archivo=open("puebla.txt","w")
        archivo.write(pantalla)
        archivo=open("puebla.txt","r")
        text=archivo.read()
        archivo.close()
        print(text)
        
    elif selected.get()==3:
        pantalla="""
Sonora:
Casos= 21,761
Recuperados= 15,271
Muertes= 2,678
"""
        archivo=open("sonora.txt","w")
        archivo.write(pantalla)
        archivo=open("sonora.txt","r")
        text=archivo.read()
        archivo.close()
        print(text)
        
    elif selected.get()==4:
        pantalla="""
Tabasco:
Casos= 29,815
Recuperados= 22,376
Muertes= 2,620
"""
        archivo=open("tabasco.txt","w")
        archivo.write(pantalla)
        archivo=open("tabasco.txt","r")
        text=archivo.read()
        archivo.close()
        print(text)
        
    else:
        pantalla="""
Tamaulipas:
Casos= 24,913
Recuperados= 19,575
Muertes= 1,850
"""
        archivo=open("tamaulipas.txt","w")
        archivo.write(pantalla)
        archivo=open("tamaulipas.txt","r")
        text=archivo.read()
        archivo.close()
        print(text)

boton1=Radiobutton(windows,text="Coahuila",value=1, variable=selected)
boton2=Radiobutton(windows,text="Puebla",value=2, variable=selected)
boton3=Radiobutton(windows,text="Sonora",value=3, variable=selected)
boton4=Radiobutton(windows,text="Tabasco",value=4, variable=selected)
boton5=Radiobutton(windows,text="Tamaulipas",value=5, variable=selected)
imp=Button(windows,text="Imprimir",command=click)

boton1.grid(column=0,row=0)
boton2.grid(column=1,row=0)
boton3.grid(column=2,row=0)
boton4.grid(column=3,row=0)
boton5.grid(column=4,row=0)
imp.grid(column=5,row=0)

windows.mainloop()
