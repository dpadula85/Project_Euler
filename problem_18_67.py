# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:05:38 2015

@author: Daniele
"""

#Description at https://projecteuler.net/problem=18

#triangle =   0  [[3],               [[3],           [[3],         [[23]]
#             1   [7, 4],        ->   [7, 4],     ->  [20, 19]] ->
#             2   [2, 4, 6],          [10, 13, 15]
#             3   [8, 5, 9, 3]]
#
#                  0  1  2  3

path = 'C:\\Users\\Daniele\\Desktop\\python_practice\\project_Euler\\'
file_num = 'problem_67.txt'
f = open(path + file_num, 'r')
triangle = []
for line in f:
    triangle.append(map(int, line.split()))
    
#analyze the triangle from the bottom
for i in range(len(triangle) - 1, 0, -1):
    for j in range(i):
        triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])
        
print triangle[0][0]    