# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:06:54 2020

@author: USR
"""

from numpy import *
a = array([['Lunes', 18,20,22,17],['Martes',11,18,21,18], 
                     ['Miercoles', 5, 21, 20, 19], ['Jueves',11,20,22,21],
                     ['Viernes', 18,17,23,22], ['Sabado',12,22,20,18],
                     ['Domingo', 13,15,19,16]])
m = reshape(a,(7,5))
print(m)
print(m[2])
print(m[4][3])
