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
	#path = []
	while not isQueueEmpty(queue):
		state = queue.popleft()
		#path.append(state)
		if problem.isOneProbGoal(state):
			return (state, NODESCREATED, MAXQUEUE)
		else:
			temp = problem.getOneProbSuccessors(state)
			NODESCREATED += len(temp)
			queue.extend(temp)
			if MAXQUEUE < len(queue):
				MAXQUEUE = len(queue)
	return (None, NODESCREATED, MAXQUEUE)
"""
A Shameless copy of BFS where the oneD methods are replaced with their twoD counterparts.
"""
def BFSTD(startState,problem):
	MAXQUEUE = 0
	NODESCREATED = 1
	queue.append(startState)

	newNodes = problem.getSuccessorsTD(startState) #This is a major difference
	NODESCREATED += len(newNodes)
	queue.extend(newNodes)
	if MAXQUEUE < len(queue):
		MAXQUEUE = len(queue)
	#path = []
	while not isQueueEmpty(queue):
		state = queue.popleft()
		#path.append(state)
		if problem.isOneProbGoalTD(state):
			return (state,NODESCREATED,MAXQUEUE)
		else:
			temp = problem.getSuccessorsTD(state)
			NODESCREATED += len(temp)
			queue.extend(temp)
			if MAXQUEUE < len(queue):
				MAXQUEUE = len(queue)
	return (None, NODESCREATED, MAXQUEUE)
	
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

	if problem.isOneProbGoalTD(startState):
		return ([startState], NODESCREATED, MAXSTACK)

	newNodes = problem.getSuccessorsTD(startState)
	NODESCREATED += len(newNodes)
	stack.extend(newNodes )
	if MAXSTACK < len(stack):
		MAXSTACK = len(stack)

	#path = []
	#newPathFlag = False
	while not isEmpty(stack):
		#if newPathFlag is True:
			#path = []
			#newPathFlag = False
		state = stack.pop()
		#path.append(state)
		if problem.isOneProbGoalTD(state):
			return (state, NODESCREATED, MAXSTACK)
		else:
			temp = problem.getSuccessorsTD(state)
			NODESCREATED += len(temp)
			stack.extend(temp)
			if MAXSTACK < len(stack):
				MAXSTACK = len(stack)
			#if len(temp) < 1:
				#newPathFlag = True
	return (None, NODESCREATED, MAXSTACK)

def runTests():
	bannr = "\n********************************\n"
	
	src1 = Problem.coordinate(0.5,0)	
	dst1 = Problem.coordinate(1.0,0)
	origin = Problem.coordinate(0,0)
	
	#Intializing objects	
	prob1 = Problem.Problem(dst1,src1,1,1,1)
	startState1 = Problem.ProblemStateWithRef(origin,src1,False,0,None)
	print ("Source: ",src1.toString()," Dest: ",dst1.toString())
	
	#Check Objects
	print ("Problem: ", prob1.toString(),'\n')
	print ("State: ", startState1.toString())
	print (bannr)
	
	#Testing BFS

	print ("TESTING BFS",bannr)
	bfsQueue = BFSTD(startState1,prob1)
	print("Type of bfsQueue: ",type(bfsQueue))
	#print("WIthin it is: ", bfsQueue)
	#print("And that is: ", bfsQueue[0])
	print("Which contains: ", type(bfsQueue[0]))
	print ("Nodes created: ", str(bfsQueue[1]))
	print ("Max Queue Size: ", str(bfsQueue[2]))

	ResultsTup = bfsQueue
	numNodespath = 0
	temp = ResultsTup[0]
	print("Printing Path from goal to start")
	while temp is not None:
		numNodespath += 1
		# print in here
		print(temp.toString())
		print(bannr)
		temp = temp.parentState
	print("Depth of Search was ", numNodespath)
	print("Number of Nodes created ", ResultsTup[1])
	print("Maximum size of the heap ",ResultsTup[2])


	#Two-D testing####################################
	print(bannr,"Testing 2D",bannr)

	#Defining Points
	src2 = Problem.coordinate(0.5,0.5)
	dst2 = Problem.coordinate(1.0,1.0)
	print ("TESTPOINTS: \n","Src: ",src2.toString(),"\n Dest: ", dst2.toString())
	
	#Initializing Problem/State
	prob2 = Problem.Problem(dst2,src2,1,1,1)
	startState2 = Problem.ProblemStateWithRef(origin,src2,False,0,None)	
	print ("Problem: ",prob2.toString())
	print ("State: ", startState2.toString())

	#Testing Search
	print("TESTING 2D BFS",bannr)
	bfsQueue2 = BFSTD(startState2,prob2)
	print ("Within BFSTree is: ",type(bfsQueue2))
	#print ("And that is: ", bfsQueue2[0])
	print ("Which contains: ", type(bfsQueue2[0]))
	print ("Nodes created: ", str(bfsQueue2[1]))
	print ("Max Queue Size: ", str(bfsQueue2[2]))

	ResultsTup = bfsQueue2
	numNodespath = 0
	temp = ResultsTup[0]
	print("Printing Path from goal to start")
	while temp is not None:
		numNodespath += 1
		# print in here
		print(temp.toString())
		print(bannr)
		temp = temp.parentState
	print("Depth of Search was ", numNodespath)
	print("Number of Nodes created ", ResultsTup[1])
	print("Maximum size of the heap ", ResultsTup[2])

	#TESTING DFS 1D
	
	print (bannr,"TESTING DFS",bannr)	
	print ("runs to long, uncomment below code to run out of RAM")
# 	dfsStack = DFS(startState1,prob1)
# 	print("Type of dfsStack: ", type(dfsStack))
# 	print("Within it is: ", dfsStack)
# 	print("And that is: ", dfsStack.toString())
	
	return

	
"""
	timedTest
	a test function to track the times of the functions in this file
	not testing the time of DFS since it is a naive implementation that bottoms out without finding an answer which is expected of it
	:returns nothing
"""
def timedTest():
	origin = Problem.coordinate(0,0)
	src1 = Problem.coordinate(0.5,0)
	dest1 = Problem.coordinate(1.0,0)
	
	testProblem = Problem.Problem(dest1,src1,1,1,1)
	testState = Problem.ProblemStateWithRef(origin, dest1, False, 0,None)
	start = timer()
	bfs = BFSTD(testState, testProblem)
	end = timer()
	print("Time taken to run Breadth first search 1D: ", end - start)

	src2 = Problem.coordinate(0.5, 0.5)
	dest2 = Problem.coordinate(1.0, 1.0)

	tDProb = Problem.Problem(dest2, src2, 1, 1, 1)
	tDStart = Problem.ProblemStateWithRef(Problem.coordinate(0,0), src2, False, 0, None)
	# timing the one problem on 2D
	start = timer()
	bfs2 = BFSTD(tDStart, tDProb)
	end = timer()
	print("Time taken to run Breadth first search2D: ", end - start)

	#potentially add code for the general function here too.


	
