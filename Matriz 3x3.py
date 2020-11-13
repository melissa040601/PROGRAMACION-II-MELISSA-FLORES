# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:03:15 2020

@author: USR
"""

matriz1=[]
matriz2=[]
matrizResultado=[]

print('Matriz 3*3')
for a in range (3):
    matriz1.append([])
    matriz2.append([])
    matrizResultado.append([])
    
for a in range(3):
    for b in range(3):
      matriz1[a].append(input("Ingresar valor del elemento: ") + str(a) + " " + str(b))
                     
for c in range(3):
    
    for d in range(3):
       matriz2[c].append(input('Ingresar valor de la segunda matriz: '))
      
for a in range(3):
    for b in range(3):
        matrizResultado[a].append(matriz1[a][b] + matriz2[a][b])
                   
print(matriz1)
print(matriz2)
print(matrizResultado)
      