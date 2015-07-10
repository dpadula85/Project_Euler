# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:56:57 2015

@author: Daniele
"""

#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
#fly, F, sits in the opposite corner. By travelling on the surfaces of the room
#the shortest "straight line" distance from S to F is 10 and the path is shown
#on the diagram.
#
#However, there are up to three "shortest" path candidates for any given cuboid
#and the shortest route doesn't always have integer length.
#
#It can be shown that there are exactly 2060 distinct cuboids, ignoring
#rotations, with integer dimensions, up to a maximum size of M by M by M, for
#which the shortest route has integer length when M = 100. This is the least
#value of M for which the number of solutions first exceeds two thousand;
#the number of solutions when M = 99 is 1975.
#
#Find the least value of M such that the number of solutions first exceeds one
#million.
#
#Shortest path in a cuboid AxBxC is the minimum among:
#
#sqrt( (a + b)**2  + c**2 )
#sqrt( (a + c)**2  + b**2 )
#sqrt( (c + b)**2  + a**2 )
#
#Also, look for http://oeis.org/A143714 for a fast solution
#Number of pairs (a,b), 1 <= a <= b <= n, such that (a+b)^2+n^2 is a square.
#Also: Number of cuboids of maximal side length n having integral shortest path
#going on the surface from one vertex to the opposite one.
#Also: Number of subsets {a,b} of {1,..,n} such that (a+b,n) form the shorter
#two legs of a pythagorean triple.

import time
from math import sqrt

#M = 1
lim = 1000000

start = time.time()

#highly inefficient for high values of lim, M
#while count < lim:
#    count = 0
#    for a in range(1, M + 1):
#        for b in range(a, M + 1):
#            for c in range(b, M + 1):
#                path1 = sqrt( (a + b)**2  + c**2 )
#                path2 = sqrt( (a + c)**2  + b**2 )
#                path3 = sqrt( (c + b)**2  + a**2 )
#                path = min(path1, path2, path3)
#                if path.is_integer():
#                    count += 1
#    M += 1
a = 2
c = 0
while c < lim:
    a += 1
    for b in range(3, 2*a):
        if (b*a) % 12 == 0:
            if sqrt((a**2 + b**2)).is_integer():
                c += min(b, a + 1) - (b + 1) //2
                
elapsed = (time.time() - start)            
print a, 'in %5.3f seconds' % elapsed 