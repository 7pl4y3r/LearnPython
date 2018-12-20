def line(mat, n):
	line = [0]
	line[0] = int(input("... "))
	for i in range(1, n):
		line.append(int(input("... ")))

	return line

def buildMat(mat, n):
	for i in range(1, n):
		mat.append(line(mat, n))

def prntMat(mat, n):
	for i in range(0, n):
		print mat[i]

mat = [[0]]
n = 3

mat[0] = line(mat, n)
buildMat(mat, 3)
prntMat(mat, n)