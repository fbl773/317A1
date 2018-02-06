#!/usr/bin/env python3
#File Search
#Contains the various uninformed search algortihms

import Problem
import collections

#Queue for BFS
queue = collections.deque([])


def isQueueEmpty(queue):
	return len(queue) == 0

def isEmpty(list):
	return list == []

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
			temp = problem.getSuccessors(state)
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

	if problem.isGoal(startState):
		return ([startState], NODESCREATED, MAXSTACK)

	newNodes = problem.getSuccessors(startState)
	NODESCREATED += len(newNodes)
	stack.extend(newNodes )
	if MAXSTACK < len(stack):
		MAXSTACK = len(stack)

	path = []
	newPathFlag = False
	while not isEmpty(stack):
		if newPathFlag is True:
			path = []
			newPathFlag = False
		state = stack.pop()
		path.append(state)
		if problem.isGoal(state):
			return (path, NODESCREATED, MAXSTACK)
		else:
			temp = problem.getSuccessors(state)
			NODESCREATED += len(temp)
			stack.extend(temp)
			if MAXSTACK < len(stack):
				MAXSTACK = len(stack)
			if len(temp) < 1:
				newPathFlag = True
	return (None, NODESCREATED, MAXSTACK)


"""
Depth Limited search of states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:param: depth the maximum depth that can be searched
:returns: the Path of the search the  number of nodes explored and the maximum size the queue was at any point
		if the search fails the path will be empty
"""
#def DLS(startState, problem, depth):
#	stack = []
#	# Records the largest size the stack reaches
#	MAXSTACK = 0
#	# Records the number of nodes created
#	NODESCREATED = 1

#	if problem.isGoal(startState):
#		return ([startState], NODESCREATED, MAXSTACK)
#	else:
#		return DLSrec(startState, problem, 0, depth, stack, MAXSTACK, NODESCREATED)

"""
Depth Limited search of states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:param: depth the max depth that can be searched
:returns: the Path of the search the  number of nodes explored and the maximum size the queue was at any point
		if the search fails the path will be empty
"""
#def DLSrec(startState, problem, curdepth, depth, stack, stackSize, numNodes):
#	if curdepth >= depth:
#		return (stack.insert(0, startState), numNodes, stackSize)
#	else:



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


	#Testing BFS
	print ("TESTING BFS",bannr)
	bfsStack = BFS(startState,prob)
	print("DFS returns a ", type(bfsStack))
	print("The number of nodes created is ", bfsStack[1])
	print("The Largest size of the queue is ", bfsStack[2])

	print("The Path contains: ")
	if len(bfsStack[0]) > 0:
		for items in bfsStack[0]:
			print(items.toString())
	else:
		print("Nothing")

	# Testing DFS
	dfsStack = DFS(startState, prob)
	print("TESTING DFS", bannr)
	print("DFS returns a ", type(dfsStack))
	print("The Return value contains", dfsStack)
	print("The Path contains: ")
	if dfsStack[0] is not None:
		for items in dfsStack[0]:
			print(items.toString())
	else:
		print("Nothing")
	
	return


