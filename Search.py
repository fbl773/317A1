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
	#Records the largest size the stack reaches
	MAXSTACK = 0
	#Records the number of nodes created
	NODESCREATED = 1

	if problem.isGoal(startState):
		return startState

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
			stack.extend(temp)
			if len(temp) < 1:
				newPathFlag = True
	return (None, NODESCREATED, MAXSTACK)


"""
Depth Limited search of states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the state that is found to meet the goal state or nothing if the goal is not found.
"""



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

	#Testing DFS
	print ("TESTING DFS",bannr)

	dfsStack = DFS(startState,prob)
	#Testing BFS
	print ("TESTING BFS",bannr)
	bfsQueue = BFS(startState,prob)
	print("Type of bfsQueue: ",type(bfsQueue))
	print("WIthin it is: ", bfsStack)
	print("And that is: ", bfsStack.toString())

	print("DFS returns a ", type(dfsStack))
	print("The Return value contains", dfsStack)

	print ("TEST BFS",bannr)
	ResultsTup = BFS(testState,testProblem)
	if dfsStack[0] is not None:
		print("The Path contains: ")
		for items in dfsStack[0]:
			print(items.toString())

	for items in ResultsTup[0]:
		print(items.toString())
	
	return


