#!/usr/bin/env python3
#File Search
#Contains the various uninformed search algortihms

import Problem
import collections
from timeit import default_timer as timer

#Queue for BFS
queue = collections.deque([])


def isQueueEmpty(queue):
	return len(queue) == 0

def isEmpty(aList):
	return aList == []

"""
Breadth First Search of the search states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the Path of the search the  number of nodes explored and the maximum size the queue was at any point
		if the search fails the path will be empty
"""
def BFS(startState, problem):
	#Records the largestsize of the queue
	MAXQUEUE = 0
	#Records the number of nodes examined
	NODESCREATED = 1
	queue.append(startState)		#Added as per Wiz's bug catch, not adding the first state
	
	newNodes = problem.getOneProbSuccessors(startState)
	NODESCREATED += len(newNodes)
	queue.extend(newNodes)
	if MAXQUEUE < len(queue):
		MAXQUEUE = len(queue)
	path = []
	while not isQueueEmpty(queue):
		state = queue.popleft()
		path.append(state)
		if problem.isOneProbGoal(state):
			return (path, NODESCREATED, MAXQUEUE)
		else:
			queue.extend(problem.getOneProbSuccessors(state))
"""
A Shameless copy of BFS where the oneD methods are replaced with their twoD counterparts.
"""
def BFSTwoD(startState,problem):
	MAXQUEUE = 0
	NODESCREATED = 1
	queue.append(startState)

	newNodes = problem.getSuccessorsTD(startState) #This is a major difference
	NODESCREATED += len(newNodes)
	queue.extend(newNodes)
	if MAXQUEUE < len(queue):
		MAXQUEUE = len(queue)
	path = []
	while not isQueueEmpty(queue):
		state = queue.popleft()
		path.append(state)
		if problem.isOneProbGoalTD(state):
			return (path,NODESCREATED,MAXQUEUE)
		else:
			queue.extend(problem.getSuccessorsTD(state))
	
"""
Depth first search  of states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the Path of the search the  number of nodes explored and the maximum size the queue was at any point
		if the search fails the path will be empty
"""
def DFS(startState, problem):
	stack = []
	#Records the largest size the stack reaches
	MAXSTACK = 0
	#Records the number of nodes created
	NODESCREATED = 1

	if problem.isOneProbGoal(startState):
		return ([startState], NODESCREATED, MAXSTACK)

	newNodes = problem.getOneProbSuccessors(startState)
	NODESCREATED += len(newNodes)
	stack.extend(newNodes)
	if MAXSTACK < len(stack):
		MAXSTACK = len(stack)

	newPathFlag = False
	while not isEmpty(stack):
		if newPathFlag is True:
			newPathFlag = False
		state = stack.pop()
		path.append(state)
		if problem.isOneProbGoal(state):
			return (state,NODESCREATED, MAXSTACK)
		else:
			temp = problem.getOneProbSuccessors(state)
			NODESCREATED += len(temp)
			stack.extend(temp)
			if MAXSTACK < len(stack):
				MAXSTACK = len(stack)
			if len(temp) < 1:
				newPathFlag = True
	return (None, NODESCREATED, MAXSTACK)

def runTests():
	bannr = "\n********************************\n"
	
	src = 0.5	
	dst = 1.0
	
	#Intializing objects	
	prob = Problem.Problem(dst,src,1,1,1)
	startState = Problem.ProblemStateWithRef(0,src,False,0,None)
	print ("Source: ",src," Dest: ",dst)
	
	#Check Objects
	print ("Problem: ", prob.toString(),'\n')
	print ("State: ", startState.toString())
	print (bannr)
	

	#Testing DFS NOT IN THIS VERSION
	print ("TESTING DFS",bannr)	
	dfsStack = DFS(startState,prob)
	print("Type of dfsStack: ", type(dfsStack))
	print("Within it is: ", dfsStack)
	print("And that is: ", dfsStack.toString())

	print (bannr)

	#Testing BFS
	print ("TESTING BFS",bannr)
	bfsQueue = BFS(startState,prob)
	print("Type of bfsQueue: ",type(bfsQueue))
	print("WIthin it is: ", type(bfsQueue[0]))
	print("And that is: ", bfsQueue[0])
	print("Which contains: ", type(bfsQueue[0][0]))


	print ("TEST BFS",bannr)
	ResultsTup = BFS(startState,prob)


	
	#Two-D testing####################################
	print(bannr,"Testing 2D",bannr)

	#Defining Points
	origin = Problem.coordinate(0,0)
	src = Problem.coordinate(0.5,0.5)
	dst = Problem.coordinate(1.0,1.0)
	print ("TESTPOINTS: \n","Src: ",src.toString(),"\n Dest: ", dst.toString())
	
	#Initializing Problem/State
	prob2 = Problem.Problem(dst,src,1,1,1)
	startState2 = Problem.ProblemStateWithRef(origin,src,False,0,None)	
	print ("Problem: ",prob2.toString())
	print ("State: ", startState2.toString())

	#Testing Search
	print("TESTING BFS",bannr)
	bfsQueue2 = BFSTwoD(startState2,prob2)
	print ("Within BFSTree is: ",bfsQueue2)
	print ("And that is: ", bfsQueue2[0])
	print ("Which contains: ", type(bfsQueue2[0][0]))
	
	for items in bfsQueue2[0]:
		print (items.toString())	

	
	
	return
"""
	timedTest
	a test function to track the times of the functions in this file
	not testing the time of DFS since it is a naive implementation that bottoms out without finding an answer which is expected of it
	:returns nothing
"""
def timedTest():
	testProblem = Problem.Problem(0.5, 1.0)
	testState = Problem.ProblemStateWithRef(0, 1.0, False, 0)
	start = timer()
	bfs = BFS(testState, testProblem)
	end = timer()
	print("Time taken to run Breadth first search: ", end - start)

	src = Problem.coordinate(0.5, 0.5)
	dest = Problem.coordinate(1.0, 1.0)

	tDProb = Problem.Problem(dest, src, 1, 1, 1)
	tDStart = Problem.ProblemStateWithRef(Problem.coordinate(0, 0), src, False, 0, None)
	# timing the one problem on 2D
	start = timer()
	bfs2 = BFSTD(tDStart, tDProb)
	end = timer()
	print("Time taken to run Breadth first search: ", end - start)

	#potentially add code for the general function here too.
