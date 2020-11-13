# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:27:42 2020

@author: Melissa A Flores Colunga
"""

while 1:
    n1=float (input ("dame un numero: "))
    n2=float (input("dame otro numero: "))
    
    opcion=0 
    print(""" 
          ¿Que quieres hacer?
          1- sumar 
          2- restar
          3- multiplicar
          4- salir
         """)
    
    opcion = int (input ("dame tu opcion:"))
    
    if opcion==1:
        print ("la suma de",n1,"+",n2, "es", n1+n2)
   elif opcion==2:
       print ("la resta de",n1, "-",n2, "es", n1-n2)
   elif opcion==3:
       print ("la multiplicacion de",n1, "x",n2, "es", n1*n2)
   elif opcion==4: 
       print ("la data de virus ha sido actualizada")
       
       break