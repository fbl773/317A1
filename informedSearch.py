import heapq
import Problem
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
			estCost = coordinate.eudCalc((0,0), prob.dest)
		else:
			#at 0 or source
			estCost = coordinate.eudCalc(state.vLoc,prob.dest) + coordinate.eudCalc((0,0), prob.dest)
	else:
		estCost = coordinate.eudCalc(state.vLoc, prob.src) + coordinate.eudCalc(prob.src,prob.dest) + coordinate.eudCalc((0,0), prob.dest)
	
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
"""
def heuristicMN1KY2(state, prob):
	estCost = 0
	for i in range(0,len(state.pLoc),1):
		if stat.pLoc[0] is not prob.dest:
			estCost = estCost + coordinate.eudCalc(state.pLoc[i],prob.dest[i])
	return estCost
			
"""	

"""
Greedy search
"""
def greedySearch(state):
	heap = []
	
	heap.extend(Problem.getSuccessors(state))
	heapq.heapify(heap)
	
	while not isEmpty(heap):
		currentState = heapq.heappop(heap)
		
		if Problem.isGoal(currenState):
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
	newNodes.extend(prob.getSuccessors(state))
	
	seqPath = []
			
	for value in newNodes:
		heapq.heappush(heap,(heuristicOneProb(value,prob) + value.distance, value))
	maxSize = len(heap)
	nodesCreated = len(heap)
			       
	while len(heap) > 0:
		currentState = heapq.heappop(heap)
		
		seqPath.append(currentState)
			       
		if prob.isGoal(prob):
			return (seqPath, nodesCreated, maxSize)
		else:
			newNodes.extend(prob.getSuccessors(currentState))
			for value in newNodes:
				heapq.heappush(heap,(heuristicOneProb(value, prob)) + value.distance, value)
				nodesCreated += 1
			if len(heap) > maxSize:
				maxSize = len(heap)
	
	return (seqPath,nodesCreated, maxSize)


"""
	The tests for the informed search
"""
def runTests():
	bannr = "\n********************************\n"
	
	print ("TESTING INFORMED SEARCH",bannr)
	
	src = 0.5
	dst = 1.0
	
	tstProb = Problem.Problem(dst,src)
	tstState = Problem.ProblemState(0,src,False,0)

	#Validating input
	print ("Environment is: ",bannr)
	print ("Source: ", src,'\n',
		   "Dest : ", dst,'\n',
		   tstProb.toString(),'\n',
		   tstState.toString(),'\n')

	#Testing the A*
	print ("Test A*",bannr)
		 
	aStar = aStarSearch(tstState, tstProb)
