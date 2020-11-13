# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:24:52 2020

@author: USR
"""

from tkinter import ttk
from tkinter import *
import sqlite3

class Product:
    db_name = 'database.db'
    def __init__(self, window):
        
        self.wind = window
        self.wind.title('COVID-19')
        self.wind.geometry("650x500") #tamaño del frame
        
        frame = LabelFrame(self.wind, text = 'REGISTRAR', fg = 'blue')
        frame.grid(row = 0, column = 10, columnspan = 3, pady = 20)
       
        Label(frame, text = 'Casos: ').grid(row = 1, column = 0)
        self.Casos = Entry(frame)
        self.Casos.focus()
        self.Casos.grid(row = 1, column = 1)

        Label(frame, text = 'Recuperados: ').grid(row = 2, column = 0)
        self.Recuperados = Entry(frame)
        self.Recuperados.grid(row = 2, column = 1)

        Label(frame, text = 'Muertes: ').grid(row = 3, column = 0)
        self.Muertes = Entry(frame)
        self.Muertes.grid(row = 3, column = 1)

        Label(frame, text = 'Estado: ').grid(row = 4, column = 0)
        self.Estado = Entry(frame)
        self.Estado.grid(row = 4, column = 1)


        # Botones 
        ttk.Button(frame, text = 'Ingresar', command = self.add_register).grid(row = 5, columnspan = 2, sticky = W + E)
        ttk.Button(frame, text = 'Buscar', command = self.search_register).grid(row = 6, columnspan = 2, sticky = W + E)

        self.message = Label(text = '', fg = 'gray')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        self.tree = ttk.Treeview(frame, height=10, columns=("#0","#1", "#2", "#3"), selectmode="extended")
        self.tree.grid(row = 8, column = 0, columnspan = 2)
        
        self.tree.heading('#0', text='Casos', anchor=CENTER)
        self.tree.heading("#1", text='Recuperados', anchor=CENTER)
        self.tree.heading("#2", text='Muertes', anchor=CENTER)
        self.tree.heading("#3", text='Estado', anchor=CENTER)
        self.tree.column("#0", stretch=NO, width=100)
        self.tree.column("#1", stretch=NO, width=100)
        self.tree.column("#2", stretch=NO, width=100)
        self.tree.column("#3", stretch=NO, width=100)
        self.get_register()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_register(self,where=""):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        if len(where)>0:
            db_rows = self.run_query( "SELECT * FROM product "+where).fetchall()
        else:
            db_rows = self.run_query( "SELECT * FROM product ").fetchall()
    
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = (row[2], row[3], row[4]))

    def validation(self):
        return len(self.Casos.get()) != 0 and len(self.Recuperados.get()) != 0 and len(self.Muertes.get()) != 0

    def add_register(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?, ?, ?)'
            parameters =  (self.Casos.get(), self.Recuperados.get(), self.Muertes.get(), self.Estado.get())
            self.run_query(query, parameters)
            self.message['text'] = 'REGISTRO EXITOSO'.format(self.Casos.get(), self.Recuperados.get(), self.Muertes.get(), self.Estado.get())
            self.Casos.delete(0, END)
            self.Recuperados.delete(0, END)
            self.Muertes.delete(0, END)
            self.Estado.delete(0, END)
        else:
            self.message['text'] = '*INGRESE INFORMACIÓN*'
        self.get_register()
    
    def search_register(self):
        self.message['text'] = ''
        where=" where 1=1 "
        if len(self.Estado.get())>0 :
            where=where+" and estado='"+self.Estado.get()+"' "
        
        self.get_register(where)

if __name__ == '__main__':
    window = Tk()
    Imagen=PhotoImage(file="")
    Imagen_2 =Label(window, image=Imagen).place(x=0, y=0)
    application = Product(window)
    window.mainloop()
    
    

