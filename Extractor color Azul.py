# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:33:07 2020

@author: USR
"""

import cv2 
import numpy as np

img=cv2.imread('Almohada.jpg')
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

azul_bajo=np.array([13,90,100])
azul_alto=np.array([500,500,500])

mask=cv2.inRange(hsv,azul_bajo,azul_alto)

cv2.imshow('Foto Original',img)
cv2.imshow('Color extraido',mask)

cv2.waitKey(0)
cv2.destroyALLWindows()
