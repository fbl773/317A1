#!/usr/bin/env python3
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 01
#   Tutorial: T01	
# Assignment: MNKY 
#   Synopsis: Shows off the code that we have working. And where we fail on ones don't.

import Problem
import Search
import informedSearch
import genTests
import sys


def usage():
	msg = ("USAGE: runMNKY [-uigsp] \n"+
		"-u Displays usage \n"+
		"-i runs Informed search showcase\n"+
		"-s runs uninformed search showcase\n"+
		"-p runs Problem class showcase\n"+
		"-g runs the test case generator showcase\n")
	return msg


def generatorSC():
	genTests.showcase()

def searchSC():
	Search.showcase()
def problemSC():
	Problem.showcase()
def informedSC():
	informedSearch.showcase()



#main
bannr = '\n*********************\n'

try:
	arg1 = sys.argv[1]
	runMe = arg1.split('-')[1]
except:
	sys.exit(usage())

print ("Showcase MNKY",bannr)
if (runMe is 'u'):
	print(usage())
elif (runMe is 'g'):
	generatorSC()
elif (runMe is 's'):
	searchSC()
elif (runMe is 'p'):
	problemSC()
elif (runMe is 'i'):
	print ("Informed search totally works")
