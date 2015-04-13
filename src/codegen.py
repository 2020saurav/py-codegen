#!/usr/bin/python
import parser
import sys
import runTimeCode

filename = "../test/func.py"

def generateMIPSCode(code):
	sys.stderr = open('dump','w')
	ST, TAC = z.parse(code)
	sys.stderr.close()
	TAC.printCode()
	RTC = runTimeCode.RunTimeCode(ST, TAC)
	RTC.fixLabels()


if __name__=="__main__":
	z = parser.G1Parser()
	sourcefile = open(filename)
	code = sourcefile.read()
	generateMIPSCode(code)
