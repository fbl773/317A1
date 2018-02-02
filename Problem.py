#!/usr/bin/env python3
#File Problem
#Contains the object for the problem state and functions to act on the problem

#ProblemState
#Object to hold a state of the problem
class ProblemState(object):
	vLoc = 0
	pLoc = ""
	loaded = False
	distance = 0

	def __init__(self, vLoc, pLoc, loaded, distance): 
		self.vLoc = vLoc
		self.pLoc = pLoc
		self.loaded = loaded
		self.distance = distance

"""
 Problem
  the problem for the function
  This will need to be refactored in order to handle more general cases
"""
class Problem:
	dest = ""
	src = ""
	trucks = 1

	#Construtor for the problem
	def __init__(self, dest, source): 
		self.dest = dest
		self.src = source

	"""
	isGoal()
	Goal checking function
		Check that vehicle is back in garage and package at destination
		param: state - the Problem state to check
		prob  - the current problem to check against
		return: true of the state matches the goal state false otherwise
	"""
	def isGoal( state, prob):
		if state.vLoc == 0 and state.pLoc == prob.dest:
			return True
		else:
			return False

	"""
	getSuccessors
	 Returns a list of the possible moves that to be searched through
	 param: curState - the current state in the search
	"""
	def getSuccessors(state, prob):
		newStates = []
		if state.vLoc == 0:
			newStates.append( ( prob.src, state.pLoc, state.loaded, state.distance+newDist ) )
			newStates.append((prob.dest, state.pLoc, state.loaded, state.distance + newDist) )
		elif state.vLoc == prob.src :
			if state.loaded == False:
				newStates.append((state.vLoc, state.pLoc, True, state.distance))
			else:
				newStates.append((0, 0, state.loaded, state.distance + newDist))
				newStates.append((prob.dest, prob.dest, state.loaded, state.distance + newDist))
		else:
			if state.loaded == True:
				newStates.append((state.vLoc, state.pLoc, False, state.distance))
			else:
				newStates.append((0, 0, state.loaded, state.distance + newDist))
				newStates.append((prob.src, prob.src, state.loaded, state.distance + newDist))