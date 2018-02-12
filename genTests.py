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

"""
giveMNKY()
	- gives a list of lists that represent a list of N, Ydimensional coordinates
	
	Paramaters
	-----------
	giveMe: an mnky whos n and y values we will use to generate a list of points
	
	return: [[point],....,[point]] A list of coordinates.
	
"""
def giveMNKY(mnky):
	giveMe = getMNKY(mnky)
	numPoints = int(giveMe[1]) #The bloody getMNKY function adds a space that changes index we need 
	dimensions = int(giveMe[3]) #ditto

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

def showcase():
	stopShow = False

	while(not stopShow):
		showMNKY = input("Input MNKY: ")
		showMNKY = getMNKY(showMNKY)

		print ("M: ",showMNKY[0])
		print ("N: ",showMNKY[1])
		print ("K: ",showMNKY[2])
		print ("Y: ",showMNKY[3])

		print ("Randomized point set of size ",showMNKY[1], " and dimensionality ", showMNKY[3])
		print ("*************************************************")
		points = genSet(int(showMNKY[1]),int(showMNKY[3]))
		print (points)
	
		stayShow = input("Run another test? (y/n)")
		if (stayShow is 'n'):
			stopShow = True	
		elif (stayShow is 'y'):
			print ("Start again! \n")
		else:
			print ("yeah I'm lazy. it just will keep going until you type n")
	return
	

#MAIN#################

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
