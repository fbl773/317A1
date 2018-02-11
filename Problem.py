#!/usr/bin/env python3
#File Problem
#Contains the object for the problem state and functions to act on the problem

import copy
import math

#ProblemState
#Object to hold a state of the problem
#Does not have reference to itself
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
#ProblemState
#Object to hold a state of the problem
#with reference to itself
class ProblemStateWithRef(object):
	vLoc = 0
	pLoc = 0
	loaded = False
	distance = 0
	parentState = None

	def __init__(self, vLoc, pLoc, loaded, distance, parent):
		self.vLoc = vLoc
		self.pLoc = pLoc
		self.loaded = loaded
		self.distance = distance
		self.parentState = parent
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
Coordinate object
used for representing a point in 2D space
"""
class coordinate(object):
	x = 0.0
	y = 0.0
	
	def __init__(self, newX, newY):
		self.x = newX
		self.y = newY
	
	"""
	eudCalc()
		calculate euclidean distance bewteen 2 points
	"""
	def eudCalc(cord1,cord2):
		return math.sqrt((cord1.x - cord2.x)**2 + (cord1.y - cord2.y)**2)
	
	def getXY(self):
		coord = []
		coord.append(str(self.x))
		coord.append(str(self.y))
		return coord

	def toString(self):
		xy = self.getXY()
		#print ("XY IS: ", type(xy), ' ', xy)
		joined = ','.join(xy)
		#print ("Joined is: " , joined)
		retMe = '('+joined+')'
		return retMe
"""
 Problem
  Class to store the problem successor function
  This will need to be refactored in order to handle more general cases
"""
class Problem:
	dest = ""
	src = ""
	trucks = 1
	k = 1
	packages = 1
	
	#Construtor for the problem
	def __init__(self,dest,source,trucks,capacity,packages):
		self.dest = dest
		self.src = source
		self.trucks = trucks
		self.k = capacity
		self.packages = packages
	
	""" 
	toString()
	- Returns a string representation of the Problem Object
	"""
	def toString(self):
		bannr = "\n****PROBLEM****\n"
		return(bannr + "Destination:Source" + '\n' +
			  str(self.dest.toString()) + ':' + str(self.src.toString()))
	"""
	isOneProbGoal()
	one problem Goal checking function
		Check that vehicle is back in garage and package at destination
		For the '1 Problem' where M=N=K=Y=1
		param: state - the Problem state to check
		prob  - the current problem to check against
		return: true of the state matches the goal state false otherwise
	"""
	def isOneProbGoal( self, state):
		if state.vLoc == 0 and state.pLoc == self.dest:
			return True
		else:
			return False
	"""
	isOneProbGoalTD()
	one problem Goal checking function for Y = 2
		Check that vehicle is back in garage and package at destination
		For the '1 Problem' where M=N=K=Y=1
		param: state - the Problem state to check
		prob  - the current problem to check against
		return: true of the state matches the goal state false otherwise
	"""
	def isOneProbGoalTD( self, state):
		if state.vLoc == (0,0) and state.pLoc == self.dest:
			return True
		else:
			return False
	"""
	isGoal()
	generalized Goal checking function
		Check that vehicle is back in garage and package at destination
		Can be used for higher variations of the problem
		param: state - the Problem state to check
		prob  - the current problem to check against
		return: true of the state matches the goal state false otherwise
	"""
	def isGoal(self, state):
		for t in range( self.trucks):
			if state.vLoc[t] != (0,0):
				return False
		for p in range( self.packages):
			if state.pLoc[p] != self.dest[p]:
				return False		
		return True
	
	"""
	packageLoaded()
		Check if package (as specified by index referring to pLoc) is loaded on a vehicle
		True if loaded on a vehicle, False otherwise
	"""
	def packageLoaded(self, state, index):
		for t in range(0,self.trucks,1):
			if index+1 in state.loaded[t]:
				return True
		return False

	"""
	getSuccessors
	only for one problem
	 Returns a list of the possible moves that to be searched through
	 used for the 1 problem
	 param: curState - the current state in the search
	"""
	def getOneProbSuccessors(self,state):
		newStates = []
		if state.vLoc == 0:
			if state.loaded:
				newStates.append( ProblemState(self.src, self.src, state.loaded, state.distance + abs(self.src - state.vLoc)) )
				newStates.append(ProblemState(self.dest, self.dest, state.loaded, state.distance + abs(self.dest - state.vLoc )) )
			else:
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
				#only legal state to drop off package.
				newStates.append(ProblemState(state.vLoc, state.pLoc, False, state.distance))
				#also consider when it doesnt do the smart thing
				newStates.append(ProblemState(0, 0, state.loaded, state.distance + abs(0 - state.vLoc)))
				newStates.append(ProblemState(self.src, self.src, state.loaded, state.distance + abs(self.src - state.vLoc)))
			else:
				newStates.append( ProblemState( self.src, state.pLoc, state.loaded, state.distance + abs(self.src - state.vLoc )) )
				newStates.append(ProblemState( 0, state.pLoc, state.loaded, state.distance + abs(0 - state.vLoc)) )
				
		return newStates
	"""
	getSuccessorsOneAStar
	for one prob
	 Returns a list of the possible moves that to be searched through
	 used for the 1 problem
	 param: curState - the current state in the search
	"""
	def getSuccessorsOneAStar(self,state):
		newStates = []
		if state.vLoc == 0:
			if state.loaded:
				newStates.append( ProblemStateWithRef(self.src, self.src, state.loaded, state.distance + abs(self.src - state.vLoc), state))
				newStates.append(ProblemStateWithRef(self.dest, self.dest, state.loaded, state.distance + abs(self.dest - state.vLoc ), state) )
			else:
				newStates.append( ProblemStateWithRef(self.src, state.pLoc, state.loaded, state.distance + abs(self.src - state.vLoc), state) )
				newStates.append(ProblemStateWithRef(self.dest, state.pLoc, state.loaded, state.distance + abs(self.dest - state.vLoc ), state) )
		elif state.vLoc == self.src :
			if state.loaded == False:
				newStates.append(ProblemStateWithRef(state.vLoc, state.pLoc, True, state.distance,state))
				#also consider that it doesn't pick up package and move without package
				newStates.append(ProblemStateWithRef(self.dest, state.pLoc, state.loaded, state.distance + abs(self.dest - state.vLoc), state))
				newStates.append(ProblemStateWithRef(0, state.pLoc, state.loaded, state.distance + abs(0 - state.vLoc ), state))
			else:
				newStates.append(ProblemStateWithRef(0, 0, state.loaded, state.distance + abs(0 - state.vLoc), state))
				newStates.append(ProblemStateWithRef(self.dest, self.dest, state.loaded, state.distance + abs(self.dest - state.vLoc), state))
		else:
			if state.loaded == True:
				#only legal state to drop off package.
				newStates.append(ProblemStateWithRef(state.vLoc, state.pLoc, False, state.distance,state))
				#also consider when it doesnt do the smart thing
				newStates.append(ProblemStateWithRef(0, 0, state.loaded, state.distance + abs(0 - state.vLoc), state))
				newStates.append(ProblemStateWithRef(self.src, self.src, state.loaded, state.distance + abs(self.src - state.vLoc), state))
			else:
				newStates.append(ProblemStateWithRef( self.src, state.pLoc, state.loaded, state.distance + abs(self.src - state.vLoc ), state))
				newStates.append(ProblemStateWithRef( 0, state.pLoc, state.loaded, state.distance + abs(0 - state.vLoc), state))
				
		return newStates
	
	"""
	getSuccessorsTD
	one problem but 2 dimensions
	 Returns a list of the possible moves that to be searched through
	 used for the 1 problem in 2D
	 param: curState - the current state in the search
	"""
	def getSuccessorsTD(self,state):
		newStates = []
		if state.vLoc == 0:
			newStates.append( ProblemState(self.src, state.pLoc, state.loaded, state.distance + coordinate.eudCalc((0,0), self.src)) )
			newStates.append(ProblemState(self.dest, state.pLoc, state.loaded, state.distance + coordinate.eudCalc((0,0), self.dest)) )
		elif state.vLoc == self.src :
			if state.loaded == False:
				newStates.append(ProblemState(state.vLoc, state.pLoc, True, state.distance))
				#also consider that it doesn't pick up package and move without package
				newStates.append(ProblemState(self.dest, state.pLoc, state.loaded, state.distance + coordinate.eudCalc(state.vLoc, self.dest)))
				newStates.append(ProblemState((0,0), state.pLoc, state.loaded, state.distance + coordinate.eudCalc(state.vLoc, (0,0))) )
			else:
				newStates.append(ProblemState((0,0), (0,0), state.loaded, state.distance + coordinate.eudCalc(state.vLoc, (0,0))))
				newStates.append(ProblemState(self.dest, self.dest, state.loaded, state.distance +  coordinate.eudCalc(state.vLoc, self.dest)))
		else:
			if state.loaded == True:
				newStates.append(ProblemState(state.vLoc, state.pLoc, False, state.distance))
				#also consider when it doesnt do the smart thing
				newStates.append(ProblemState((0,0), (0,0), state.loaded, state.distance + coordinate.eudCalc(state.vLoc, (0,0))))
				newStates.append(ProblemState(self.src, self.src, state.loaded, state.distance +  coordinate.eudCalc(state.vLoc, self.src)))
			else:
				newStates.append( ProblemState( self.src, state.pLoc, state.loaded, state.distance + coordinate.eudCalc(state.vLoc, self.src)) )
				newStates.append(ProblemState( (0,0), state.pLoc, state.loaded, state.distance + coordinate.eudCalc(state.vLoc, (0,0))) )
		return newStates
	
	"""
	getSuccessorsGeneral
	should work for any values M N K (assume Y = 2)
	 Returns a list of the possible moves that to be searched through
	 Can be used for higher order problems
	 param: curState - the current state in the search
	"""
	def getSuccessorsGeneral(self, state):
		newStates = []
		
		for t in range(0,self.trucks,1):
		
			if len(state.loaded[t]) is self.k:
				#truck is full, legal moves is to drop something off
				
				for i in range (0,self.k,1):
					pIndex = state.loaded[t][i] - 1
					if state.vLoc[t] == self.dest[pIndex]:
						#truck is loaded with a package and is at that package's dest
						#only legal move is to drop off package i
						cState = copy.copy(state)
						cState.loaded[t].remove(pIndex)
						newStates.append(cState)
						#distance doesn't change
					else:
						#need to move to package i dest
						cState = copy.copy(state)
						cState.distance[t] += coordinate.eudCalc(state.vLoc[t],self.dest[pIndex])
						cState.vLoc[t] = self.dest[pIndex]
						#need to update pacakge locations
						for x in range(0,self.k,1):
							newPI = state.loaded[t][x] - 1
							cState.pLoc[newPI] = self.dest[pIndex]
						newStates.append(cState) 
			
			elif len(state.loaded[t]) is 0:
				#if truck has no packages, either go home or get new package
				cState = copy.copy(state)
				cState.distance[t] += coordinate.eudCalc(state.vLoc[t],(0,0))
				newStates.append(cState)
				
				#check packages not loaded and at a source
				for p in range (0,self.packages,1):
					if state.pLoc[p] == self.src[p] and not self.packageLoaded(state,p):
						if state.vLoc[t] == self.src[p]:
							#pick up package
							cState = copy.copy(state)
							cState.loaded[t].append(p+1)
							newStates.append(cState)
						else:
							#go to a new package
							cState = copy.copy(state)
							cState.distance[t] += coordinate.eudCalc(state.vLoc[t],self.src[p])
							cState.vLoc[t] = self.src[p]
							newStates.append(cState)						
				
			else:
				#truck has room for more packages and is not empty
				#it can get another package or it can drop off its package
				for i in range (0,len(state.loaded[t]),1):
					#of packages loaded if at the destination drop it off otherwise go to dest
					pIndex = state.loaded[t][i] - 1
					if state.vLoc[t] == self.dest[pIndex]:
						cState = copy.copy(state)
						cState.loaded[t].remove(pIndex)
						newStates.append(cState)
					else:
						#go to destination
						cState = copy.copy(state)
						cState.distance[t] += coordinate.eudCalc(state.vLoc[t],self.dest[pIndex])
						cState.vLoc[t] = self.dest[pIndex]
						#need to update pacakge locations
						for x in range(0,self.k,1):
							newPI = state.loaded[t][x] - 1
							cState.pLoc[newPI] = self.dest[pIndex]
						newStates.append(cState)
				#get new package
				for p in range (0,self.packages,1):
					if state.pLoc[p] == self.src[p] and not self.packageLoaded(state,p):
						if state.vLoc[t] == self.src[p]:
							#pick up package
							cState = copy.copy(state)
							cState.loaded[t].append(p+1)
							newStates.append(cState)
						else:
							#go to a new package
							cState = copy.copy(state)
							cState.distance[t] += coordinate.eudCalc(state.vLoc[t],self.src[p])
							cState.vLoc[t] = self.src[p]
							for x in range(0,len(state.loaded[t]),1):
								newPI = state.loaded[t][x] - 1
								cState.pLoc[newPI] = self.src[p]
							newStates.append(cState)
				
		return newStates

#--------------------------------------------------
#Test for the 1 problem renae functions for when change old function names
def runTests():
	print ("Begin Algorithm Code Program")
	
	#for Y = 1
	bannr = '\n*****************************\n'

# 	src = 0.5		
# 	dest = 1.0 
# 
# 	"""
# 	#taking in 2D, sohuld work for 1D as well
# 	
# 	sinput = []
# 	dinput = []
# 	
# 	Y = int(input("Number of dimensions: "))
# 	sources = input("Space seperated list of package sources: ")
# 	sinput.extend(sources.split(' '))
# 	destinations = input("Space seperated list of package destinations: ")
# 	dinput.extend(destinations.split(' '))
# 	
# 	src = []
# 	dest = []
# 
# 	if( Y ==1):
# 		for value in sinput:
# 			src.append(float(value))
# 		for value in dinput:
# 			dest.append(float(value))
# 	else: #assume y =2 	
# 		for i in range(1,len(sinput),2):
# 			coord = coordinate(i, i+1)
# 			src.append(coord)
# 		for i in range(1,len(dinput),2):
# 			coord = coordinate(i, i+1)
# 			dest.append(coord)
# 	"""
# 	
# 	
# 	#Testing Input validity
# 	print ("src: ",src, " dest: ", dest)
# 
# 	#Testing State Declaration
# 	startState = ProblemState(0,src,False,0) # was startState = ProblemState(0,src,False,0) change back if error ~sarah
# 	if startState is None:
# 		print ("No no no no no no no no no no none")
# 	else:
# 		print ("StartState is not None: ", startState.toString())
# 
# 	print (bannr)
# 
# 	#Testing Problem Declaration
# 	aProblem = Problem(dest,src,1,1,1)
# 	print (aProblem.toString())
# 
# 	print (bannr)
# 
# 	#Testing Successor Function
# 	successorList = aProblem.getOneProbSuccessors(startState)
# 	successors = ''	
# 	for s in successorList:
# 		successors += s.toString()
# 
# 	print("Type of Succesors is: ", type(successorList))
# 	print(" And it Contains: ", successors)

	#Testing 2d problems
	print("Testing 2D",bannr)
	
	src = coordinate(0.5,0.5)
	dest = coordinate(1.0,1.0)	
	print("Source is: " , src.toString())
	print("Destination is: ", dest.toString())
	
	#Attempting initialization w/ coordinates
	aProblem2 = Problem(dest,src,1,1,1)	
	print("2DProblem: ",aProblem2.toString())
	
	print ("Type of 2DtoString: ", type(aProblem2.toString()))
	print (" And that string is: ", aProblem2.toString())


	
	#Time to find those successors!
	startState2 = ProblemStateWithRef(0,src,False,0,None)
	print("2DState: ", startState2.toString())
	
	#And now the moment we've all been waiting for!
	#successors2 = aProblem2.getSuccessorsTD(startState2)





	print (bannr, "PROBLEM MODULE TESTING FINISHED",bannr)
		
