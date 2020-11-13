# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:06:02 2020

@author: Melissa Flores 
"""

import cv2

while 1:
    opcion=0
    print("""
    ¿Que desea hacer? (eliga una opcion)
    1)Tomar foto nuevamente
    2)Salir
    """)
    opcion=int(input('¿Que desea hacer? '))

    if opcion == 1:
               
        camara = cv2.VideoCapture(0)

        foto,frame=camara.read()

        if foto == True:
            cv2.imwrite('foto.png',frame)
            print('Foto tomada con exito')

        else:
            print('Error de camara, Apagada o No Configurada')

        camara.release()

    elif opcion == 2:
        break
    
    else:
        print('Opcion no valida')