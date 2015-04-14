CS335A: Compiler Design (Assignment 4: ASSEMBLY CODE GENERATOR)
===================================================================

* Source Language: *Python*
* Target Language: *MIPS Assembly*
* Implementation Language: *Python*
* Authors: Abhilash Kumar, Arnab Ghosh and Saurav Kumar

* Tool Used : PLY (Python Lex and Yacc)

### MIPS Assembly Code Representation
_____________________________________

1. Representation: ```opcode rd rs rt```

2. Operators:

	- ADD -- Add (with overflow)
	- ADDI -- Add immediate (with overflow)
	- AND -- Bitwise and
	- B-- Unconditional Branch
	- BEQ -- Branch on equal
	- BGEZ -- Branch on greater than or equal to zero
	- BGTZ -- Branch on greater than zero
	- BLEZ -- Branch on less than or equal to zero
	- BNE -- Branch on not equal
	- DIV -- Divide
	- JAL -- Jump and link
	- JR -- Jump register
	- LW -- Load word
	- LI -- Load Immediate
	- LA --	Load Address
	- MULT -- Multiply
	- NOOP -- no operation
	- OR -- Bitwise or
	- SLL -- Shift left logical 
	- SUB -- Subtract
	- SW -- Store word
	- SYSCALL -- System call
	- SRL -- Shift right logical
	- LI -- Load Immediate
	- SNE -- Signed Not Equal
	- SLL -- Signed Left Shift
	- SLT -- Signed Less Than
	- SGT -- Signed Greater Than
	- SLE -- Signed Less Than or Equal to
	- SGE -- Signed Greater Than or Equal to
	- SEQ -- Signed Equal To
	- SUB -- Subtraction
	- MFLO -- Move from LO
	- MFHI -- Move from HI


### Running Instruction
_______________________
1. Run the makefile 
```
make
```
2. To run the Assembly Code Generator, pass the path of filename as argument.
```
bin/codegen test/<filename>.py
```
The output will be saved in ```build``` directory with name <filename>.s. This can be run using SPIM simulator or on a MIPS machine.


3. To clean the executables and other helper files, run make clean.
```
make clean
```

### Directory Structure
______________________________________________________
* bin:
	* codegen [Python dependent bytecode for assembly code generation]
	* converter.py [Python source file to convert the dump of parser into dot file: may be needed for debugging]
	* lex.py [Python source file from PLY for lexing]
	* lexer.py [Python source file to specify language lexemes]
	* parser.py [Python source file to specify grammar]
	* yacc.py [Python source file from PLY for parsing ]
	* runTimeCode.py [Python source which is used for efficient allocation & maintenance of registers as a 			helper function for codegen.py]
	* symbolTable.py [Python source file with necessary functions related to symbol table]
	* tac.py [Python scource file with necessary functions related to Three Address Code Representation]
* lib:
	* code.s [Assembly source code to generate useful labels]
	* data.s [Assembly source code to allocate space for useful data spaces]
	* library.py [Python source code to be compiled using our compiler and to be used as library for the language]
* src:
	* runTimeCode.py  [ Python source which is used for efficient allocation & maintenance of registers as a 			helper function for codegen.py ]
 	* codegen.py    [ Python source file which runs the parser and uses the TAC codes to generate the final 				assembly code ]
	* converter.py [Python source file to convert the dump of parser into dot file: may be needed for debugging]
	* lex.py [Python source file from PLY for lexing]
	* lexer.py [Python source file to specify language lexemes]
	* irgen [Python dependent bytecode for parsing and semantic analysis]
	* parser.py [Python source file to specify grammar]
	* yacc.py [Python source file from PLY for parsing ]
	* symbolTable.py [Python source file with necessary functions related to symbol table]
	* tac.py [Python scource file with necessary functions related to Three Address Code Representation]
* test:
	* 'filename'.py [Test files]
* build:
	This directory is used to keep assembly code
* .gitignore
* makefile [To move the source files to bin directory and compile bytecode for lexer and making it executable]
* readme.md

A Tutorial on the language features offered by the compiler 
----------------------------------------------------------------
----------------------------------------------------------------

The compiler supports the basic structures of the Programming languages such as assignment , operators , loops ans function calls.

*Note : Indentation is through tabs or spaces

Assignment 
____________________________
```
a = 10
b = 20
```
Operators
_______________________________________

```
a = 10
b = 20
print a
print b
c = a + b
print c
```
Relational & Logical Operators
_________________________________________
```
a = 4 > 3
if a == 1 :
  print 8
c = 3 > 4
if c == 0 :
  print 9
if a or c :
  print 10
if a and c :
  print 11
if a and c or a or c :
  print 12  
```
If Statement
___________________________
```
a = 10
if a == 10:
  print 1
else :
  print 2
```

While Statement
_____________________________

```
a = 100
summ = 0
while a > 0:
  summ = summ + a
  a = a-1
print summ
```

Nested Looping
________________________

```

a = 100
summ = 0
while a > 0:
  b = 40
  while b >= 0:
    summ = summ +b
    b = b -1
    a = a - 2
  print summ

```

Some Library function calls
_________________________________


* max
```
print max(4,5)
```
* min
```
print min(4,5)
```
Function Without Parameters
______________________________________

```
def myfun():
  a = 10
  summ = 0
  while a > 0 :
    summ = summ + a
    a = a - 1
  print summ

myfun()
```

Function With Parameters
_________________________________

```

def myfun(c, d, e, f):
  a = 35
  b = a + c
  return c+d+e+f
a = myfun(1000, 100, 10, 1)
print a

```

Function call from another function
__________________________________________
```
def f():
	return 1
def f1():
	a = f()
	return 2*a
x = f1()
print x
```
Recursion
_______________________________
```

def sum(n):
	if n == 0 :
		return 0
	a = sum(n-1)
	return a + n
x = sum(100)
print x
```
Break Statement
__________________________

```
i=1
while i<=3:
  if i == 2:
    break
  else :
    i = 3
```




Continue Statement
__________________________

```
i=1
while i<=3:
  if i == 2:
    continue
  else :
    i = 3
```
Nested Functions : A special feature of our compiler
===================================================
_________________________________________________
```
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
```


# Python Compiler

## Language Features

- Library Function calls
	-some library calls such as max and min have support from our compiler
- Recursive Functions 
	- Python supports recursive functions and so does our compiler
- Function call 
	- Function call can be made from another function 

- Nested Functions
    -Python language supports a function to be nested within a function
    -Our compiler supports one function to be only accessible within the scope of another function	

- Register Allocation:
    - Remove redundancy as both caller and callee are flushing registers.
    - Make use of dirty bit
    - Update flushtemporary and flsuh registers to make used of function name
    	and dirty bit
    - Use nextReg heuristic from the Dragon Book for better optimization 
- Arguments of functions
    - Number of parameters can be varied
    - At function call time, we know the number of parameters passed

## Optimizations
- Code Motion
- Common Sub expression removal
- The nextReg and getReg functions work well after doing block analysis of the code block 
- All the operations are computed with the help of Registers which are asymptotically
- The stack is used generously used which is faster in an amortized manner
## Issues

## TODO
- Multidimensional Array
- Class
- Lambda Calculus
- More libraries
