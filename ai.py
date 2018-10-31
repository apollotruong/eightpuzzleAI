import numpy as np
import math

w, h = 3, 3;



puzzle = [[0 for x in range(w)] for y in range(h)] 

puzzle[0] = ["5","2","3"]
puzzle[1] = ["4","1","6"]
puzzle[2] = ["7","*","8"]


defaultPosRow = [0,0,0,0,1,1,1,2,2,2]
defaultPosCol = [0,0,1,2,0,1,2,0,1,2]

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
		print ("Cannnot move Up")
	else:
		M[row][col], M[row - 1][col] = M[row - 1][col], M[row][col]
def moveStarDown(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[0] == 2:
		print ("Cannnot move Down")
	else:
		M[row][col], M[row + 1][col] = M[row + 1][col], M[row][col]
def moveStarLeft(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[1] == 0:
		print ("Cannnot move Left")
	else:
		M[row][col], M[row][col - 1] = M[row][col - 1], M[row][col]
def moveStarRight(M):
	pos = findStar(M)
	row = pos[0]
	col = pos[1]
	if pos[1] == 2:
		print ("Cannnot move Right")
	else:
		M[row][col], M[row][col + 1] = M[row][col + 1], M[row][col]
def puzzlePrint(M):
	print(np.matrix(M))
	print()
	return
def compareSoln(M):
	soln = [[0 for x in range(w)] for y in range(h)] 
	soln[0] = ["1","2","3"]
	soln[1] = ["4","5","6"]
	soln[2] = ["7","8","*"]

	if soln == M:
		return 1
	else:
		return 0
def findNum(M,x):
	for i in range(w):
		for j in range(h):
			if M[i][j] == x:
				return [i,j]
def distance(t0,t1,t):
	return math.fabs(t0[0] - t1) + math.fabs(t0[1] - t2)
# Check the distance from x to its supposed position 1-8
def distanceCheck1(M,x):
	# Checking 1
	tup1 = findNum(M,str(x))
	print(tup1)
	print(defaultPosRow[x]," ",defaultPosCol[x])
	d = distance(findNum(M,x),defaultPosRow[x],defaultPosCol[x])
	print(d)
	return d






print ("Welcome to Apollo Truong's 8-puzzle solver.")
userInput = input("Type \'1\' to use a default puzzle, or \'2\' to enter your own puzzle.") 

puzzlePrint(puzzle)
d = distanceCheck1(puzzle,1)
print("Distance is")
print(d)

print(compareSoln(puzzle))


