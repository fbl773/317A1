import heapq

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

"""
	def heuristicMK1NY2(state,prob):
		estCost = 0
		if state.loaded[0]:
			if state.vLoc == prob.dest[0]:
				if state.pLoc[1] == prob.dest[1]:
					estCost = coordinate.eudCalc(prob.dest[0],(0,0)]) 
				else:
					estCost = coordinate.eudCalc(prob.dest[0],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],(0,0))
			elif state.vLoc == prob.dest[1]:
				if state.pLoc[0] == prob.dest[0]:
					estCost = coordinate.eudCalc(prob.dest[1],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],(0,0)])
				else:
					if coordinate.eudCalc(prob.dest[1],prob.src[0]) < coordinate.eudCalc(prob.dest[1],prob.src[1]):
						coordinate.eudCalc(prob.dest[1],prob.src[0]) + coordinate.eudCalc(prob.src[0],prob.dest[0]) + coordinate.eudCalc(prob.dest[0],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],(0,0)) 
					else:
						coordinate.eudCalc(prob.dest[1],prob.src[1]) + coordinate.eudCalc(prob.src[1],prob.dest[1]) + coordinate.eudCalc(prob.dest[1],prob.src[0]) + coordinate.eudCalc(prob.src[0],prob.dest[0]) + coordinate.eudCalc(prob.dest[0],(0,0))
		elif state.loaded[1]:
		
		else:
			estCost = coordinate.eudCalc(state.vLoc, prob.src) + coordinate.eudCalc(prob.src,prob.dest) + coordinate.eudCalc((0,0), prob.dest)
		
		return estCost
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
	newNodes.extend(Problem.getSuccessors(state)
	
	sequence = []
			
	for value in newNodes:
		heapq.heappush(heap,(heuristicOneProb(value,prob) + value.distance, value)
	maxSize = len(heap)
	nodesCreated = len(heap)
			       
	while not isEmpty(heap):
		currentState = heapq.heappop(heap)
		
		sequence.append(currentState)
			       
		if Problem.isGoal(currenState,prob):
			return (sequence, nodesCreated, maxSize)
		else:
			newNodes.extend(Problem.getSuccessors(currentState)
			for value in newNodes:
				heapq.heappush(heap,(heuristicOneProb(value, prob) + value.distance, value)
				nodesCreated += 1
			if len(heap) > maxSize:
				maxSize = len(heap)
	
	return (sequence,nodesCreated, maxSize)
