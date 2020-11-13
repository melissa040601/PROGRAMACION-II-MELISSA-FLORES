# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:50:08 2020

@author: USR
"""

import numpy as np
ma = np.array(([11,12,13], [21,22,23], [31,32,33]))
print(ma)
mat = np.array(([111,112,113], [121,122,123], [131,132,133]))
print('')
print(mat)
print('')
print('suma')
print(ma + mat)
print('')
print(ma * mat)

print(ma[2][0] + mat[2][0])
