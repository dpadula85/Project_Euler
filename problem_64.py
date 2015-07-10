# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:57:35 2015

@author: Daniele
"""

#Desctiption at https://projecteuler.net/problem=64

import time
import math
from Euler import *

irr = [i for i in range(10001) if not math.sqrt(i).is_integer()]

start = time.time()

sol = 0
for n in irr:
    p = period(n)[1:]
    if len(p) % 2 == 1:
        sol += 1
        
elapsed = (time.time() - start)
print sol, 'in %5.3f seconds' % elapsed


    