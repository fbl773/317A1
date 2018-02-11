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
	

def runTests():
	bannr = "\n********************************\n"
	
# 	src = 0.5	
# 	dst = 1.0
# 	
# 	#Intializing objects	
# 	prob = Problem.Problem(dst,src,1,1,1)
# 	startState = Problem.ProblemStateWithRef(0,src,False,0,None)
# 	print ("Source: ",src," Dest: ",dst)
# 	
# 	#Check Objects
# 	print ("Problem: ", prob.toString(),'\n')
# 	print ("State: ", startState.toString())
# 	print (bannr)
# 	
# 
# 	#Testing DFS NOT IN THIS VERSION
# 	print ("TESTING DFS",bannr)	
# 
# 	# dfsStack = DFS(startState,prob)
# # 	print("Type of dfsStack: ", type(dfsStack))
# # 	print("Within it is: ", dfsStack)
# # 	print("And that is: ", dfsStack.toString())
# 
# 	print (bannr)
# 
# 	#Testing BFS
# 	print ("TESTING BFS",bannr)
# 	bfsQueue = BFS(startState,prob)
# 	print("Type of bfsQueue: ",type(bfsQueue))
# 	print("WIthin it is: ", bfsQueue)
# 	print("And that is: ", bfsQueue[0])
# 	print("Which contains: ", type(bfsQueue[0][0]))
# 
# 
# 	print ("TEST BFS",bannr)
# 	ResultsTup = BFS(startState,prob)
# 
# 	for items in ResultsTup[0]:
# 		print(items.toString())
	
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
	bfs2Queue = BFSTwoD(startState2,prob2)
	print ("Within BFSTree is: ",bfsQueue2)
	print ("And that is: ", bfsQueue2[0])
	print ("Which contains: ", type(bfsQueue2[0][0]))
	
	print ("Holy shit you made it this far! A+ Dervs and Sarah")

	
	
	return

	
