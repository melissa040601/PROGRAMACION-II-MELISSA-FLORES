# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 08:34:40 2020

@author: USR
"""

import cv2
import sys

imagePatch=sys.argv[0]
cascPath='haarcascade_frontalface_default.xml'
faceCascade=cv2.CascadeClassifier(cascPath)
image=cv2.imread('.jpg')
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(
    gray,
    ScaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags=cv2.CASCADE_SCALE_IMAGE
    )
print('Se encontraron {0} rostros'.format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y), (x+w,y+h), (0,255,0), 2)
    
cv2.imshow('Rostro Identificado',  image)
cv2.waitKey(0)