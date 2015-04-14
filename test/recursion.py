def sum(n):
	if n == 0 :
		return 0
	a = sum(n-1)
	return a + n
x = sum(100)
print x