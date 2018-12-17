def isBigger(x, y):
	if x > y:
		return True
	else:
		return False

def isPrime(x):
	if x < 2:
		return False
	if x > 2 & x % 2 == 0:
		return False

	d = 3
	while d * d <= x:
		if x % d == 0:
			return False

	return True

def square(x):
	return x * x

x = 25
y = 2

print "is x is bigger than y?"
if isBigger(x, y):
	print "Yes"
else:
	print "No"

print "is x prime?"
if isPrime(x):
	print "Yes"
else:
	print "No"

print "square of x is"
print square(x)
