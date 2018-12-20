def maxi(x, y):
	if x > y:
		return x
	else:
		return y

def mini(x, y):
	if x < y:
		return x
	else:
		return y

def isPrime(x):
	if x < 2 or x % 2 == 0:
		return False

	d = 3
	while d * d <= x:
		if x % d == 0:
			return False
		d += 2

	return True


def arePrimes(x, y):
	switch = {
		1: "Both are primes",
		0: "Not both of them are prime"
	}
	print switch.get(isPrime(x) and isPrime(y), "Error")

x = int(input("x = "))
y = int(input("y = "))

print "The maximum is"
print maxi(x, y)

print "The minimum is "
print mini(x, y)

arePrimes(x, y)