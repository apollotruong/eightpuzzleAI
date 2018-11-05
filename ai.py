import numpy as np
import math
import collections
import itertools

##############################################################

w, h = 3, 3;

# Inputted puzzle #
userpuzzle = [[0 for x in range(w)] for y in range(h)] 
userpuzzle[0] = [1,2,3]
userpuzzle[1] = [4,5,0]
userpuzzle[2] = [7,8,6]

# Respective [0,1,2,3,4,5,6,7,8,9] indexes for solution
solnPosRow = [2,0,0,0,1,1,1,2,2,2]
solnPosCol = [2,0,1,2,0,1,2,0,1,2]

###############################################################

# Manhattan Distance !!
# Takes the distance of parameters 1RC , 2RC respectively
def distance(t0,t1,s0,s1):
	return math.fabs(t0 - s0) + math.fabs(t1 - s1)

# Check the distance from x to its supposed position 1-8
def distanceCheck(M,x):
	d = distance(findRow(M,x),findCol(M,x),defaultPosRow[x],defaultPosCol[x])
	return d

def manhattanDistanceCheck(M):
	sum = 0
	for i in range(8):
		sum = sum + distanceCheck(M,i)
	return sum

class Puzzle:
	def __init__(self,M):
		self.board = M

	def compareSoln(self):
		soln = [[0 for x in range(w)] for y in range(h)] 
		soln[0] = [1,2,3]
		soln[1] = [4,5,6]
		soln[2] = [7,8,0]

		if self.board == soln:
			print("GOAL!!! SOLVED!!")
			return 1
		else:
			return 0

	def copy(self):
		board = self.board
		return board

	def puzzlePrint(M):
		print(np.matrix(self.board))
		print()

# Find the row of the x
def findRow(M,x):
	for i in range(w):
		for j in range(h):
			if M[i][j] == x:
				return i
# Find the column of the x
def findCol(M,x):
	for i in range(w):
		for j in range(h):
			if M[i][j] == x:
				return j
	

class Node:
	def __init__(self,state=None,parent=None,cost=0,depth=0,children=[]):
		self.state = state 
		self.parent = parent
		self.cost = cost
		self.depth = depth
		self.children = children

	def is_goal(self,goal_state):
		return is_goal_state(self.state, goal_state)

	def expand(self):
		new_states = operator(self.state)
		self.children = []
		for state in new_states:
			self.children.append(Node(state,self,self.cost + 1,self.depth + 1))


	def parents(self):
		current_node = self
		while current_node.parent:
			yield current_node.parent:
			current_node = current_node.parent

	def gn(self):
		costs = self.cost
		for parent in self.parents():
			costs += parent.cost

		return costs

# Queue Class came from
# http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaQueueinPython.html
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class SearchAlg:
	# use start as Puzzle obj
	def __init__(self,start):
		self.start = start

	def solve(self):
		q = Queue()
		visited = set()
		q.enqueue 



# main stuff

print ("Welcome to Apollo Truong's 8-puzzle solver.")
userInput = input("Type \'1\' to use a default puzzle. You may edit the top code for a different puzzle") 

puzzle = Puzzle(board)

s = AStar(puzzle)
p = s.solve()

steps = 0

for node in p:
	print(node.moves)
	node.puzzlePrint(puzzle)
	steps = steps + 1

print("Total number of steps: " + str(steps))
