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

#uninformed search
if runMe is 'i':
	testUninformedSearch()
#Informed Search
elif runMe is 's':
	testInformedSearch()
#Problem class
elif runMe is 'p':
	testProblem()

