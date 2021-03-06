import heapq
import Problem
from timeit import default_timer as timer
"""
heuristic for the 1 problem

"""
def heuristicOneProb(state,prob):
	estCost = 0
	if state.loaded:
		if state.vLoc == prob.dest:
			estCost = prob.dest
		else:
			#at 0 or source
			estCost = abs(prob.dest - state.vLoc) + prob.dest
	else:
		estCost = abs(prob.src - state.vLoc) + abs(prob.src - prob.dest) + prob.dest
	
	return estCost
"""
heuristic for the 1 problem but 2 dimensions

"""
def heuristicOneProb2D(state,prob):
	estCost = 0
	if state.loaded:
		if state.vLoc == prob.dest:
			estCost = prob.eudCalc((0,0), prob.dest)
		else:
			#at 0 or source
			estCost = prob.eudCalc(state.vLoc,prob.dest) + prob.eudCalc((0,0), prob.dest)
	else:
		estCost = prob.eudCalc(state.vLoc, prob.src) + prob.eudCalc(prob.src,prob.dest) + prob.eudCalc((0,0), prob.dest)
	
	return estCost
"""
heuristic for M=K=1, N=2, Y=2
This is too big to write out, several if statements too many conditions t consider
Need a better heuristic while the problem scales up
"""
# 
# def heuristicMK1NY2(state,prob):
# 	estCost = 0
# 	if state.loaded[0]:
# 		if state.vLoc == prob.dest[0]:
# 			if state.pLoc[1] == prob.dest[1]:
# 				estCost = coordinate.eudCal(prob.dest[0],(0,0)) 
# 			else:
# 				estCost = coordinate.eudCalc(prob.dest[0],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],(0,0))
# 		elif state.vLoc == prob.dest[1]:
# 			if state.pLoc[0] == prob.dest[0]:
# 				estCost = coordinate.eudCalc(prob.dest[1],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],(0,0)])
# 			else:
# 				if coordinate.eudCalc(prob.dest[1],prob.src[0]) < coordinate.eudCalc(prob.dest[1],prob.src[1]):
# 					coordinate.eudCalc(prob.dest[1],prob.src[0]) + coordinate.eudCalc(prob.src[0],prob.dest[0]) + coordinate.eudCalc(prob.dest[0],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],(0,0)) 
# 				else:
# 					coordinate.eudCalc(prob.dest[1],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],prob.src[0]) + coordinate.eudCalc(prob.src[0],prob.dest[0]) + coordinate.eudCalc(prob.dest[0],(0,0))
# 		elif state.vLoc == prob.src[0]:
# 		else:
# 	elif state.loaded[1]:
# 	elif state.loaded[0] and state.loaded[1]:	
# 	else:
# 		
# 	
# 	return estCost

"""
Alternative to brute force heuristic for M=N=1, N=Y=2
perhpas consdier the distance to get each individual package to their goal
break down the problem into a 1 problem
"""

def heuristicMN1KY2(state, prob):
	estCost = 0
	for i in range(0,len(state.pLoc),1):
		if state.pLoc[i] is not prob.dest:
			estCost = estCost + Problem.coordinate.eudCalc(state.pLoc[i],prob.dest[i])
	return estCost
			


"""
Greedy search
"""

def greedySearch(state):
	heap = []
	
	heap.extend(Problem.getSuccessors(state))
	heapq.heapify(heap)
	
	while len(heap) > 0:
		currentState = heapq.heappop(heap)
		
		if Problem.isGoal(currentState):
			return currentState
		else:
			heap.extend(Problem.getSuccessors(currentState))
	
	return None
	
"""
A* search
"""
def aStarSearch(state, prob):
	heap = []
	
	newNodes = []
	#newNodes.extend(prob.getSuccessors(state))
	
	seqPath = []
			
	#for vState in newNodes:
		#print ("Values are: ",type(vState))
		#heapq.heappush(heap,(heuristicOneProb(vState,prob) + vState.distance), vState)

	heapq.heappush(heap,(0,state))
	maxSize = len(heap)
	nodesCreated = len(heap)

	print ("Entering Loop with" )			       
	print ("Heap Length: ", maxSize)
	print ("Nodes Created", nodesCreated)
	
	while len(heap) > 0:
		currentState = heapq.heappop(heap)[1]
	#	print ("within currentState is: ", type(currentState))		

		seqPath.append(currentState)

		if prob.isGoal(currentState):
			return (seqPath, nodesCreated, maxSize)
		else:
			newNodes.extend(prob.getSuccessors(currentState))
			for vState in newNodes:
				heapq.heappush(heap,(heuristicOneProb(vState, prob) + vState.distance, vState))
				nodesCreated += 1
				newNodes.remove(vState)
			if len(heap) > maxSize:
				maxSize = len(heap)
	
	#print("Heap is: ", heap)
	return (seqPath,nodesCreated, maxSize)

"""
A* search TEST
"""
def aStarSearchWithRef(state, prob):
	heap = []
	
	newNodes = []
	#newNodes.extend(prob.getSuccessors(state))
	
	#seqPath = []
			
	#for vState in newNodes:
		#print ("Values are: ",type(vState))
		#heapq.heappush(heap,(heuristicOneProb(vState,prob) + vState.distance), vState)

	heapq.heappush(heap,(0,state))
	maxSize = len(heap)
	nodesCreated = len(heap)

	print ("Entering Loop with" )			       
	print ("Heap Length: ", maxSize)
	print ("Nodes Created", nodesCreated)
	
	while len(heap) > 0:
		currentState = heapq.heappop(heap)[1]
	#	print ("within currentState is: ", type(currentState))		

		#seqPath.append(currentState)

		if prob.isOneProbGoal(currentState):
			return (currentState, nodesCreated, maxSize)
		else:
			newNodes.extend(prob.getSuccessorsOneAStar(currentState))
			for vState in newNodes:
				heapq.heappush(heap,(heuristicOneProb(vState, prob) + vState.distance, vState))
				nodesCreated += 1
				newNodes.remove(vState)
			if len(heap) > maxSize:
				maxSize = len(heap)
	
	#print("Heap is: ", heap)
	return (None,nodesCreated, maxSize)


"""
	aStarGeneral
	A* search using our general successor This should handle a wider range of problems
	:param state: the start state of the current search is a search object.
	:param prob: the problem object for this search
	:return: returns the goal state(with references to its parents), the number of nodes created, the largest size of the heap and the largest distance travelled by one truck in a tuple
"""
def aStarGeneral(state, prob):
	#heap to sort states
	heap = []
	#temporary holder for new States
	newNodes = []

	#creating a heap out of the heap list
	heapq.heappush(heap, (0, state))
	maxSize = len(heap)
	nodesCreated = len(heap)

	while len(heap) > 0:
		currentState = heapq.heappop(heap)[1]

		#finds the maximum distance traveled and the sum of distances
		maxdist = 0
		sumdist = 0
		for dists in currentState.distance:
			sumdist += dists
			if dists > maxdist:
				maxdist = dists

		if prob.isGoal(currentState):
			return (currentState, nodesCreated, maxSize, maxdist)
		else:
			newNodes.extend(prob.getSuccessorsGeneral(currentState))
			for vState in newNodes:
				heapq.heappush(heap, (heuristicMN1KY2(vState, prob) + sumdist + 10*maxdist, vState))
				nodesCreated += 1
				newNodes.remove(vState)
			if len(heap) > maxSize:
				maxSize = len(heap)

	return (None, nodesCreated, maxSize, maxdist)


"""
	The tests for the informed search
"""
def runTests():
	bannr = "\n********************************\n"
	
	print ("TESTING INFORMED SEARCH",bannr)
	
	src = 0.5
	dst = 1.0
	
	tstProb = Problem.Problem(dst,src, 1, 1, 1)
	tstState = Problem.ProblemStateWithRef(0,src,False,0, None)

	#Validating input
	print ("Environment is: ",bannr)
	print ("Source: ", src,'\n',
		   "Dest : ", dst,'\n',
		   tstProb.toString(),'\n',
		   tstState.toString(),'\n')

	#Testing the A*
	print ("Test A*",bannr)
	"""		 
	aStar = aStarSearch(tstState, tstProb)
	print ("A* is a: ", type(aStar))
	print ("And in that is: ", aStar)

	n = 0
	for state in aStar[0]:
		try:
			print ("vLoc",n,": ",state.vLoc)
			print ("pLoc",n,": ",state.pLoc)
			print ("load",n,": ",state.loaded,bannr)
			n += 1

		except TypeError as tplsSuk:
			print (tplsSuk)
	print("The number of nodes created is ", aStar[1])
	print("The largest size the heap gets is ", aStar[2])
	"""
	"""
	This will need some syntax work 
	"""

	aStar1 = aStarSearchWithRef(tstState,tstProb)
	numNodespath = 0
	temp = aStar1[0]
	print("Printing Path from goal to start")
	while temp is not None:
		numNodespath += 1
		#print in here
		print(temp.toString())
		print(bannr)
		temp = temp.parentState
	print("Depth of Search was ", numNodespath)
	print("Number of Nodes created ", aStar1[1])
	print("Maximum size of the heap ", aStar1[2])

	#Testing 2D#######
	#print ("Testing 2D A*",bannr)

	#Testing the general case

	print("??????????????????????????????????????????????????????????????????????????????????")

	dests = [Problem.coordinate(0.5, 0.5), Problem.coordinate(1.0, 1.0)]
	srcs = [Problem.coordinate(1.5, 1.5), Problem.coordinate(0.7, 0.6)]

	genProb = Problem.Problem(dests, srcs, 1, 1, 2)

	loades = [False, False]
	dists = [0]

	genState = Problem.ProblemStateGeneral([Problem.coordinate(0, 0)], list(srcs), [loades], dists, None)

	genStar = aStarGeneral(genState, genProb)

	numNodespath = 0
	temp = genStar[0]
	print("Printing Path from goal to start")
	while temp is not None:
		numNodespath += 1
		# print in here
		print(temp.toString())
		print(bannr)
		temp = temp.parentState
	print("Depth of Search was ", numNodespath)
	print("Number of Nodes created ", genStar[1])
	print("Maximum size of the heap ", genStar[2])
	print("Max distance by one truck ", genStar[3])
	
	
	




#	print("Final State of the Problem ", tstProb.toString())

def timedTest():
	testProb = Problem.Problem(0.5, 1.0, 1, 1, 1)
	testState = Problem.ProblemStateWithRef(0, 1.0, False, 0, None)

	#timing out the 1 problem
	start = timer()
	res = aStarSearchWithRef(testState, testProb)
	end = timer()
	print(" Result of A* on MNKY = 1 is ", end - start)

	src = Problem.coordinate(0.5, 0.5)
	dest = Problem.coordinate(1.0, 1.0)

	tDProb = Problem.Problem(dest, src, 1, 1, 1)
	tDStart = Problem.ProblemStateWithRef(Problem.coordinate(0,0), src, False, 0, None)
	#timing the one problem on 2D
	start = timer()
	#res = aStarSearchWithRefTD(tDStart, tDProb )
	end = timer()

	#Add code to time for the general search.

def showcase():
	bannr = '\n*****************************\n'

	print("A* MNKY=1",bannr)

	#Initialize environment
	src = 0.5
	dst = 1.0
	tstProb = Problem.Problem(dst,src, 1, 1, 1)
	tstState = Problem.ProblemStateWithRef(0,src,False,0, None)
	aStar1 = aStarSearchWithRef(tstState,tstProb)
	numNodespath = 0
	temp = aStar1[0]

	#Showcase environment.
	print ("Environment is: ",bannr)
	print ("Source: ", src,'\n',
		"Dest : ", dst,'\n',
	        tstProb.toString(),'\n',
	        tstState.toString(),'\n')
	print("Number of Nodes created ", aStar1[1])
	print("Maximum size of the heap ", aStar1[2])

	
	#Check resultant depth
	showPath = input("Show path knowing it could be pretty deep? (y/n)")

	if (showPath is 'y'):
		while temp is not None:
			numNodespath += 1
			print(temp.toString())
			#print(bannr)
			temp = temp.parentState
		print("Depth of Search was ", numNodespath)
	

	print (bannr, "And now some time stats!",bannr)
	timedTest()	

