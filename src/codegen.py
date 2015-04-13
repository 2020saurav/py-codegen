#!/usr/bin/python
import parser
import sys
import runTimeCode

filename = "../test/assignment.py"

def generateMIPSCode(code):
	sys.stderr = open('dump','w')
	ST, TAC = z.parse(code)
	# sys.stderr.close()
	TAC.printCode()
	ST.printSymbolTableHistory()
	RTC = runTimeCode.RunTimeCode(ST, TAC)
	RTC.fixLabels()
	for function in TAC.code:
		RTC.addFunction(function)

		# Different stuff for main
		if (function == 'main'):
			#allocate space for the registers by updating stack pointer
			RTC.addLineToCode(['sub', '$sp', '$sp', '200'])

			#set fame pointer of the callee
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
			RTC.addLineToCode(['sw','$t0','12($sp)',''])
			RTC.addLineToCode(['sw','$t1','16($sp)',''])
			RTC.addLineToCode(['sw','$t2','20($sp)',''])
			RTC.addLineToCode(['sw','$t3','24($sp)',''])
			RTC.addLineToCode(['sw','$t4','28($sp)',''])
			RTC.addLineToCode(['sw','$t5','32($sp)',''])
			RTC.addLineToCode(['sw','$t6','36($sp)',''])
			RTC.addLineToCode(['sw','$t7','40($sp)',''])
			RTC.addLineToCode(['sw','$t8','44($sp)',''])
			RTC.addLineToCode(['sw','$t9','48($sp)',''])
			RTC.addLineToCode(['sw','$s0','52($sp)',''])
			RTC.addLineToCode(['sw','$s1','56($sp)',''])
			RTC.addLineToCode(['sw','$s2','60($sp)',''])
			RTC.addLineToCode(['sw','$s3','64($sp)',''])
			RTC.addLineToCode(['sw','$s4','68($sp)',''])

			# Create space for local data
			RTC.addLineToCode(['li','$v0',ST.getAttributeFromFunctionList(function, 'width'),''])
			RTC.addLineToCode(['sub','$sp','$sp','$v0'])

			# Copy the parameters
			for x in range(ST.getAttributeFromFunctionList(function, 'numParam')):
				RTC.addLineToCode(['sw','$a' + str(x), str(4*x) + '($sp)', ''])

		for line in TAC.code[function]:
			if line[3] == 'JUMPLABEL':
				counter = 0 ;
				reg = RTC.getRegister(line[2])
				RTC.addLineToCode(['jal', reg, '', ''])
				RTC.reloadParents(ST.getAttributeFromFunctionList(function, 'scopeLevel'), function)

			elif line[3] == 'JUMPBACK':
				RTC.addLineToCode(['b', function + 'end', '', ''])

			elif line[3] == 'PARAM':
				reg = RTC.getRegister(line[0])
				RTC.addLineToCode(['move', '$a'+str(counter), reg,''])
				counter = counter +1 ;

			elif line[3] == '=':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				RTC.addLineToCode(['move', reg1, reg2, ''])

				RTC.flushTemporary(line[0])

			elif line[3] == '=i':
				reg = RTC.getRegister(line[0])
				RTC.addLineToCode(['li', reg, line[1], ''])

				RTC.flushTemporary(line[0])

			elif line[3] == '=REF':
				reg = RTC.getRegister(line[0])
				RTC.addLineToCode(['la', reg, line[1], ''])

				RTC.flushTemporary(line[0])

			elif line[3] == 'uni-':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				RTC.addLineToCode(['neg', reg1, reg2, ''])

				RTC.flushTemporary(line[0])

			elif line[3] == '+':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['add', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == '-':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['sub', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == '*':
				reg1 = RTC.getRegister(line[1])
				reg2 = RTC.getRegister(line[2])
				reg3 = RTC.getRegister(line[0])
				RTC.addLineToCode(['mult', reg1, reg2,''])
				RTC.addLineToCode(['mflo', reg3,'',''])

				RTC.flushTemporary(line[0])

			elif line[3] == '/':
				reg1 = RTC.getRegister(line[1])
				reg2 = RTC.getRegister(line[2])
				reg3 = RTC.getRegister(line[0])
				RTC.addLineToCode(['div', reg1, reg2, ''])
				RTC.addLineToCode(['mflo', reg3, '', ''])

				RTC.flushTemporary(line[0])

			elif line[3] == '%':
				reg1 = RTC.getRegister(line[1])
				reg2 = RTC.getRegister(line[2])
				reg3 = RTC.getRegister(line[0])
				RTC.addLineToCode(['div', reg1, reg2, ''])
				RTC.addLineToCode(['mfhi', reg3, '', ''])

				RTC.flushTemporary(line[0])

			elif line[3] == '<':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['slt', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == '>':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['sgt', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == '<=':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['sle', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == '>=':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['sge', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == '==':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['seq', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == '!=':
				reg1 = RTC.getRegister(line[0])
				reg2 = RTC.getRegister(line[1])
				reg3 = RTC.getRegister(line[2])
				RTC.addLineToCode(['sne', reg1, reg2, reg3])

				RTC.flushTemporary(line[0])

			elif line[3] == 'COND_GOTO':
				reg1 = RTC.getRegister(line[0])
				RTC.addLineToCode(['beq', reg1, '$0', line[2]])

			elif line[3] == 'GOTO':
				RTC.addLineToCode(['b', line[2], '', ''])

			elif line[3] == 'FUNCTION_RETURN':
				reg1 = RTC.getRegister(line[0])
				RTC.addLineToCode(['move', reg1, '$v0', ''])

			elif line[3] == 'RETURN':
				reg1 = RTC.getRegister(line[0])
				RTC.addLineToCode(['move', '$v0', reg1, ''])
				RTC.addLineToCode(['b', function + 'end', '', ''])

			elif line[3] == 'HALT':
				RTC.addLineToCode(['jal', 'exit', '', ''])

			elif line[3] == 'PRINT' and line[0] == '':
				RTC.addLineToCode(['jal', 'print_newline', '', ''])

			elif line[3] == 'PRINT' and line[2] == 'UNDEFINED':
				RTC.addLineToCode(['jal', 'print_undefined', '', ''])

			elif line[3] == 'PRINT':
				reg = RTC.getRegister(line[0])
				RTC.addLineToCode(['move', '$a0', reg, ''])

				if line[2] == 'NUMBER':
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

			# Registers
			RTC.addLineToCode(['lw','$t0','12($sp)',''])
			RTC.addLineToCode(['lw','$t1','16($sp)',''])
			RTC.addLineToCode(['lw','$t2','20($sp)',''])
			RTC.addLineToCode(['lw','$t3','24($sp)',''])
			RTC.addLineToCode(['lw','$t4','28($sp)',''])
			RTC.addLineToCode(['lw','$t5','32($sp)',''])
			RTC.addLineToCode(['lw','$t6','36($sp)',''])
			RTC.addLineToCode(['lw','$t7','40($sp)',''])
			RTC.addLineToCode(['lw','$t8','44($sp)',''])
			RTC.addLineToCode(['lw','$t9','48($sp)',''])
			RTC.addLineToCode(['lw','$s0','52($sp)',''])
			RTC.addLineToCode(['lw','$s1','56($sp)',''])
			RTC.addLineToCode(['lw','$s2','60($sp)',''])
			RTC.addLineToCode(['lw','$s3','64($sp)',''])
			RTC.addLineToCode(['lw','$s4','68($sp)',''])
			RTC.addLineToCode(['addi','$sp','$sp','72'])

			# Jump to the calling procedure
			RTC.addLineToCode(['jr','$ra','',''])

	# Print the generated code
	RTC.printCode('a')



if __name__=="__main__":
	z = parser.G1Parser()
	sourcefile = open(filename)
	code = sourcefile.read()
	generateMIPSCode(code)
