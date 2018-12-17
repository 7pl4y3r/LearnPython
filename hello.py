def maxi(a,b):
	if a > b:
		return a
	else:
		return b

def isPrime(x):
	if x < 2:
		return 0
	if x > 2:
		if x % 2 == 0:
			return 0
			
	d = 3
	while d * d <= x:
		if x % d == 0:
			return 0
		d += 2

		return 1

i = 0
while i < 10:
	if isPrime(i) == 1:
		print i

	i += 1