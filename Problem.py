#!/usr/bin/env python3
#File Problem
#Contains the object for the problem state and functions to act on the problem

#ProblemState
#Object to hold a state of the problem
class ProblemState(object):
	vLoc = 0.0 
	pLoc = 0.0
	loaded = ''
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
			newStates.append( ProblemState(prob.src, state.pLoc, state.loaded, state.distance + abs(prob.src - state.vLoc)) )
			newStates.append(ProblemState(prob.dest, state.pLoc, state.loaded, state.distance + abs(prob.dest - state.vLoc )) )
		elif state.vLoc == prob.src :
			if state.loaded == False:
				newStates.append(ProblemState(state.vLoc, state.pLoc, True, state.distance))
				#also consider that it doesn't pick up package and move without package
				newStates.append(ProblemState(prob.dest, state.pLoc, state.loaded, state.distance + abs(prob.dest - state.vLoc )) )
				newStates.append(ProblemState(0, state.pLoc, state.loaded, state.distance + abs(0 - state.vLoc )) )
			else:
				newStates.append(ProblemState(0, 0, state.loaded, state.distance + abs(0 - state.vLoc )))
				newStates.append(ProblemState(prob.dest, prob.dest, state.loaded, state.distance + abs(prob.dest - state.vLoc )))
		else:
			if state.loaded == True:
				newStates.append(ProblemState(state.vLoc, state.pLoc, False, state.distance))
				#also consider when it doesnt do the smart thing
				newStates.append( ProblemState( prob.src, state.pLoc, state.loaded, state.distance + abs(prob.src - state.vLoc )) )
				newStates.append(ProblemState( 0, state.pLoc, state.loaded, state.distance + abs(0 - state.vLoc)) )
			else:
				newStates.append(ProblemState(0, 0, state.loaded, state.distance + abs(0 - state.vLoc)))
				newStates.append(ProblemState(prob.src, prob.src, state.loaded, state.distance + abs(prob.src - state.vLoc)))
		return newStates

#MAIN
print ("Begin Algorithm Code Program")

src = int(input("Source Coordinate: "))
dest = int(input("Destination Coordinate: "))

print ("src: ",src, " dest: ", dest)
print ("Sum is: ", src + dest)


