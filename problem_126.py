# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Fri Jul 17 15:51:58 2015                                                                                     
@author: Daniele                                                                                                        
"""

#If we then add a second layer to this solid it would require forty-six cubes
#to cover every visible face, the third layer would require seventy-eight cubes
#and the fourth layer would require one-hundred and eighteen cubes to cover
#every visible face.
#
#However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-
#two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1
#and 11 x 1 x 1 all contain forty-six cubes.
#
#We shall define C(n) to represent the number of cuboids that contain n cubes
#in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.
#
#It turns out that 154 is the least value of n for which C(n) = 10.
#
#Find the least value of n for which C(n) = 1000.
#
# The function to calculate the cubes needed to cover up a cuboid of dimensions
# x, y, z up to the kth layer is
# Cubes(x,y,z,k) = 2(xy + xz + yz) + 4(x + y + z + k - 2)(k - 1)
# Now we have to find the number of cubes in a layer for which 1000 solutions
# are possible.

import time
import math 
from Euler import *

def Cubes(x, y, z, k):
    return 2*(x*y + x*z + y*z) + 4*(x + y + z + k - 2)*(k - 1)

def C(k):
    count = 0
    a = 1
    while 4*a <= k:
        b = 1
        while 2*a*b <= k and b <= a:
            n = 1
            while (k - 2*a*b - 4*(n - 1)*(a + b + n - 2) > 0):
                if ((k - 2*a*b - 4*(n - 1)*(a + b + n - 2)) % (2*a + 2*b + 4*(n - 1)) == 0):
                    c = (k - 2*a*b - 4*(n - 1)*(a + b + n - 2)) / (2*a + 2*b + 4*(n - 1))
                    if c <= b:
                        count += 1
                n += 1
            b += 1
        a += 1
    return count

start = time.time()

target = 1000
# Really slow (more than 15 minutes) but it does the job. No ideas on how to
# improve it
n = 1 
result = C(n)
while result != target:
    n += 1
    result = C(n)
    

elapsed = (time.time() - start)                                                                                         
print n, 'in %5.3f seconds' % elapsed 
