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
heap = []

"""
Greedy search
"""
def greedySearch(state, prob):
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
		
	newNodes []
	newNodes.extend(Problem.getSuccessors(state, problem)
	
	for value in newNodes:
		heapq.heappush(heap,(heuristicOneProb(value, prob) + value.distance, value)
	
	while not isEmpty(heap):
		currentState = heapq.heappop(heap)
		
		if Problem.isGoal(currenState,prob):
			return currentState
		else:
			newNodes.extend(Problem.getSuccessors(currentState, problem)
			for value in newNodes:
				heapq.heappush(heap,(heuristicOneProb(value, prob) + value.distance, value)
	
	return None
