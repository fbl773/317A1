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

def getSet(d,y):
	group = []
	for i in range(y):
		group.append(getCoord(d))
	return group
	
def usage():
	bannr = "\n#################################################\n"
	usgMsg = "USAGE: genPoints <dimensionality> <#Coordinates>"
	infoMsg= "Generates n random points of dimensionality y"
	
	return bannr + infoMsg + '\n' + usgMsg + bannr
#MAIN#################

#I know this is a bunk check, I also know that I really shouldn't need exception handling in a program this simple. 
# But It works. and This is really more of a novelty."
if sys.argv[1] is '-u':
	print (usage())
else:
	try:
		dimensions = sys.argv[1]
		numPoints = sys.argv[2]
		print (getCoord(int(dimension)))
		print("A group of 4:\n", getSet(int(dimension),int(numPoints)))
	except IndexError as e:
		print (usage())

