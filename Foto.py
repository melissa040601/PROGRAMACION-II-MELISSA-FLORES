# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:21:49 2020

@author: USR
"""

import cv2

camara = cv2.Videocapture(0)
leido, frame = camara.read()

if leido==True:
     cv2.inwrite("potob3.png", frame)
     print("Foto tomada con exito")
     
else:
     print('No se tomo la foto')     
     
camara.release()