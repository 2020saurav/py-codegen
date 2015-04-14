class RunTimeCode:
	def __init__(self, ST, TAC):
		self.code = dict()
		self.ST = ST
		self.TAC = TAC
		self.currentFunction = ''
		self.registersCount = 1
		self.labelCount = -1
		self.labelBase = 'label'
		self.resetRegisters()

	def resetRegisters(self):
		self.registerDescriptor = {
			'$t0' : None, '$t1' : None, '$t2' : None, '$t3' : None, '$t4' : None, '$t5' : None, 
			'$t6' : None, '$t7' : None, '$t8' : None, '$t9' : None, '$s0' : None, '$s1' : None, 
			'$s2' : None, '$s3' : None, '$s4' : None }

		self.freeRegisters = []
		for register in self.registerDescriptor.keys():
			self.freeRegisters.append(register)
		self.busyRegisters = []

	def fixLabels(self):
		# convert jump line numbers to labels. MIPS supports labels
		for function in self.TAC.code:
			unresolvedLabels = {}
			for line in self.TAC.code[function]:
				if line[3] in ['COND_GOTO', 'GOTO']:
					if line[2] in unresolvedLabels:
						label = unresolvedLabels[line[2]]
					else:
						label = self.nameLabel()
						unresolvedLabels[line[2]] = label
					line[2] = label
			lineNumber = -1
			count = 0
			for line in range(len(self.TAC.code[function])):
				lineNumber += 1
				if lineNumber in unresolvedLabels.keys():
					effectiveLineNumber = lineNumber + count
					self.TAC.code[function].insert(effectiveLineNumber, ['LABEL', unresolvedLabels[lineNumber], '', ''])
					count += 1
					del unresolvedLabels[lineNumber]

	def nameLabel(self):
		self.labelCount += 1
		return self.labelBase + str(self.labelCount)

	def putAbsoluteAddressInRegister(self, level, offset):
		self.addLineToCode(['la', '$s5', '__myspace__', ''])
		self.addLineToCode(['li', '$s6', level, ''])
		self.addLineToCode(['sll', '$s6', '$s6', 2])		# 4x
		self.addLineToCode(['add', '$s7', '$s5', '$s6'])	 

		self.addLineToCode(['lw', '$s5', '0($s7)', ''])
		self.addLineToCode(['li', '$s6', offset/4, ''])		
		self.addLineToCode(['sll', '$s6', '$s6', 2])		# 4x
		self.addLineToCode(['add', '$s7', '$s5', '$s6'])	 # add offset

	def addLineToCode(self, line):
		self.code[self.currentFunction].append(line)

	def addFunction(self, function):
		self.currentFunction = function
		self.code[function] = []

	def getRegister(self, temp):
		if temp in self.registerDescriptor.values():
			register = self.ST.addressDescriptor[temp]['register']
		else:
			if len(self.freeRegisters) == 0:
				register = self.busyRegisters.pop(0)
				tempReg = self.registerDescriptor[register]
				self.ST.addressDescriptor[tempReg]['register'] = None
				self.registerDescriptor[register] = temp
				
				if self.ST.addressDescriptor[tempReg]['memory'] != None:
					(level, offset) = self.ST.addressDescriptor[tempReg]['memory']
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLineToCode(['sw', register, '0($s7)', ''])
					self.ST.addressDescriptor[tempReg]['store'] = True

				if self.ST.addressDescriptor[temp]['memory'] != None:
					(level, offset) = self.ST.addressDescriptor[temp]['memory']
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLineToCode(['lw', register, '0($s7)', ''])	
			else:
				register = self.freeRegisters.pop()
				if self.ST.addressDescriptor[temp]['memory'] != None and self.ST.addressDescriptor[temp]['store']:
					(level, offset) = self.ST.addressDescriptor[temp]['memory']
					# print (level, offset)
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLineToCode(['lw', register, '0($s7)', ''])
			
			self.ST.addressDescriptor[temp]['register'] = register
			self.busyRegisters.append(register)
			self.registerDescriptor[register] = temp

		return register

	def reloadParentRegisters(self, level, function):
		for temp in self.ST.addressDescriptor:
			tempEntry = self.ST.addressDescriptor[temp]
			if tempEntry['memory'] != None and tempEntry['scope'] == function:
				if tempEntry['memory'][0] <= level and tempEntry['register'] != None:
					(level, offset) = tempEntry['memory']
					register = tempEntry['register']
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLineToCode(['lw', register, '0($s7)', ''])
					self.ST.addressDescriptor[temp]['store'] = True

	def flushRegisters(self, level, function):
		for temp in self.ST.addressDescriptor:
			tempEntry = self.ST.addressDescriptor[temp]
			if temp['memory'] != None and tempEntry['scope'] == function:
				if temp['memory'][0] <= level and temp['register'] != None:
					(level, offset) = tempEntry['memory']
					register = tempEntry['register']
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLineToCode(['sw', register, '0($s7)', ''])
					tempEntry['store'] = True
					tempEntry['register'] = None
					self.registerDescriptor[register] = None
					self.freeRegisters.append(register)
					self.busyRegisters.pop(self.busyRegisters.index(register))

	def flushTemporary(self, temp):
		tempEntry = self.ST.addressDescriptor[temp]
		register = tempEntry['register']

		if tempEntry['memory'] != None and tempEntry['register'] != None:
			(level, offset) = tempEntry['memory']
			register = tempEntry['register']
			self.putAbsoluteAddressInRegister(level, offset)
			self.addLineToCode(['sw', register, '0($s7)', ''])
			tempEntry['store'] = True
			tempEntry['register'] = None
			self.registerDescriptor[register] = None
			self.freeRegisters.append(register)
			self.busyRegisters.pop(self.busyRegisters.index(register))

		elif tempEntry['register'] != None:
			self.registerDescriptor[register] = None
			self.freeRegisters.append(register)
			self.busyRegisters.pop(self.busyRegisters.index(register))

	def printCode(self, fileName=''):
		f = open('build/' + fileName + '.s', 'w')
		data = open('lib/data.s').read()
		f.write(data)
		for functionName in self.TAC.code:
			functionEntry = self.ST.functionlist[functionName]
			for stringEntry in functionEntry['stringList']:
				f.write('\t%s:\t.asciiz\t"%s"\n' %(stringEntry[0], stringEntry[1]))
		f.write('\n.text\n')

		for functionName in self.code.keys():
			f.write("\n%s:\n" %functionName)
			for i in range(len(self.code[functionName])):
				codePoint = self.code[functionName][i]
				if codePoint[0] == 'LABEL':
					f.write("%s:\n" %codePoint[1])
				elif codePoint[1] == '':
					f.write("\t%s\n" %codePoint[0])
				elif codePoint[2] == '':
					f.write("\t%s\t\t%s\n" %(codePoint[0], codePoint[1]))
				elif codePoint[3] == '':
					f.write("\t%s\t\t%s,\t%s\n" %(codePoint[0], codePoint[1], codePoint[2]))
				else:
					f.write("\t%s\t\t%s,\t%s,\t%s\n" %(codePoint[0], codePoint[1], codePoint[2], codePoint[3]))
		# labels for printing etc
		data = open('lib/code.s').read()
		f.write(data)
		f.close()