import pprint

class SymbolTable:
	def __init__(self):
		self.symbolTable = {
			"main" : {
				"scopeName"		: "main",
				"type"			: "FUNCTION",
				"returnType"	: "UNDEFINED",
				"stringList"	: [],
				"scopeLevel"	: 0
			}
		}

		self.stackHistory = []
		self.offsetStack	= [0]
		self.functionlist = {'main':self.symbolTable['main']}
		self.scopeStack	= [self.symbolTable["main"]]

		self.addressDescriptor = dict()
		self.stringCount = 0
		self.varCount = 0

	def getNewTempVar(self, memLocation='', variable='', loadFromMem=False):
		self.varCount += 1
		tempVar = "var" + str(self.varCount)
		self.addressDescriptor[tempVar] = {
							'memory'	: None,
							'register'	: None,
							'store'		: loadFromMem,
							'dirty'		: False,
							'scope'		: self.getCurrentScope(),
							'variable'	: variable
						}

		if memLocation != '':
			self.addressDescriptor[tempVar]['memory'] = memLocation
		return tempVar	
	
	def changeMemLocation(self, tempName, memLocation, variable=''):
		self.addressDescriptor[tempName]['memory'] = memLocation
		self.addressDescriptor[tempName]['variable'] = variable
		self.addressDescriptor[tempName]['scope'] = self.getCurrentScope()

	def lookup(self, identifier):
		currentScope = len(self.scopeStack)
		return self.lookupScopeStack(identifier, currentScope - 1)

	def lookupScopeStack(self, identifier, position):
		if position == -1:
			return None
		currentScope = self.scopeStack[position]
		# if sought identifier is not in current scope, it may be in parent
		if identifier in currentScope:
			return currentScope[identifier]
		else:
			return self.lookupScopeStack(identifier, position - 1)

	def getCurrentScope(self):
		return self.scopeStack[len(self.scopeStack) - 1]["scopeName"]
	# ensure every scope has this key

	def addScope(self, scopeName, var):
		currentScope = self.scopeStack[len(self.scopeStack) - 1]
		level = currentScope['scopeLevel'] + 1
		currentScope[scopeName] = {
			"scopeName"		: scopeName,
			"parentName"	: currentScope["scopeName"],
			"type"			: "FUNCTION",
			"returnType"	: "NUMBER",
			"stringList"	: [],
			"scopeLevel"	: level,
			"var"			: var
		}
		# self.addIdentifier('True', 'BOOLEAN')
		# self.addAttribute('True', scopeName, 1)
		# self.addIdentifier('False', 'BOOLEAN')
		# self.addAttribute('False', scopeName, 0)

		self.scopeStack.append(currentScope[scopeName])

		# start new relative addressing
		self.offsetStack.append(0)
		self.functionlist[scopeName] = currentScope[scopeName]

	def addIdentifier(self, identifier, identifierType):
		currentScope = self.scopeStack[len(self.scopeStack) - 1]
		width = self.getWidthFromType(identifierType)
		# TODO Add other types

		currentOffset = self.offsetStack.pop()
		if not identifier in currentScope:
			currentScope[identifier] = dict()
		currentScope[identifier]["offset"] = currentOffset
		currentScope[identifier]["type"] = identifierType
		currentScope[identifier]["width"] = width	
		currentScope[identifier]["scopeLevel"] = currentScope["scopeLevel"]
		
		self.offsetStack.append(currentOffset + width)

	def addAttribute(self, identifier, key, value):
		entry = self.lookup(identifier)
		entry[key] = value

	def getAttribute(self, identifier, key):
		entry = self.lookup(identifier)
		if key in entry:
			return entry[key]
		else:
			return None

	def getAttributeFromCurrentScope(self, key):
		currentScope = self.scopeStack[len(self.scopeStack) - 1]
		return currentScope[key]

	def addAttributeToCurrentScope(self, key, value):
		currentScope = self.scopeStack[len(self.scopeStack) - 1]
		currentScope[key] = value

	def exists(self, identifier):
		if self.lookup(identifier) != None:
			return True
		return False

	def existsInCurrentScope(self, identifier):
		return self.scopeStack[len(self.scopeStack)-1].get(identifier, False) != False

	def removeCurrentScope(self):
		currentScope = self.scopeStack.pop()
		currentScope["width"] = self.offsetStack.pop()
		self.stackHistory.append(currentScope)

	# print scopeStack
	def printST(self):
		print self.scopeStack

	def getAttributeFromFunctionList(self, function, key):
		if function in self.functionlist:
			return self.functionlist[function][key]
		else :
			return None 	

	def getFunctionAttribute(self, identifier, key):
		functionName = self.getAttribute(identifier, 'name')
		if functionName in self.functionlist:
			return functionlist[functionName][key]

	def getBaseAddress(self, scopeName, key):
		return 100

	def getWidthFromType(self, identifierType):
		if identifierType == 'NUMBER':
			width = 4
		elif identifierType == 'STRING':
			width = 256
		elif identifierType == 'UNDEFINED':
			width = 0
		elif identifierType == 'FUNCTION':
			width = 4
		elif identifierType == 'BOOLEAN':
			width = 4
		else:
			width = 0
		return width

	def nameString(self):
		self.stringCount += 1
		return "str" + str(self.stringCount)

	def addToStringList(self, label, string):
		currentScope = self.scopeStack[len(self.scopeStack) - 1]
		currentScope['stringList'].append([label, string])

	def printSymbolTableHistory(self):
		print "\n\n SYMBOL TABLE"
		print     "--------------"
		for st in self.stackHistory:
			print "\nSCOPE: " + st['scopeName']
			print "-----------------------"
			pprint.pprint (st)
			print "-----------------------\n"
