#!user/bin/env python3
#File Search
#Contains the various uninformed search algortihms

import Problem

#Starting with BFS
queue = []

def isQueueEmpty(queue):
	return queue == []

#BFS
#Does a Breadth First Search of the Search Space

def BFS( startState, problem):
	queue.extend(Problem.getSuccessors(startState, problem))
	while not isQueueEmpty(queue):
		state = queue.pop()
		if Problem.isGoal(state, problem):
			return state
		else:
			queue.extend(Problem.getSuccessors(state, problem))

