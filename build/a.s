.data
        __display__:       .space     200
        __true__:          .asciiz    "true"
        __false__:         .asciiz    "false"
        __undefined__:     .asciiz    "undefined"
        __newline__:       .asciiz    "\n" 
.text

main:
	sub		$sp,	$sp,	200
	la		$fp,	200($sp)
	la		$s5,	__display__
	lw		$s7,	0($s5)
	la		$v0,	-8($sp)
	sw		$v0,	0($s5)
	li		$v0,	8
	sub		$sp,	$sp,	$v0
	li		$t4,	10
	la		$s5,	__display__
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	sw		$t4,	0($s7)
label1:
	li		$t4,	0
	la		$s5,	__display__
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	lw		$t5,	0($s7)
	sgt		$t4,	$t5,	$t6
	beq		$t4,	$0,	label0
	li		$t7,	1
	sub		$t7,	$t5,	$t0
	la		$s5,	__display__
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	4
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	sw		$t7,	0($s7)
	la		$s5,	__display__
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	4
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	lw		$t7,	0($s7)
	move		$a0,	$t7
	jal		print_integer
	move		$t5,	$t7
	la		$s5,	__display__
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	lw		$s5,	0($s7)
	li		$s6,	0
	add		$s6,	$s6,	$s6
	add		$s6,	$s6,	$s6
	add		$s7,	$s5,	$s6
	sw		$t5,	0($s7)
	b		label1
label0:
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