def readLine(n):
	line = [0]
	line[0] = int(input("... "))
	for i in range(1, n):
		line.append(int(input("... ")))

	return line

def readMat(mat, n):
	for i in range(1, n):
		mat.append(readLine(n))


mat = [[0]]