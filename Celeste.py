# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:20:53 2020

@author: Melissa A Flores Colunga
"""

import cv2
import numpy as np

img=cv2.imread('Celeste.jpg')
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

celeste_bajo=np.array([90,50,50])
celeste_alto=np.array([130,135,255])

mask=cv2.inRange(hsv,celeste_bajo,celeste_alto)

cv2.imshow('Foto Original',img)
cv2.imshow('Foto Celeste Extraida', mask)
print("\n Pulsa cualquier tecla para cerrar\n")


cv2.waitKey(0)
cv2.destroyAllWindows()