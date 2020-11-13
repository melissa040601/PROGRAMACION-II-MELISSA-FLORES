# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:09:18 2020

@author: Melissa A Flores Colunga
"""

import cv2
import numpy as np

img=cv2.imread('Marron.jpg')
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

marron_bajo=np.array([5,125,90])
marron_alto=np.array([23,245,180])

mask=cv2.inRange(hsv,marron_bajo,marron_alto)

cv2.imshow('Foto Original',img)
cv2.imshow('Foto Marron Extraida', mask)

print("\nPulsa cualquier tecla para cerrar\n")

cv2.waitKey(0)
cv2.destroyAllWindows()