def readArray(arr, leng):
	if leng > 0:
		arr[0] = int(input("Element 1 "))
		if leng > 1:
			for i in range(1, leng):
				arr.append(int(input("Element ")))

def bubbleSort(arr):
	for i in range(0, len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if arr[i] > arr[j]:
				arr[i] -= arr[j]
				arr[j] += arr[i]
				arr[i] = arr[j] - arr[i]

def quickSort(arr, low, high):
	if low < high:
		i = low
		piv = low
		j = high

		while arr[i] < arr[piv]:
			i += 1

		while arr[j] > arr[piv]:
			j -= 1

		if i < j:
			arr[i] -= arr[j]
			arr[j] += arr[i]
			arr[i] = arr[j] - arr[i]

		arr[j] -= arr[piv]
		arr[piv] += arr[j]
		arr[j] = arr[piv] - arr[j]

		quickSort(arr, low, j - 1)
		quickSort(arr, j + 1, high)

def prntMenu():
	print "1 - bubble sort"
	print "2 - quickSort"

def choose(arr):
	i = int(input("Option "))
	if i == 1:
		bubbleSort(arr)
	elif i == 2:
		quickSort(arr, 0, len(arr) - 1)

	
arr = [0]
leng = int(input("Number of elements in array "))
readArray(arr, leng)
print "The initial array is",arr

prntMenu()
choose(arr)

#bubbleSort(arr)
print "Array after sorting",arr