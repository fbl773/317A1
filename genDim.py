#!/usr/bin/env python3
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 01	
#   Tutorial: T01
# Assignment: M-N-K-Y
#   Synopsis: Generates a series of tests based on a given dimension

import sys
from random import random
'''
   genCoord()
	- Generates a single d dimensional coordinate
   Paramaters
   ----------
	d: the dimesionality of the coordinate
'''
def getCoord(d):
	coord = []
	
	for i in range(d):
		addMe = random()
		coord.append(str(addMe))
	return coord

#MAIN#####
dimension = sys.argv[1]
print (getCoord(int(dimension)))

