#!/usr/bin/env python3
#File Search
#Contains the various uninformed search algortihms

import Problem

#Queue for BFS
queue = []

def isEmpty(list):
	return queue == []

"""
Breadth First Search of the search states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the state that is found to meet the goal state or nothing if the goal is not found.
"""
def BFS( startState, problem):
	queue.extend(Problem.getSuccessors(startState, problem))
	while not isEmpty(queue):
		state = queue.pop()
		if Problem.isGoal(state, problem):
			return state
		else:
			queue.extend(Problem.getSuccessors(state, problem))
	return None

#Stack for DFSs
stack = []

"""
Depth first search  of states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the state that is found to meet the goal state or nothing if the goal is not found.
"""
def DFS(startState, problem):
	if Problem.isGoal(startState, problem):
		return startState
	stack.extend(Problem.getSuccessors(startState, problem))
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
		stack.extend(Problem.getSuccessors(state, problem))



def runTests():
	bannr = "\n********************************\n"
	
	src = float(input("Input Source: "))
	dst = float(input("Input Dest: "))
	
	#Intializing objects	
	prob = Problem.Problem(src,dst)
	startState = Problem.ProblemState(0,src,False,0)
	
	print ("TESTING DFS",bannr)
	
	#Checking input	
	print ("Source: ",src," Dest: ",dst)
	
	print (bannr)

	#Check Objects
	print ("Problem: ", prob.toString())
	print ("State: ", startState.toString())

	#Testing DFS
	dfsStack = DFS(startState,prob)
	
	print("Type of dfsStack: ", type(dfsStack))
	print("Within it is: ", defStack)	

	return

	

#Main
runTests()	



