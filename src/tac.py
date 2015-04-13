class ThreeAddressCode:
	def __init__(self):
		self.code = {'main': []}
		self.quad = {'main': -1}
		self.nextQuad = {"main": 0}


	def incrementQuad(self, functionName):
		self.quad[functionName] = self.nextQuad[functionName]
		self.nextQuad[functionName] += 1
		return self.quad[functionName]

	def getNextQuad(self, functionName):
		return self.nextQuad[functionName]

	def getCodeLength(self, functionName):
		return self.quad[functionName]

	def emit(self, functionName, regDest, regSrc1, regSrc2, op):
		self.incrementQuad(functionName)
		self.code[functionName].append([regDest, regSrc1, regSrc2, op])

	def createNewFucntionCode(self, functionName):
		self.code[functionName] = []
		self.quad[functionName] = -1
		self.nextQuad[functionName] = 0

	def printCode(self):
		for functionName in self.code.keys():
			print functionName,":"
			for i in range(len(self.code[functionName])):
				print  "%5d: \t" %i, self.code[functionName][i]

	def merge(self, list1, list2):
		return list1+list2

	def backpatch(self, functionName, locationList, location):
		for position in locationList:
			self.code[functionName][position][2] = location

	def noop(self, functionName, locationList):
		for position in locationList:
			self.code[functionName][position][3] = 'NOOP'