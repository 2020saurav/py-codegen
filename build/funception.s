.data
        __myspace__:       .space     200
        __true__:          .asciiz    "true"
        __false__:         .asciiz    "false"
        __undefined__:     .asciiz    "undefined"
        __newline__:       .asciiz    "\n" 
.text

f4:
	sub		$sp,	$sp,	72
	sw		$ra,	0($sp)
	sw		$fp,	4($sp)
	la		$fp,	72($sp)
	li		$v0,	2
	la		$s5,	__myspace__
	add		$v0,	$v0,	$v0
	add		$v0,	$v0,	$v0
	add		$s6,	$v0,	$s5
	lw		$s7,	0($s6)
	sw		$s7,	8($sp)
	la		$v0,	-12($sp)
	sw		$v0,	0($s6)
	sw		$t0,	12($sp)
	sw		$t1,	16($sp)
	sw		$t2,	20($sp)
	sw		$t3,	24($sp)
	sw		$t4,	28($sp)
	sw		$t5,	32($sp)
	sw		$t6,	36($sp)
	sw		$t7,	40($sp)
	sw		$t8,	44($sp)
	sw		$t9,	48($sp)
	sw		$s0,	52($sp)
	sw		$s1,	56($sp)
	sw		$s2,	60($sp)
	sw		$s3,	64($sp)
	sw		$s4,	68($sp)
	li		$v0,	12
	sub		$sp,	$sp,	$v0
	li		$t4,	7
	move		$a0,	$t4
	jal		print_integer
	jal		print_newline
	la		$t5,	funception
	jal		$t5
	la		$s5,	__myspace__
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t5,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t4,	0($s7)
	move		$t6,	$v0
	move		$a0,	$t6
	jal		print_integer
	jal		print_newline
	move		$v0,	$t6
	b		f4end
	b		f4end
f4end:
	addi		$sp,	$sp,	12
	lw		$ra,	0($sp)
	lw		$fp,	4($sp)
	lw		$a0,	8($sp)
	li		$a1,	2
	la		$s5,	__myspace__
	add		$a1,	$a1,	$a1
	add		$a1,	$a1,	$a1
	add		$s6,	$a1,	$s5
	sw		$a0,	0($s6)
	lw		$t0,	12($sp)
	lw		$t1,	16($sp)
	lw		$t2,	20($sp)
	lw		$t3,	24($sp)
	lw		$t4,	28($sp)
	lw		$t5,	32($sp)
	lw		$t6,	36($sp)
	lw		$t7,	40($sp)
	lw		$t8,	44($sp)
	lw		$t9,	48($sp)
	lw		$s0,	52($sp)
	lw		$s1,	56($sp)
	lw		$s2,	60($sp)
	lw		$s3,	64($sp)
	lw		$s4,	68($sp)
	addi		$sp,	$sp,	72
	jr		$ra

min:
	sub		$sp,	$sp,	72
	sw		$ra,	0($sp)
	sw		$fp,	4($sp)
	la		$fp,	72($sp)
	li		$v0,	1
	la		$s5,	__myspace__
	add		$v0,	$v0,	$v0
	add		$v0,	$v0,	$v0
	add		$s6,	$v0,	$s5
	lw		$s7,	0($s6)
	sw		$s7,	8($sp)
	la		$v0,	-8($sp)
	sw		$v0,	0($s6)
	sw		$t0,	12($sp)
	sw		$t1,	16($sp)
	sw		$t2,	20($sp)
	sw		$t3,	24($sp)
	sw		$t4,	28($sp)
	sw		$t5,	32($sp)
	sw		$t6,	36($sp)
	sw		$t7,	40($sp)
	sw		$t8,	44($sp)
	sw		$t9,	48($sp)
	sw		$s0,	52($sp)
	sw		$s1,	56($sp)
	sw		$s2,	60($sp)
	sw		$s3,	64($sp)
	sw		$s4,	68($sp)
	li		$v0,	8
	sub		$sp,	$sp,	$v0
	sw		$a0,	0($sp)
	sw		$a1,	4($sp)
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t8,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t9,	0($s7)
	slt		$t3,	$t8,	$t9
	beq		$t3,	0,	label2
	move		$v0,	$t8
	b		minend
	b		label3
label2:
	move		$v0,	$t9
	b		minend
label3:
	b		minend
minend:
	addi		$sp,	$sp,	8
	lw		$ra,	0($sp)
	lw		$fp,	4($sp)
	lw		$a0,	8($sp)
	li		$a1,	1
	la		$s5,	__myspace__
	add		$a1,	$a1,	$a1
	add		$a1,	$a1,	$a1
	add		$s6,	$a1,	$s5
	sw		$a0,	0($s6)
	lw		$t0,	12($sp)
	lw		$t1,	16($sp)
	lw		$t2,	20($sp)
	lw		$t3,	24($sp)
	lw		$t4,	28($sp)
	lw		$t5,	32($sp)
	lw		$t6,	36($sp)
	lw		$t7,	40($sp)
	lw		$t8,	44($sp)
	lw		$t9,	48($sp)
	lw		$s0,	52($sp)
	lw		$s1,	56($sp)
	lw		$s2,	60($sp)
	lw		$s3,	64($sp)
	lw		$s4,	68($sp)
	addi		$sp,	$sp,	72
	jr		$ra

max:
	sub		$sp,	$sp,	72
	sw		$ra,	0($sp)
	sw		$fp,	4($sp)
	la		$fp,	72($sp)
	li		$v0,	1
	la		$s5,	__myspace__
	add		$v0,	$v0,	$v0
	add		$v0,	$v0,	$v0
	add		$s6,	$v0,	$s5
	lw		$s7,	0($s6)
	sw		$s7,	8($sp)
	la		$v0,	-8($sp)
	sw		$v0,	0($s6)
	sw		$t0,	12($sp)
	sw		$t1,	16($sp)
	sw		$t2,	20($sp)
	sw		$t3,	24($sp)
	sw		$t4,	28($sp)
	sw		$t5,	32($sp)
	sw		$t6,	36($sp)
	sw		$t7,	40($sp)
	sw		$t8,	44($sp)
	sw		$t9,	48($sp)
	sw		$s0,	52($sp)
	sw		$s1,	56($sp)
	sw		$s2,	60($sp)
	sw		$s3,	64($sp)
	sw		$s4,	68($sp)
	li		$v0,	8
	sub		$sp,	$sp,	$v0
	sw		$a0,	0($sp)
	sw		$a1,	4($sp)
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t1,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t2,	0($s7)
	sgt		$t0,	$t1,	$t2
	beq		$t0,	0,	label0
	move		$v0,	$t1
	b		maxend
	b		label1
label0:
	move		$v0,	$t2
	b		maxend
label1:
	b		maxend
maxend:
	addi		$sp,	$sp,	8
	lw		$ra,	0($sp)
	lw		$fp,	4($sp)
	lw		$a0,	8($sp)
	li		$a1,	1
	la		$s5,	__myspace__
	add		$a1,	$a1,	$a1
	add		$a1,	$a1,	$a1
	add		$s6,	$a1,	$s5
	sw		$a0,	0($s6)
	lw		$t0,	12($sp)
	lw		$t1,	16($sp)
	lw		$t2,	20($sp)
	lw		$t3,	24($sp)
	lw		$t4,	28($sp)
	lw		$t5,	32($sp)
	lw		$t6,	36($sp)
	lw		$t7,	40($sp)
	lw		$t8,	44($sp)
	lw		$t9,	48($sp)
	lw		$s0,	52($sp)
	lw		$s1,	56($sp)
	lw		$s2,	60($sp)
	lw		$s3,	64($sp)
	lw		$s4,	68($sp)
	addi		$sp,	$sp,	72
	jr		$ra

f:
	sub		$sp,	$sp,	72
	sw		$ra,	0($sp)
	sw		$fp,	4($sp)
	la		$fp,	72($sp)
	li		$v0,	1
	la		$s5,	__myspace__
	add		$v0,	$v0,	$v0
	add		$v0,	$v0,	$v0
	add		$s6,	$v0,	$s5
	lw		$s7,	0($s6)
	sw		$s7,	8($sp)
	la		$v0,	-4($sp)
	sw		$v0,	0($s6)
	sw		$t0,	12($sp)
	sw		$t1,	16($sp)
	sw		$t2,	20($sp)
	sw		$t3,	24($sp)
	sw		$t4,	28($sp)
	sw		$t5,	32($sp)
	sw		$t6,	36($sp)
	sw		$t7,	40($sp)
	sw		$t8,	44($sp)
	sw		$t9,	48($sp)
	sw		$s0,	52($sp)
	sw		$s1,	56($sp)
	sw		$s2,	60($sp)
	sw		$s3,	64($sp)
	sw		$s4,	68($sp)
	li		$v0,	4
	sub		$sp,	$sp,	$v0
	li		$t7,	9
	move		$v0,	$t7
	b		fend
	b		fend
fend:
	addi		$sp,	$sp,	4
	lw		$ra,	0($sp)
	lw		$fp,	4($sp)
	lw		$a0,	8($sp)
	li		$a1,	1
	la		$s5,	__myspace__
	add		$a1,	$a1,	$a1
	add		$a1,	$a1,	$a1
	add		$s6,	$a1,	$s5
	sw		$a0,	0($s6)
	lw		$t0,	12($sp)
	lw		$t1,	16($sp)
	lw		$t2,	20($sp)
	lw		$t3,	24($sp)
	lw		$t4,	28($sp)
	lw		$t5,	32($sp)
	lw		$t6,	36($sp)
	lw		$t7,	40($sp)
	lw		$t8,	44($sp)
	lw		$t9,	48($sp)
	lw		$s0,	52($sp)
	lw		$s1,	56($sp)
	lw		$s2,	60($sp)
	lw		$s3,	64($sp)
	lw		$s4,	68($sp)
	addi		$sp,	$sp,	72
	jr		$ra

funception:
	sub		$sp,	$sp,	72
	sw		$ra,	0($sp)
	sw		$fp,	4($sp)
	la		$fp,	72($sp)
	li		$v0,	3
	la		$s5,	__myspace__
	add		$v0,	$v0,	$v0
	add		$v0,	$v0,	$v0
	add		$s6,	$v0,	$s5
	lw		$s7,	0($s6)
	sw		$s7,	8($sp)
	la		$v0,	-8($sp)
	sw		$v0,	0($s6)
	sw		$t0,	12($sp)
	sw		$t1,	16($sp)
	sw		$t2,	20($sp)
	sw		$t3,	24($sp)
	sw		$t4,	28($sp)
	sw		$t5,	32($sp)
	sw		$t6,	36($sp)
	sw		$t7,	40($sp)
	sw		$t8,	44($sp)
	sw		$t9,	48($sp)
	sw		$s0,	52($sp)
	sw		$s1,	56($sp)
	sw		$s2,	60($sp)
	sw		$s3,	64($sp)
	sw		$s4,	68($sp)
	li		$v0,	8
	sub		$sp,	$sp,	$v0
	li		$s1,	42
	move		$a0,	$s1
	jal		print_integer
	jal		print_newline
	li		$s0,	44
	move		$v0,	$s0
	b		funceptionend
	b		funceptionend
funceptionend:
	addi		$sp,	$sp,	8
	lw		$ra,	0($sp)
	lw		$fp,	4($sp)
	lw		$a0,	8($sp)
	li		$a1,	3
	la		$s5,	__myspace__
	add		$a1,	$a1,	$a1
	add		$a1,	$a1,	$a1
	add		$s6,	$a1,	$s5
	sw		$a0,	0($s6)
	lw		$t0,	12($sp)
	lw		$t1,	16($sp)
	lw		$t2,	20($sp)
	lw		$t3,	24($sp)
	lw		$t4,	28($sp)
	lw		$t5,	32($sp)
	lw		$t6,	36($sp)
	lw		$t7,	40($sp)
	lw		$t8,	44($sp)
	lw		$t9,	48($sp)
	lw		$s0,	52($sp)
	lw		$s1,	56($sp)
	lw		$s2,	60($sp)
	lw		$s3,	64($sp)
	lw		$s4,	68($sp)
	addi		$sp,	$sp,	72
	jr		$ra

fib:
	sub		$sp,	$sp,	72
	sw		$ra,	0($sp)
	sw		$fp,	4($sp)
	la		$fp,	72($sp)
	li		$v0,	1
	la		$s5,	__myspace__
	add		$v0,	$v0,	$v0
	add		$v0,	$v0,	$v0
	add		$s6,	$v0,	$s5
	lw		$s7,	0($s6)
	sw		$s7,	8($sp)
	la		$v0,	-12($sp)
	sw		$v0,	0($s6)
	sw		$t0,	12($sp)
	sw		$t1,	16($sp)
	sw		$t2,	20($sp)
	sw		$t3,	24($sp)
	sw		$t4,	28($sp)
	sw		$t5,	32($sp)
	sw		$t6,	36($sp)
	sw		$t7,	40($sp)
	sw		$t8,	44($sp)
	sw		$t9,	48($sp)
	sw		$s0,	52($sp)
	sw		$s1,	56($sp)
	sw		$s2,	60($sp)
	sw		$s3,	64($sp)
	sw		$s4,	68($sp)
	li		$v0,	12
	sub		$sp,	$sp,	$v0
	sw		$a0,	0($sp)
	la		$s3,	f4
	jal		$s3
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s3,	0($s7)
	move		$s2,	$v0
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s4,	0($s7)
	move		$s4,	$s2
	move		$v0,	$s4
	b		fibend
	la		$s5,	__myspace__
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	sw		$t4,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t4,	0($s7)
	li		$t4,	3
	move		$a0,	$t4
	jal		print_integer
	jal		print_newline
	b		fibend
fibend:
	addi		$sp,	$sp,	12
	lw		$ra,	0($sp)
	lw		$fp,	4($sp)
	lw		$a0,	8($sp)
	li		$a1,	1
	la		$s5,	__myspace__
	add		$a1,	$a1,	$a1
	add		$a1,	$a1,	$a1
	add		$s6,	$a1,	$s5
	sw		$a0,	0($s6)
	lw		$t0,	12($sp)
	lw		$t1,	16($sp)
	lw		$t2,	20($sp)
	lw		$t3,	24($sp)
	lw		$t4,	28($sp)
	lw		$t5,	32($sp)
	lw		$t6,	36($sp)
	lw		$t7,	40($sp)
	lw		$t8,	44($sp)
	lw		$t9,	48($sp)
	lw		$s0,	52($sp)
	lw		$s1,	56($sp)
	lw		$s2,	60($sp)
	lw		$s3,	64($sp)
	lw		$s4,	68($sp)
	addi		$sp,	$sp,	72
	jr		$ra

main:
	sub		$sp,	$sp,	200
	la		$fp,	200($sp)
	la		$s5,	__myspace__
	lw		$s7,	0($s5)
	la		$v0,	-24($sp)
	sw		$v0,	0($s5)
	li		$v0,	24
	sub		$sp,	$sp,	$v0
	la		$s5,	__myspace__
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	sw		$t5,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t5,	0($s7)
	la		$t5,	max
	la		$s5,	__myspace__
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	sw		$t6,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t6,	0($s7)
	la		$t6,	min
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	sw		$t7,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t7,	0($s7)
	la		$t7,	f
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	3
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t0,	0($s7)
	la		$t0,	fib
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	sw		$t1,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	4
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t1,	0($s7)
	li		$t1,	3
	move		$a0,	$t1
	jal		$t0
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	4
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t1,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t6,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t5,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	2
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t7,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	3
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t0,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	1
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	sw		$t2,	0($s7)
	la		$s5,	__myspace__
	li		$s6,	0
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	5
	sll		$s6,	$s6,	2
	add		$s7,	$s5,	$s6
	lw		$t2,	0($s7)
	move		$t2,	$v0
	move		$a0,	$t2
	jal		print_integer
	jal		print_newline
	jal		exit
exit:
	li 		$v0, 10
	syscall

print_integer:
	li		$v0, 1 
	syscall
	jr		$ra

print_string:
	li		$v0, 4
	syscall
	jr		$ra

print_boolean:
    li      $v0, 4
    beq     $a0, $zero, print_false
print_true:
    la      $a0, __true__
    jr      print_boolean_end
print_false:
    la      $a0, __false__
print_boolean_end:
    syscall
    jr      $ra

print_undefined:
    li      $v0, 4
    la      $a0, __undefined__
    syscall
    jr      $ra

print_newline:
    li      $v0, 4
    la      $a0, __newline__
    syscall
    jr      $ra