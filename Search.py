#!/usr/bin/env python3
#File Search
#Contains the various uninformed search algortihms

import Problem
import collections

#Queue for BFS
queue = collections.deque([])



def isQueueEmpty(queue):
	return len(queue) == 0

"""
Breadth first Search of the search states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the Path of the search the  number of nodes explored and the maximum size the queue was at any point
		if the search fails the path will be empty
"""
def BFS( startState, problem):
	#Records the largestsize of the queue
	MAXQUEUE = 0
	#Records the number of nodes examined
	NODESCREATED = 1
	queue.append(startState)		#Added as per Wiz's bug catch, not adding the first state
	newNodes = problem.getSuccessors(startState)
	NODESCREATED += len(newNodes)
	queue.extend(newNodes)
	if MAXQUEUE < len(queue):
		MAXQUEUE = len(queue)
	path = []
	while not isQueueEmpty(queue):
		state = queue.popleft()
		path.append(state)
		if problem.isGoal(state):
			return (path, NODESCREATED, MAXQUEUE)
		else:
			queue.extend(problem.getSuccessors(state))
	return (None, NODESCREATED, MAXQUEUE)


def runTests():
	
	bannr = "\n************************\n"
	src = float(input("Source: "))
	dst = float(input("Destination: "))

	testProblem = Problem.Problem(dst,src)
	testState = Problem.ProblemState(0,src,False,0)

	print ("Test Values: ")
	print ("testProblem: " , testProblem.toString())
	print ("\n**********\n")
	print ("TestState: " , testState.toString())


	print ("TEST BFS",bannr)
	ResultsTup = BFS(testState,testProblem)

	for items in ResultsTup[0]:
		print(items.toString())
	
	return

#Main
runTests()
