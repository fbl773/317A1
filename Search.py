#!/usr/bin/env python3
#File Search
#Contains the various uninformed search algortihms

import Problem

#Queue for BFS
queue = []

def isQueueEmpty(queue):
	return queue == []

"""
Breadth first Search of the search states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the state that is found to meet the goal state or nothing if the goal is not found.
"""
def BFS( startState, problem):
	queue.append(startState)		#Added as per Wiz's bug catch, not adding the first state
	queue.extend(problem.getSuccessors(startState, problem))
	while not isQueueEmpty(queue):
		state = queue.pop()
		if Problem.isGoal(state, problem):
			return state
		else:
			queue.extend(problem.getSuccessors(state, problem))
	return None


def runTests():
	
	bannr = "\n************************\n"
	src = float(input("Source: "))
	dst = float(input("Destination: "))

	testProblem = Problem.Problem(src,dst)
	testState = Problem.ProblemState(0,src,False,0)

	print ("Test Values: ")
	print ("testProblem: " , testProblem.toString())
	print ("\n**********\n")
	print ("TestState: " , testState.toString())


	print ("TEST BFS",bannr)
	#BFS(testState,testProblem)
	
	return

#Main
runTests()
