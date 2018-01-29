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

def genSet(d,y):
	group = []
	for i in range(y):
		group.append(getCoord(d))
	return group

"""
oneTest()
	- Outputs M-N-K-Y values as one followed by 1 randomized point in 1d space
"""
def oneTest():
	mnky = '1 1 1 1 '
	point  = genSet(1,1)
	return mnky + point[0][0]


def getMNKY(mnky):
	return ' '.join(mnky)
	
def usage():
	bannr = "\n#################################################\n"
	usgMsg = "USAGE: genTest <MNKY>"
	infoMsg= "Outputs the MNKY values then Generates n random \npoints of dimensionality y"
	
	return bannr + infoMsg + '\n' + usgMsg + bannr
#MAIN#################

#I know this is a bunk check, I also know that I really shouldn't need exception handling in a program this simple. 
# But It works. and This is really more of a novelty."
if sys.argv[1] is 'u':
	print (usage())
else:
	try:
		mnky = sys.argv[1]
		if mnky is '1':
			print (oneTest())
		else:
			print(getMNKY(mnky) , genSet(int(mnky[1]),int(mnky[3])))
	except IndexError as e:
		print (e)
		print (usage())

