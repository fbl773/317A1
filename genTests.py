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
def getCoord(y):
	coord = []
	
	for i in range(y):
		addMe = random()
		coord.append(str(addMe))
	return coord

def genSet(n,y):
	group = []
	for i in range(n):
		group.append(getCoord(y))
	return group

"""
oneTest()
	- Outputs M-N-K-Y values as one followed by 1 randomized point in 1d space
"""
def oneTest():
	mnky = '1 1 1 1 '
	pointSrc  = genSet(1,1)
	pointDes  = genSet(1,1)	
	return mnky + pointSrc[0][0] +' ' + pointDes[0][0]


"""
became completely redundant. sorry
"""
def getMNKY(mnky):
	return str(mnky)


def giveMNKY(giveMe):
	mnky = getMNKY(giveMe)
	numPoints = int(mnky[1]) #The bloody getMNKY function adds a space that changes index we need 
	dimensions = int(mnky[3]) #ditto

	return genSet(numPoints, dimensions)

def runTests():
	tstMNKY = input("MNKY: ")
	generated = giveMNKY(tstMNKY)
	print ("Generated points were: ",generated)
	
def usage():
	bannr = "\n#################################################\n"
	usgMsg = "USAGE: genTest <MNKY>"
	infoMsg= "Outputs the MNKY values then Generates n random \npoints of dimensionality y"
	
	return bannr + infoMsg + '\n' + usgMsg + bannr
#MAIN#################


runTests()

"""
FROM CMD LINE DAYS
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
			numPoints = int(mnky[1])
			dest = ' '.join(genSet(numPoints,int(mnky[3])))
			src = ' '.join(genSet(numPoints,int(mnky[3])))
			print(getMNKY(mnky),src,dest)
	except IndexError as e:
		print (e)
		print (usage())
"""
