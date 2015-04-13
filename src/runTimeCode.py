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
			'$t0' : None,
			'$t1' : None,
			'$t2' : None,
			'$t3' : None,
			'$t4' : None,
			'$t5' : None,
			'$t6' : None,
			'$t7' : None,
			'$t8' : None,
			'$t9' : None,
			'$s0' : None,
			'$s1' : None,
			'$s2' : None,
			'$s3' : None,
			'$s4' : None
		}

		self.freeRegisters = []
		for register in self.registerDescriptor.keys():
			self.freeRegisters.append(register)

		self.busyRegisters = []

	def fixLabels(self):
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

	def putAbsoluteAddressInRegister(level, offset):
		self.addLine(['la', '$s5', 'myspace', '']) # put the address of display into $s5
		self.addLine(['li', '$s6', level, ''])		 # put the index into $s5
		self.addLine(['add', '$s6', '$s6', '$s6'])	 # double the index
		self.addLine(['add', '$s6', '$s6', '$s6'])	 # double the index again (now 4x)
		self.addLine(['add', '$s7', '$s5', '$s6'])	 # combine the two components of the address

		# Now we store the value to the location in the stack
		self.addLine(['lw', '$s5', '0($s7)', ''])	  # load the value into display
		self.addLine(['li', '$s6', offset, ''])		# put the offset into $s6
		self.addLine(['add', '$s6', '$s6', '$s6'])	 # double the offset
		self.addLine(['add', '$s6', '$s6', '$s6'])	 # double the offset again (now 4x)
		self.addLine(['add', '$s7', '$s5', '$s6'])	 # combine the two components of the address

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
					self.addLine(['sw', register, '0($s7)', ''])		# store the value into the record
					self.ST.addressDescriptor[tempReg]['store'] = True

				if self.ST.addressDescriptor[temp]['memory'] != None:
					(level, offset) = self.ST.addressDescriptor[temp]['memory']
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLine(['lw', register, '0($s7)', ''])		# store the value into the record
			else:
				register = self.ST.freeRegisters.pop()
				if self.ST.addressDescriptor[temp]['memory'] != None and self.ST.addressDescriptor[temp]['store']:
					(level, offset) = self.ST.addressDescriptor[tempReg]['memory']
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLine(['lw', register, '0($s7)', ''])		# store the value into the record
			
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
					self.addLine(['lw', reg, '0($s7)', ''])
					self.ST.addressDescriptor[temp]['store'] = True

	def flushRegisters(self, level, function):
		for temp in self.ST.addressDescriptor:
			tempEntry = self.ST.addressDescriptor[temp]
			if temp['memory'] != None and tempEntry['scope'] == function:
				if temp['memory'][0] <= level and temp['register'] != None:
					(level, offset) = tempEntry['memory']
					register = tempEntry['register']
					self.putAbsoluteAddressInRegister(level, offset)
					self.addLine(['sw', register, '0($s7)', ''])		# store the value into the record
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
			self.addLine(['sw', register, '0($s7)', ''])		# store the value into the record
			tempEntry['store'] = True
			tempEntry['register'] = None
			self.registerDescriptor[register] = None
			self.freeRegisters.append(register)
			self.busyRegisters.pop(self.busyRegisters.index(register))

		elif tempEntry['register'] != None:
			self.registerDescriptor[reg] = None
			self.freeReg.append(reg)
			self.regInUse.pop(self.regInUse.index(reg))

	def printCode(self):
		for function in self.code.keys():
			print function
			for i in range(0, len(self.code[function])):
				quad = self.code[functionName][i]
				print quad[0] + ' ' + quad[1] + ' ' + quad[2] + ' ' + quad[3]
