# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:15:24 2020

@author: USR
"""
#Algoritmo de deteccion de colores
#Detecta objetos rojo, azul y amarillo elimina el ruido y busca su centro
 
import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    rojo_bajos1=np.array([0,100,20], dtype=np.uint8)
    rojo_altos1=np.array([8,255,255], dtype=np.uint8)
 
    #Crear una mascara con solo los pixeles dentro del rango de verdes
    mask1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
    
    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(mask1)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
         
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
        print ("x = ", x)
        print ("y = ", y)
 
        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('Detector de colores', mask1)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()