def f():
	return 9

def fib(n):
	def f4():
		print 7
		def funception():
			print 42
			return 44
		a = funception()
		print a
		return a
	n = f4()
	return n
	print 3

x = fib(3)
print x
# a = funception() # ERROR :D