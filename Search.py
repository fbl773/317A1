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


"""
Breadth First Search of the search states to find the goal state if it exists
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

def runTests():
	bannr = "\n********************************\n"
	
	src = float(input("Input Source: "))
	dst = float(input("Input Dest: "))
	
	#Intializing objects	
	prob = Problem.Problem(dst,src)
	startState = Problem.ProblemState(0,src,False,0)
	print ("Source: ",src," Dest: ",dst)
	
	#Check Objects
	print ("Problem: ", prob.toString(),'\n')
	print ("State: ", startState.toString())
	print (bannr)
	
	testProblem = Problem.Problem(dst,src)
	testState = Problem.ProblemState(0,src,False,0)


	#Testing DFS
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
	print("WIthin it is: ", bfsQueue)
	print("And that is: ", bfsQueue.toString())


	print ("TEST BFS",bannr)
	ResultsTup = BFS(testState,testProblem)

	for items in ResultsTup[0]:
		print(items.toString())
	
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
