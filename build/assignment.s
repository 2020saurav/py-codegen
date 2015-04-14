.data
        __myspace__:       .space     200
        __true__:          .asciiz    "true"
        __false__:         .asciiz    "false"
        __undefined__:     .asciiz    "undefined"
        __newline__:       .asciiz    "\n" 
.text

main:
	sub		$sp,	$sp,	200
	la		$fp,	200($sp)
	la		$s5,	__myspace__
	lw		$s7,	0($s5)
	la		$v0,	-20($sp)
	sw		$v0,	0($s5)
	li		$v0,	20
	sub		$sp,	$sp,	$v0
	li		$t4,	10
	li		$t5,	20
	move		$a0,	$t4
	jal		print_integer
	jal		print_newline
	move		$a0,	$t5
	jal		print_integer
	jal		print_newline
	add		$t6,	$t4,	$t5
	move		$a0,	$t6
	jal		print_integer
	jal		print_newline
	mult		$t4,	$t6
	mflo		$t7
	move		$t5,	$t7
	move		$a0,	$t5
	jal		print_integer
	jal		print_newline
	mult		$t5,	$t5
	mflo		$t0
	move		$t5,	$t0
	move		$a0,	$t5
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