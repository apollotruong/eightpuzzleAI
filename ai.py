import numpy as np
import math

w, h = 3, 3;

# Inputted puzzle #
puzzle = [[0 for x in range(w)] for y in range(h)] 

puzzle[0] = [1,2,3]
puzzle[1] = [4,5,0]
puzzle[2] = [7,8,6]

# Respective    [0,1,2,3,4,5,6,7,8,9] (9 is not used)
defaultPosRow = [2,0,0,0,1,1,1,2,2,2]
defaultPosCol = [2,0,1,2,0,1,2,0,1,2]

def findStar(M):
	for i in range(w):
		for j in range(h):
			if M[i][j] == 0:
				return [i,j]
def moveStarUp(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[0] == 0:
		#print ("Cannnot move Up")
		return 0
	else:
		M[row][col], M[row - 1][col] = M[row - 1][col], M[row][col]
		return 1
def moveStarDown(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[0] == 2:
		#print ("Cannnot move Down")
		return 0
	else:
		M[row][col], M[row + 1][col] = M[row + 1][col], M[row][col]
		return 1
def moveStarLeft(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[1] == 0:
		#print ("Cannnot move Left")
		return 0
	else:
		M[row][col], M[row][col - 1] = M[row][col - 1], M[row][col]
		return 1
def moveStarRight(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[1] == 2:
		#print ("Cannnot move Right")
		return 0
	else:
		M[row][col], M[row][col + 1] = M[row][col + 1], M[row][col]
		return 1
def puzzlePrint(M):
	print(np.matrix(M))
	print()
	return
def compareSoln(M):
	soln = [[0 for x in range(w)] for y in range(h)] 
	soln[0] = [1,2,3]
	soln[1] = [4,5,6]
	soln[2] = [7,8,0]

	if soln == M:
		return 1
	else:
		return 0
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

# Manhattan Distance !!
# Takes the distance of parameters 1:RC , 2:RC respectively
def distance(t0,t1,s0,s1):
	return math.fabs(t0 - s0) + math.fabs(t1 - s1)

# Check the distance from x to its supposed position 1-8
def distanceCheck(M,x):
	d = distance(findRow(M,x),findCol(M,x),defaultPosRow[x],defaultPosCol[x])
	
	# debug
	#print("defaultPosRow and defaultPosCol")
	#print(defaultPosRow[x],defaultPosCol[x])
	return d

# Check the distance of the arrangement from the solution (goal)
# Smallest number before goal is 2
# Since there are 2 movements
def totalDistanceCheck(M):
	sum = 0
	for i in range(8):
		sum = sum + distanceCheck(M,i)
	return sum

def uniformCS(M):
	""" FROM HAND-OUT
	function general-search( problen, QUEUEING-FUNCTION)

	nodes = MAKE-QUEUE(MAKE-NODE( problem, INITIAL-STATE ))

	loop do
		if EMPTY(nodes) then return "failure"

			node = REMOVE-FRONT(nodes)
		if problem.GOAL-TEST(node.STATE) suceeds then return node
			nodes = QUEUEING-FUNCTION( nodes, EXPAND(node, problem.OPERATORS))

	"""

# TAKEN FROM 
# http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaQueueinPython.html 
# Reason: First time working in Python, didn't know how to implement Queue
class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.iterms.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

q = Queue()

q.enqueue(4)



print ("Welcome to Apollo Truong's 8-puzzle solver.")
userInput = input("Type \'1\' to use a default puzzle, or \'2\' to enter your own puzzle. ") 

puzzlePrint(puzzle)

print("Distance is")

d = distanceCheck(puzzle,0)
print(d)

#return 1 if true, 0 false
print(compareSoln(puzzle))

print("Total distance is: ",totalDistanceCheck(puzzle))

