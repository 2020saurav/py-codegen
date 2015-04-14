def f():
	return 9

def fib(n):
	def f4():
		print 7
		def funinception():
			print 42
			return 44
		a = funinception()
		print a
		return a
	n = f4()
	return n
	print 3

x = fib(3)
print x
