#!user/bin/env python3
#File Search
#Contains the various uninformed search algortihms

import Problem

#Queue for BFS
queue = []

def isQueueEmpty(queue):
	return queue == []

"""
Breadth first Search of the search states to find the goal state if it exists
:param: startState the state at which the search is starting from
:param: problem the object for the current problem
:returns: the state that is found to meet the goal state or nothing if the goal is not found.
"""
def BFS( startState, problem):
	queue.extend(Problem.getSuccessors(startState, problem))
	while not isQueueEmpty(queue):
		state = queue.pop()
		if Problem.isGoal(state, problem):
			return state
		else:
			queue.extend(Problem.getSuccessors(state, problem))
	return None

