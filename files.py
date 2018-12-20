f = open("newFile.txt", "w+")

for i in range(5):
	f.write("Iteration number %d\n" % (i + 1))

f1 = open("matrix.txt", "r")
line1 = f1.readlines()

for i in range(0, len(line1)):
	for j in range(0, len(line1)):
		print(line1[i][j])