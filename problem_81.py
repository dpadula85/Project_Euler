# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:06:16 2015

@author: Daniele
"""

#Description at https://projecteuler.net/problem=81
#Find the minimum path in a 80x80 matrix by moving only down or right.
#
#The solution is similar to problem 18:
#We calculate the sum of the present cell with the right and down cells.
#We then move to the cell giving the minimum result and repeat till we got to
#the end point.

import time
import numpy as np

path = 'C:\\Users\\Daniele\\Desktop\\python_practice\\project_Euler\\'
file_mat = 'problem_81.txt'
m = np.loadtxt(path + file_mat, delimiter=',')   #load matrix into numpy array
w, h = m.shape  #80, 80

start = time.time()

for i in range(w):
    for j in range(h):
        if i > 0 and j == 0:
            m[i][j] += m[i - 1][j]
        elif i == 0 and j > 0:
            m[i][j] += m[i][j - 1]
        elif i > 0 and j > 0:
            m[i][j] += min(m[i - 1][j], m[i][j - 1])
        
elapsed = (time.time() - start)            
print m[-1][-1], 'in %5.3f seconds' % elapsed       