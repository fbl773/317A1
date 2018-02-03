#!/usr/bin/env python3
#File Problem
#Contains the object for the problem state and functions to act on the problem

#ProblemState
#Object to hold a state of the problem
class ProblemState(object):
	vLoc = 0
	pLoc = 0
	loaded = False
	distance = 0

	def __init__(self, vLoc, pLoc, loaded, distance): 
		self.vLoc = vLoc
		self.pLoc = pLoc
		self.loaded = loaded
		self.distance = distance
	"""
	toString()
	- Returns a string represntation Problem state Attributes
	"""
	def toString(self):
		bannr = "\n****PROBLEM_STATE****\n"
		return (bannr + "vLoc: " +str(self.vLoc) + '\n' +
				"pLoc: " + str(self.pLoc) + '\n'+
				"loaded: " + str(self.loaded) + '\n' +
				"distance: " + str(self.distance) + '\n') 
	
	def __lt__(self, other):
    		return self.distance < other.distance


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
	toString()
	- Returns a string representation of the Problem Object
	"""
	def toString(self):
		bannr = "\n****PROBLEM****\n"
		return(bannr + "Destination:Source" + '\n' +
			  str(self.dest) + ':' + str(self.src))
	"""
	isGoal()
	Goal checking function
		Check that vehicle is back in garage and package at destination
		param: state - the Problem state to check
		prob  - the current problem to check against
		return: true of the state matches the goal state false otherwise
	"""
	def isGoal( self, state, prob):
		if state.vLoc == 0 and state.pLoc == prob.dest:
			return True
		else:
			return False

	"""
	getSuccessors
	 Returns a list of the possible moves that to be searched through
	 param: curState - the current state in the search
	"""
	def getSuccessors(self,state):
		newStates = []
		if state.vLoc == 0:
			newStates.append( ProblemState(self.src, state.pLoc, state.loaded, state.distance + abs(self.src - state.vLoc)) )
			newStates.append(ProblemState(self.dest, state.pLoc, state.loaded, state.distance + abs(self.dest - state.vLoc )) )
		elif state.vLoc == self.src :
			if state.loaded == False:
				newStates.append(ProblemState(state.vLoc, state.pLoc, True, state.distance))
				#also consider that it doesn't pick up package and move without package
				newStates.append(ProblemState(self.dest, state.pLoc, state.loaded, state.distance + abs(self.dest - state.vLoc )) )
				newStates.append(ProblemState(0, state.pLoc, state.loaded, state.distance + abs(0 - state.vLoc )) )
			else:
				newStates.append(ProblemState(0, 0, state.loaded, state.distance + abs(0 - state.vLoc )))
				newStates.append(ProblemState(self.dest, self.dest, state.loaded, state.distance + abs(self.dest - state.vLoc )))
		else:
			if state.loaded == True:
				newStates.append(ProblemState(state.vLoc, state.pLoc, False, state.distance))
				#also consider when it doesnt do the smart thing
				newStates.append( ProblemState( self.src, state.pLoc, state.loaded, state.distance + abs(self.src - state.vLoc )) )
				newStates.append(ProblemState( 0, state.pLoc, state.loaded, state.distance + abs(0 - state.vLoc)) )
			else:
				newStates.append(ProblemState(0, 0, state.loaded, state.distance + abs(0 - state.vLoc)))
				newStates.append(ProblemState(self.src, self.src, state.loaded, state.distance + abs(self.src - state.vLoc)))
		return newStates

def runTests():
	print ("Begin Algorithm Code Program")

	src = float(input("Source Coordinate: "))
	dest = float(input("Destination Coordinate: "))

	#Testing Input validity
	print ("src: ",src, " dest: ", dest)
	print ("Sum is: ", src + dest)

	#Testing State Declaration
	startState = ProblemState(0,src,False,0)
	if startState is None:
		print ("No no no no no no no no no no none")
	else:
		print ("StartState is not None: ", startState.toString())

	#Testing Problem Declaration
	aProblem = Problem(src,dest)
	print (aProblem.toString())

	#Testing Successor Function
	successorList = aProblem.getSuccessors(startState)
	successors = ''	
	for s in successorList:
		successors += s.toString()

	print("Type of Succesors is: ", type(successorList))
	print(" And it Contains: ", successors)


