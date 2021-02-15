#!/usr/bin/env python3
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 01
#   Tutorial: T01	
# Assignment: MNKY 
#   Synopsis: Calls the runTest method of all the modules when given a commandline arg.

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
	Search.timedTest()

def testInformedSearch():
	print ("INFORMED search")
	print ("---------------")
	informedSearch.runTests()
	informedSearch.timedTest()

def testGenerator():
	print ("GENERATOR")
	print ("---------")
	genTests.runTests()

#main
runMe = sys.argv[1]
print ("MNKY TESTER")

if runMe is 'i':
	testInformedSearch()
elif runMe is 's':
	testUninformedSearch()
elif runMe is 'p':
	testProblem()
elif runMe is 'g':
	testGenerator()

