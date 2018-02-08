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
import genTests
import sys


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

def testGenerator():
	print ("GENERATOR")
	print ("---------")
	genTests.runTests()

#main
runMe = sys.argv[1]
print ("MNKY TESTER")

if runMe is 'i':
	testUninformedSearch()
elif runMe is 's':
	testInformedSearch()
elif runMe is 'p':
	testProblem()
elif runMe is 'g':
	testGenerator()

