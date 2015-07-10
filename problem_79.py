# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:16:08 2015

@author: Daniele
"""

#A common security method used for online banking is to ask the user for three
#random characters from a passcode. For example, if the passcode was 531278,
#they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
#317.
#
#The text file, keylog.txt, contains fifty successful login attempts.
#
#Given that the three characters are always asked for in order, analyse the file
#so as to determine the shortest possible secret passcode of unknown length.
#
#Analyzing the data in problem_79.txt is easy to come up with an answer thanks
#to these observations:
#
#remove duplicates and sort the data
#4 and 5 are never present, so the sequence is 8 digits long (0...9)
#0 is always last and 7 always first.
#the only number that comes before 3 is 7
#9 is usually last or before 0
#8 is last or before a 9 or a 0
#1 is after 3
#6 is always after 1 but before 8, 9, 0
#2 is after 6
#
#thus our sequence is 73162890