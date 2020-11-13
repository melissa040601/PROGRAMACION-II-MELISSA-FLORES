# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:05:01 2020

@author: Melissa Flores Colunga
"""
import json
import tkinter as tk

def funcion():
     for c in data['item1']:
        print('Ciudad', c['Ciudad'])
        print('Contagiados',c['Contagiados'])
        print('Recuperados',c['Recuperados'])
        print('Muertes',c['Muertes'])
        print(' ')

root = tk.Tk()
boton = tk.Button(root, text="COAHUILA", command=funcion)
root.geometry('300x300')
root.title("Ventana")
boton.pack()

def lineaSearch (item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
    return found 

item= 'item 1'
bolsa= ['Coahuila', 'Tabasco','Tamaulipas', 'Puebla', 'Sonora']
itemfound = lineaSearch(item,bolsa)
data= {}

data['item1'] = []
data['Coahuila'].append ({
    'Ciudad' : 'Coahuila',
    'Contagiados' : 22336,
    'Recuperados' : 16967,
    'Muertes' : 1452 })

data['item1'] = []
data['Tabasco'].append ({
    'Ciudad' : 'Tabasco',
    'Contagiados' : 28815,
    'Recuperados' : 22376,
    'Muertes' : 2620 })

data['item1'] = []  
data['Puebla'].append ({
    'Ciudad' : 'Puebla',
    'Contagiados' : 27527,
    'Recuperados' : 17538,
    'Muertes' : 3620 })

data['item1'] = []
data['Tamaulipas'].append ({
    'Ciudad' : 'Tamaulipas',
    'Contagiados' : 24913,
    'Recuperados' : 19575,
    'Muertes' : 1850 })
    
data['item1'] = []
data['Sonora'].append ({
    'Ciudad' : 'Sonora',
    'Contagiados' : 21761,
    'Recuperados' : 15271,
    'Muertes' : 2678 })

with open ('datos.json', 'w') as file:
    json.dump(data,file,indent=2)
    
with open ('datos.json') as file:
    data=json.load(file)    
    
    for c in data['item1']:
        print('Ciudad', c['Ciudad'])
        print('Contagiados',c['Contagiados'])
        print('Recuperados',c['Recuperados'])
        print('Muertes',c['Muertes'])
        print(' ')
    else:
        print('No Existe')