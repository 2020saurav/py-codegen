.data
        __display__:       .space     200
        __true__:          .asciiz    "true"
        __false__:         .asciiz    "false"
        __undefined__:     .asciiz    "undefined"
        __newline__:       .asciiz    "\n" 
.text

myfucn:
	sub		$sp,	$sp,	72
	sw		$ra,	0($sp)
	sw		$fp,	4($sp)
	la		$fp,	72($sp)
	li		$v0,	1
	la		$s5,	__display__
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
	li		$t4,	10
	move		$a0,	$t4
	jal		print_integer
	
myfucnend:
	addi		$sp,	$sp,	4
	lw		$ra,	0($sp)
	lw		$fp,	4($sp)
	lw		$a0,	8($sp)
	li		$a1,	1
	la		$s5,	__display__
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
	la		$s5,	__display__
	lw		$s7,	0($s5)
	la		$v0,	-8($sp)
	sw		$v0,	0($s5)
	li		$v0,	8
	sub		$sp,	$sp,	$v0
	li		$t5,	1111
	move		$a0,	$t5
	jal		print_integer
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