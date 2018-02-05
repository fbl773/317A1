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
	return (None, NODESCREATED, MAXQUEUE)

#Stack for DFSs
stack = []

"""
Depth first search  of states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the state that is found to meet the goal state or nothing if the goal is not found.
"""
def DFS(startState, problem):
	if problem.isGoal(startState):
		return startState
	#print ("about to append: ",problem.getSuccessors(startState))
	stack.extend(problem.getSuccessors(startState)
	return DFSRec(stack, problem)


"""
Recursive Helper for Depth first search
:param: stack of the states in the problem
:param: problem the object for the current problem
:returns: the state that is found to meet the goal or nothing if it does not
"""
def DFSRec(stack, problem):
	if isEmpty(stack):
		return None
	else:
		state = stack.pop()
		if Problem.isGoal(state):
			return state
		stack.extend(Problem.getSuccessors(state))



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
	print("WIthin it is: ", bfsStack)
	print("And that is: ", bfsStack.toString())


	print ("TEST BFS",bannr)
	ResultsTup = BFS(testState,testProblem)

	for items in ResultsTup[0]:
		print(items.toString())
	
	return

	
