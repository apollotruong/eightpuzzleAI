import numpy as np
w, h = 3, 3;
puzzle = [[0 for x in range(w)] for y in range(h)] 

puzzle[0] = ["1","2","3"]
puzzle[1] = ["4","*","6"]
puzzle[2] = ["7","8","9"]

def findStar(M):
	for i in range(w):
		for j in range(h):
			if M[i][j] == "*":
				return [i,j]

def moveStarUp(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[0] == 0:
		print "Cannnot move Up"
	else:
		M[row][col], M[row - 1][col] = M[row - 1][col], M[row][col]

def moveStarDown(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[0] == 2:
		print "Cannnot move Down"
	else:
		M[row][col], M[row + 1][col] = M[row + 1][col], M[row][col]

def moveStarLeft(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[1] == 0:
		print "Cannnot move Left"
	else:
		M[row][col], M[row][col - 1] = M[row][col - 1], M[row][col]

def moveStarRight(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[1] == 2:
		print "Cannnot move Right"
	else:
		M[row][col], M[row][col + 1] = M[row][col + 1], M[row][col]



print np.matrix(puzzle)
findStar(puzzle)
moveStarRight(puzzle)
print 
print np.matrix(puzzle)

