# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:20:45 2015

@author: Daniele
"""

#Three distinct points are plotted at random on a Cartesian plane, for which
#-1000 ≤ x, y ≤ 1000, such that a triangle is formed.
#
#Consider the following two triangles:
#
#A(-340,495), B(-153,-910), C(835,-947)
#
#X(-175,41), Y(-421,-714), Z(574,-645)
#
#It can be verified that triangle ABC contains the origin, whereas triangle XYZ
#does not.
#
#Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text
#file containing the co-ordinates of one thousand "random" triangles, find the
#number of triangles for which the interior contains the origin.
#
#NOTE: The first two examples in the file represent the triangles in the
#example given above.
#
#The idea is to compare the area of ABC with the sum of the areas AOB, AOC, BOC.
#If the areas are the same, then O is inside ABC.
#Here is a method for the calculation of areas given the coordinates of the
#vertices:
#http://en.wikipedia.org/wiki/Triangle#Using_coordinates

import time

path = 'C:\\Users\\Daniele\\Desktop\\python_practice\\project_Euler\\'
file_words = 'problem_102.txt'
f = open(path + file_words, 'r')

start = time.time()

count = 0
for line in f.readlines():
    xa, ya, xb, yb, xc, yc = map(int, line.strip().split(','))
    A_abc = 0.5*abs(((xa - xc)*(yb - ya) - (xa - xb)*(yc - ya)))
    A_aob = 0.5*abs((xa*yb - xb*ya))
    A_aoc = 0.5*abs((xa*yc - xc*ya))
    A_boc = 0.5*abs((xb*yc - xc*yb))
    if A_abc == A_aob + A_aoc + A_boc:
        count += 1
    
elapsed = (time.time() - start)            
print count, 'in %5.3f seconds' % elapsed