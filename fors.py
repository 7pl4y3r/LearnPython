def isPrime(x):
	if x < 2 or (x > 2 and x % 2 == 0):
		return False

	d = 3
	while d * d <= x:
		if x % d == 0:
			return False
		d += 2

	return True


x = int(input("Num..."))
if isPrime(x):
	print "Yes"
else:
	print "No"


#for i in range(3, 1000, 2):
#	if isPrime(i):
#		print i
#		print "is prime"