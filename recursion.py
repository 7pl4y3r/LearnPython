def prntList(mList):
	for i in range(0, len(mList)):
		print mList[i]

def recPrntList(mList, i):
	if i >= 0:
		recPrntList(mList, i - 1)
		print mList[i]

def swapInList(x, y):
	z = x
	x = y
	y = z

def partition(mList, low, high):
	pivot = mList[high]
	i = low - 1

	for j in range(low, high):
		if mList[j] <= pivot:
			i += 1
			swapInList(mList[i + 1], mList[high])

	swapInList(mList[i + 1], mList[high])
	return i + 1

def quickSort(mList, low, high):
	if low < high:
		pi = partition(mList, low, high)
		quickSort(mList, low, pi - 1)
		quickSort(mList, pi + 1, high)

list1 = [2, 3, 6, 8, 11]
list2 = [35, 8, 4, 2, 6, 4, 12, 3]

print "Iterative"
prntList(list1)

print "Recursive"
recPrntList(list1, len(list1) - 1)

print "Sorted"
quickSort(list2, 0, len(list2) - 1)
prntList(list2)