class RunTimeCode:
	def __init__(self, ST, TAC):
		self.code = dict()
		self.ST = ST
		self.TAC = TAC
		self.currentFunction = ''
		self.registersCount = 1
		self.labelCount = -1
		self.labelBase = 'label'
		self.freeRegisters = []
		self.busyRegisters = []
		self.resetRegsisters()

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

		for register in registerDescriptor.keys():
			self.freeRegisters.append(register)

		self.busyRegisters = []

	def addLineToCode(self, line):
		self.code[self.currentFunction].append(line)

	def addFunction(self, function):
		self.currentFunction = function
		self.code[function] = []

	def printCode(self):
		for function in self.code.keys():
			print function
			for i in range(0, len(self.code[function])):
				quad = self.code[functionName][i]
				print quad[0] + ' ' + quad[1] + ' ' + quad[2] + ' ' + quad[3]

	def nextRegister(self, temp):
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
					self.addLine(['la', '$s5', '__display__', '']) # put the address of display into $s5
					self.addLine(['li', '$s6', level, ''])         # put the index into $s5
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the index
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the index again (now 4x)
					self.addLine(['add', '$s7', '$s5', '$s6'])     # combine the two components of the address

					# Now we store the value to the location in the stack
					self.addLine(['lw', '$s5', '0($s7)', ''])      # load the value into display
					self.addLine(['li', '$s6', offset, ''])        # put the offset into $s6
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the offset
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the offset again (now 4x)
					self.addLine(['add', '$s7', '$s5', '$s6'])     # combine the two components of the address

					self.addLine(['sw', register, '0($s7)', ''])        # store the value into the record
					self.ST.addressDescriptor[tempReg]['store'] = True

				if self.ST.addressDescriptor[temp]['memory'] != None:
					(level, offset) = self.ST.addressDescriptor[temp]['memory']
					# First we load in the value of the activation record where we have to store the value
					self.addLine(['la', '$s5', '__display__', '']) # put the address of display into $s5
					self.addLine(['li', '$s6', level, ''])         # put the index into $s5
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the index
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the index again (now 4x)
					self.addLine(['add', '$s7', '$s5', '$s6'])     # combine the two components of the address

					# Now we store the value to the location in the stack
					self.addLine(['lw', '$s5', '0($s7)', ''])      # load the value into display
					self.addLine(['li', '$s6', offset, ''])        # put the offset into $s6
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the offset
					self.addLine(['add', '$s6', '$s6', '$s6'])     # double the offset again (now 4x)
					self.addLine(['add', '$s7', '$s5', '$s6'])     # combine the two components of the address

					self.addLine(['lw', register, '0($s7)', ''])        # store the value into the record
			else:
				pass 			





