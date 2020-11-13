# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:58:22 2020

@author: USR
"""

import cv2 
import numpy as np
from PIL import Image

foto=Image.open('Melanoma Maligno.jpg')

datos = list(foto.getdata())
print(datos)


    
  

