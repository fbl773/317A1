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
