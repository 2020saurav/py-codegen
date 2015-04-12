#!/usr/bin/python
import parser
import sys

def generateMIPSCode(code):
	sys.stderr = open('dump','w')
	ST, TAC = z.parse(code)
	sys.stderr.close()
	TAC.printCode()
	# ST.printSymbolTableHistory()
	# TODO write here. 
	# TODO some getNewTempVars in parser.py need args
	# TODO may need helper functions for Run Time Env
	# TODO use TAC.code and generate assembly


if __name__=="__main__":
	z = parser.G1Parser()
	filename = "../test/func.py"
	sourcefile = open(filename)
	code = sourcefile.read()
	generateMIPSCode(code)
