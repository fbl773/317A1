#!/usr/bin/env python3
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 01
#   Tutorial: T01	
# Assignment: MNKY 
#   Synopsis: Calls the runTest method of all the modules

import Problem
import Search
import informedSearch
import sys
print ("MNKY Tester")

def testProblem():
	print ("PROBLEM")
	print ("-------")
	Problem.runTests()


def testUninformedSearch():
	print ("SEARCH")
	print ("------")
	Search.runTests()

def testInformedSearch():
	print ("INFORMED search")
	print ("---------------")
	informedSearch.runTests()

#main
runMe = sys.argv[1]

#informed search
if runMe is 'i':
	testInformedSearch()
#Uninformed Search
elif runMe is 's':
	testUinformedSearch()
#Problem class
elif runMe is 'p':
	testProblem()
else:
	print("call with: i for informedSearch.py\n s for Search.py\n p for Problem.py\n")
