# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:32:48 2020

@author: Melissa A Flores Colunga
"""

import cv2 
import numpy as np

img=cv2.imread('Rojo.jpg')
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rojo_bajo=np.array([0,110,40])
rojo_alto=np.array([8,255,255])

mask=cv2.inRange(hsv,rojo_bajo,rojo_alto)

cv2.imshow('Foto Original',img)
cv2.imshow('Foto Roja Extraida', mask)

print("\nPulsa cualquier tecla para cerrar\n")

cv2.waitKey(0)
cv2.destroyAllWindows()