#!/usr/bin/python
import parser
import sys
import runTimeCode

filename = "../test/func.py"
RTC = {}

def registerAction(action):
	global RTC
	regs = ['$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$t8', '$t9', '$s0', '$s1', '$s2', '$s3', '$s4']
	offset = 12
	for reg in regs:
		RTC.addLineToCode([action, reg, str(offset)+'($sp)', ''])
		offset += 4

def generateMIPSCode(code):
	global RTC
	sys.stderr = open('dump','w')
	ST, TAC = z.parse(code)
	# sys.stderr.close()
	TAC.printCode()
	# ST.printSymbolTableHistory()
	RTC = runTimeCode.RunTimeCode(ST, TAC)
	RTC.fixLabels()
	counter = 0
	for function in TAC.code:
		RTC.addFunction(function)

		if (function == 'main'):
			RTC.addLineToCode(['sub', '$sp', '$sp', '200'])
			#set frame pointer of the callee
			RTC.addLineToCode(['la', '$fp', '200($sp)', ''])
			RTC.addLineToCode(['la', '$s5', '__display__', ''])
			RTC.addLineToCode(['lw', '$s7', '0($s5)', ''])
			#set display[level]
			RTC.addLineToCode(['la', '$v0', '-' + str(ST.getAttributeFromFunctionList(function, 'width')) + '($sp)', ''])
			RTC.addLineToCode(['sw','$v0', '0($s5)', ''])
			RTC.addLineToCode(['li', '$v0', ST.getAttributeFromFunctionList(function, 'width'), ''])
			RTC.addLineToCode(['sub', '$sp', '$sp', '$v0'])

		else:
			#allocate space for the registers by updating stack pointer
			RTC.addLineToCode(['sub', '$sp','$sp','72'])
			#store return address of the caller
			RTC.addLineToCode(['sw','$ra','0($sp)',''])
			#sstore the frame pointer of the caller
			RTC.addLineToCode(['sw','$fp','4($sp)',''])
			#set fame pointer of the callee
			RTC.addLineToCode(['la','$fp','72($sp)',''])
			#storing display[level]
			RTC.addLineToCode(['li','$v0',ST.getAttributeFromFunctionList(function, 'scopeLevel'),''])
			RTC.addLineToCode(['la', '$s5', '__display__', ''])
			RTC.addLineToCode(['add', '$v0', '$v0', '$v0'])
			RTC.addLineToCode(['add', '$v0', '$v0', '$v0'])
			RTC.addLineToCode(['add', '$s6', '$v0', '$s5'])
			RTC.addLineToCode(['lw','$s7','0($s6)',''])
			RTC.addLineToCode(['sw','$s7','8($sp)',''])
			#set display[level]
			RTC.addLineToCode(['la', '$v0', '-' + str(ST.getAttributeFromFunctionList(function, 'width'))+'($sp)' , ''])
			RTC.addLineToCode(['sw','$v0','0($s6)',''])

			#store remaining registers
			registerAction('sw')
			# Create space for local data
			RTC.addLineToCode(['li','$v0',ST.getAttributeFromFunctionList(function, 'width'),''])
			RTC.addLineToCode(['sub','$sp','$sp','$v0'])

			# Copy the parameters
			# print ST.getAttributeFromFunctionList(function, 'numParam')
			numParam = ST.getAttributeFromFunctionList(function, 'numParam')
			if numParam >4:
				parser.error("Too many parameters (max: 4)", None)
			for x in range(numParam):
				RTC.addLineToCode(['sw','$a' + str(x), str(4*x) + '($sp)', ''])

		for line in TAC.code[function]:
			if line[3] == 'JUMPLABEL':
				counter = 0 ;
				RTC.addLineToCode(['jal', RTC.getRegister(line[2]), '', ''])
				RTC.reloadParentRegisters(ST.getAttributeFromFunctionList(function, 'scopeLevel'), function)

			elif line[3] == 'JUMP_RETURN':
				RTC.addLineToCode(['b', function + 'end', '', ''])

			elif line[3] == 'PARAM':
				RTC.addLineToCode(['move', '$a'+str(counter), RTC.getRegister(line[0]),''])
				counter = counter +1 ;
				if counter == 5:
					parser.error("Too many parameters (max: 4)", None)

			elif line[3] == '=':
				RTC.addLineToCode(['move', RTC.getRegister(line[0]), RTC.getRegister(line[1]), ''])
				# RTC.flushTemporary(line[0])

			elif line[3] == '=i':
				RTC.addLineToCode(['li', RTC.getRegister(line[0]), line[1], ''])
				# RTC.flushTemporary(line[0])

			elif line[3] == '=REF':
				RTC.addLineToCode(['la', RTC.getRegister(line[0]), line[1], ''])
				# RTC.flushTemporary(line[0])

			elif line[3] == '+':
				RTC.addLineToCode(['add', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])

			elif line[3] == '-':
				RTC.addLineToCode(['sub', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])

			elif line[3] == '*':
				RTC.addLineToCode(['mult', RTC.getRegister(line[1]), RTC.getRegister(line[2]),''])
				RTC.addLineToCode(['mflo', RTC.getRegister(line[0]),'',''])
				# RTC.flushTemporary(line[0])

			elif line[3] == '/':
				RTC.addLineToCode(['div', RTC.getRegister(line[1]), RTC.getRegister(line[2]), ''])
				RTC.addLineToCode(['mflo', RTC.getRegister(line[0]), '', ''])
				# RTC.flushTemporary(line[0])

			elif line[3] == '%':
				RTC.addLineToCode(['div', RTC.getRegister(line[1]), RTC.getRegister(line[2]), ''])
				RTC.addLineToCode(['mfhi', RTC.getRegister(line[0]), '', ''])
				# RTC.flushTemporary(line[0])

			elif line[3] == '<':
				print line[0],line[1],line[2]
				RTC.addLineToCode(['slt', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])

			elif line[3] == '>':
				RTC.addLineToCode(['sgt', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])

			elif line[3] == '<=':
				RTC.addLineToCode(['sle', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])

			elif line[3] == '>=':
				RTC.addLineToCode(['sge', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])

			elif line[3] == '==':
				RTC.addLineToCode(['seq', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])

			elif line[3] == '!=':
				RTC.addLineToCode(['sne', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
				# RTC.flushTemporary(line[0])
			elif line[3] == 'or':
				RTC.addLineToCode(['or', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])
			
			elif line[3] == 'and':
				RTC.addLineToCode(['and', RTC.getRegister(line[0]), RTC.getRegister(line[1]), RTC.getRegister(line[2])])

			elif line[3] == 'COND_GOTO':
				RTC.addLineToCode(['beq', RTC.getRegister(line[0]), line[1], line[2]])

			elif line[3] == 'GOTO':
				RTC.addLineToCode(['b', line[2], '', ''])

			elif line[3] == 'FUNCTION_RETURN':
				RTC.addLineToCode(['move', RTC.getRegister(line[0]), '$v0', ''])

			elif line[3] == 'RETURN':
				RTC.addLineToCode(['move', '$v0', RTC.getRegister(line[0]), ''])
				RTC.addLineToCode(['b', function + 'end', '', ''])
 
			elif line[3] == 'HALT':
				RTC.addLineToCode(['jal', 'exit', '', ''])

			elif line[3] == 'PRINT' and line[0] == '':
				RTC.addLineToCode(['jal', 'print_newline', '', ''])

			# elif line[3] == 'PRINT' and line[2] == 'UNDEFINED':
			# 	RTC.addLineToCode(['jal', 'print_undefined', '', ''])

			elif line[3] == 'PRINT':
				RTC.addLineToCode(['move', '$a0', RTC.getRegister(line[0]), ''])

				if line[2] == 'NUMBER' or line[2] == 'UNDEFINED':
					RTC.addLineToCode(['jal', 'print_integer', '', ''])
				elif line[2] == 'STRING':
					RTC.addLineToCode(['jal', 'print_string', '', ''])
				else:
					RTC.addLineToCode(['jal', 'print_boolean', '', ''])
			else:
				RTC.addLineToCode(line)

		# Data unloading happens for all function save main
		if function != 'main':
			# Add a label to point to the end of the function
			RTC.addLineToCode(['LABEL', function + 'end', '', ''])
			# Remove the local data
			RTC.addLineToCode(['addi','$sp','$sp',ST.getAttributeFromFunctionList(function,'width')])
			# Get enviornment pointers
			RTC.addLineToCode(['lw','$ra','0($sp)',''])
			RTC.addLineToCode(['lw','$fp','4($sp)',''])
			RTC.addLineToCode(['lw','$a0','8($sp)',''])
			# diplay level
			RTC.addLineToCode(['li','$a1',ST.getAttributeFromFunctionList(function, 'scopeLevel'),''])
			RTC.addLineToCode(['la', '$s5', '__display__', ''])
			RTC.addLineToCode(['add', '$a1', '$a1', '$a1'])
			RTC.addLineToCode(['add', '$a1', '$a1', '$a1'])
			RTC.addLineToCode(['add', '$s6', '$a1', '$s5'])
			RTC.addLineToCode(['sw','$a0','0($s6)',''])

			# Registers loading
			registerAction('lw')
			RTC.addLineToCode(['addi','$sp','$sp','72'])

			# Jump to the calling procedure
			RTC.addLineToCode(['jr','$ra','',''])
	RTC.printCode('a')

if __name__=="__main__":
	z = parser.G1Parser()
	sourcefile = open(filename)
	code = sourcefile.read()
	generateMIPSCode(code)
