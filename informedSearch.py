import heapq

"""
heuristic for the 1 problem

"""
	def heuristicOneProb(state,prob):
		estCost = 0
		if state.loaded:
			if stat.vLoc == prob.dest:
				estCost = prob.dest
			else:
				#at 0 or source
				estCost = abs(prob.dest - state.vLoc) + prob.dest
		else:
			estCost = abs(prob.src - state.vLoc) + abs(prob.src - prob.dest) + prob.dest
		
		return estCost

"""
Greedy search
"""
def greedySearch(state, prob):
	heap = []
	
	heap.extend(Problem.getSuccessors(state, problem))
	heapq.heapify(heap)
	
	while not isEmpty(heap):
		currentState = heapq.heappop(heap)
		
		if Problem.isGoal(currenState,prob):
			return currentState
		else:
			heap.extend(Problem.getSuccessors(currentState, problem))
	
	return None
	
"""
A* search
"""
def aStarSearch(state, prob):
	heap = []
	
	newNodes = []
	newNodes.extend(Problem.getSuccessors(state, problem)
	
	sequence = []
			
	for value in newNodes:
		heapq.heappush(heap,(heuristicOneProb(value, prob) + value.distance, value)
	maxSize = len(heap)
	nodesCreated = len(heap)
			       
	while not isEmpty(heap):
		currentState = heapq.heappop(heap)
		
		sequence.append(currentState)
			       
		if Problem.isGoal(currenState,prob):
			return (sequence, nodesCreated, maxSize)
		else:
			newNodes.extend(Problem.getSuccessors(currentState, problem)
			for value in newNodes:
				heapq.heappush(heap,(heuristicOneProb(value, prob) + value.distance, value)
				nodesCreated += 1
			if len(heap) > maxSize:
				maxSize = len(heap)
	
	return (sequence,nodesCreated, maxSize)
