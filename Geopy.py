# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:08:21 2020

@author: USR
"""

from geopy.geocoders import Nominatim 

import time
import math

geolocator = Nominatim(user_agent="AppMap")
location=geolocator.geocode ("Frontera Coahuila")
print(location.address)
print((location.latitude,location.longitude))
