#CS220,Group09
#12616,12640
#multiply.asm

#We implement multiply by analyzing the multiplier digit by digit and doing the following operations :-
#All numbers are stpred in linked lists in reverse order for ease of arithmetic operations
#the temporary linked list and answer linked list are initialized to 0.
#The size of temporary linked list = 1+sizeof(multiplicand), and size of answer=sizeof(multiplicand)+sizeof(multiplier)  , so we take maximum sizes in beginning and remove excess zeros in end if necessary
#We append -1 to end of all linked lists to mark their end
#Multiply the multiplier by the current digit in a temporary linked list. 
#Append the necessary number of zeroes to the temporary linked list
#Add this to the linked list that stores the answer
#Remove the appended zeroes from the temporary linked list
#Repeat until you reach -1 in the linked list storing the multiplier

#Use of registers
#t0 holds the head of multiplicand
#t1 holds the head of multiplier
#t2 holds the head of temporary linked list
#t3 holds the head of linked list storing the product/answer
#t4 is used to iterate over multiplicand
#t1 is used to iterate over multiplier
#t5 is used to iterate over temporary linked list
#t6 is used to iterate over answer linked list
#t9 is used to store the count of zeros
#t7,t8 along with t4,t5 and t6(whichever is not being used that time as an iterator) are used to store the temporary variables needed at that time 
#a1,a2 and a3 can also be used for storing temporary variables
#Also besides these conventions, any register that is not in use during a process is used to store temporary values to minimise the use of registers.
#a1 is used to store carry during array multiplication and addition

.text
.globl main
main:
	li $t7, -1	
	li $a0, 8	#starting all linked lists with a -1.
	li $v0, 9
	syscall
	sw $t7, 0($v0)
	sw $zero, 4($v0)
	addi $t0,$v0,0		#t0 contains start of multiplicand containing linked list

	li $a0, 8	
	li $v0, 9
	syscall
	sw $t7, 0($v0)
	sw $zero, 4($v0)
	addi $t1,$v0,0		#t1 contains start of multiplier containing linked list

	li $a0, 8	
	li $v0, 9
	syscall
	sw $t7, 0($v0)
	sw $zero, 4($v0)
	addi $t2,$v0,0		#t2 contains start of temporary linked list

	li $a0, 8	
	li $v0, 9
	syscall
	sw $t7, 0($v0)
	sw $zero, 4($v0)
	addi $t3,$v0,0		#t3 contains start of answer containing linked list
	
	la $a0, query_msg
	li $v0, 4
	syscall
	
first_1:			#input first number
	li $v0, 5
	syscall
	bgt $v0, 9, err		#print error if first input of first number is >=10
	b first_2

first_2:
	bgt $v0, 9, second_1	#check everytime for current input >=10
	move $t7, $v0
	li $a0, 8
	li $v0, 9
	syscall
	sw $t7, 0($v0)		#appending the current input at head of multiplicand list, this stores the number in reverse
	sw $t0, 4($v0)
	addi $t0,$v0,0		#updating the new head

	li $a0, 8
	li $v0, 9
	syscall
	sw $zero, 0($v0)	#appending zero at head of temporary list, initially all zeros
	sw $t2, 4($v0)
	addi $t2,$v0,0		#updating the new head

	li $a0, 8
	li $v0, 9
	syscall
	sw $zero, 0($v0)	#appending zero at head of answer list, initially all zeros
	sw $t3, 4($v0)
	addi $t3,$v0,0		#updating the new head

	li $v0, 5
	syscall
	b first_2

second_1:			#input second number	
	
	li $a0, 8		#temp can be atmost one digit more than multiplicand, so an extra node added
	li $v0, 9
	syscall
	sw $zero, 0($v0)	#appending zero at head of temporary list, initially all zeros
	sw $t2, 4($v0)
	addi $t2,$v0,0		#updating the new head

	li $t9, 0		#t9 stores the count of padded zeros, initially set to 0	
	li $v0, 5
	syscall
	bgt $v0, 9, err		#print error if first input of second number is >=10
	b second_2

second_2:
	bgt $v0, 9, multiply_main 	#initiate multiply when the number ends
	move $t7, $v0
	li $a0, 8
	li $v0, 9
	syscall
	sw $t7, 0($v0)			#appending the current input at head of multiplier linked list
	sw $t1, 4($v0)
	addi $t1,$v0,0			#updating the new head

	li $a0, 8
	li $v0, 9
	syscall
	sw $zero, 0($v0)		#appending more zeroes to answer linked list(its size is atmost sizeof(multiplier) + sizeof(multiplicand)
	sw $t3, 4($v0)
	addi $t3,$v0,0			#updating the new head

	li $v0, 5
	syscall
	b second_2

#t8 stores the current digit being analyzed
multiply_main:
	lw $t8, 0($t1)			#start multiplying
	beq $t8, -1, reverse_ans1	#end of linked list, go to reversing and then printing
	addi $t4,$t0,0			#setting the iterators over multiplicand and temp to head of list
	addi $t5,$t2,0	
	li $a1, 0			#set carry to 0 initially
	b multiply_digit
		
	

#t6,t7,a1,a2 and a3 are free at this moment and we use them for temporary variables
#t8 stores the digit to be multiplied
multiply_digit:
	lw $t7, 0($t4)			#t7 stores the current digit in multiplicand
	beq $t7,-1, carry_check1	#check for final carry once multiplicand's end is reached
	mul $t6, $t8, $t7
	add $t6,$t6,$a1			
	li $t7, 10
	div $t6, $t7
	mflo $a1			#a1 contains the carry from this operation
	mfhi $t7			#t7 contains the digit from this operation
	sw $t7, 0($t5)			#store the digit in temp
	lw $t5, 4($t5)			#go to next digit of temp and multiplicand
	lw $t4, 4($t4)
	b multiply_digit

carry_check1:
	addi $t6,$t9,0		#the no of zeroes to be padded
	sw $a1, 0($t5)		#the leftmost digit in temp is equal to carry 	
	b pad_zero

pad_zero:
	beqz $t6, jump_1	#jump_1 links to addition in answer linked list, go there once the zeros have been padded
	li $a0, 8
	li $v0, 9
	syscall
	sw $zero, 0($v0)	#appending zero at head of temporary list
	sw $t2, 4($v0)
	addi $t2,$v0,0		#updating the new head
	addi $t6,$t6,-1
	b pad_zero
	

jump_1:
	addi $t5,$t2,0
	addi $t6,$t3,0			#setting iterator over temp and ans to head of list
	li $a1, 0			#setting carry to 0
	b add_ans

jump_2:
	lw $t1, 4($t1)			#now t1 stores the next address
	addi $t9,$t9,1			#update the count of zeroes to be padded in t9			
	b multiply_main
		

#now t4,a1,a2,t7,t8 and a3 are free
add_ans:
	lw $t7, 0($t5)			#t7 and t8 contain the current digit in ans and temp linked list
	lw $t8, 0($t6)
	beq $t7, -1, carry_check2	#since temp is smaller, it will reach -1 first,after it does check for any carry that remains
	add $t4,$t7,$t8			
	add $t4,$t4,$a1			#getting the sum of current digits and carry
	li $t7, 10
	div $t4, $t7
	mflo $a1			#a1 contains the carry from the operation
	mfhi $t7			#t7 contains the digit from the operation
	sw $t7, 0($t6)			#store the digit in ans linked list node
	lw $t5, 4($t5)			#go to the next digit of ans and temp linked list
	lw $t6, 4($t6)
	b add_ans

carry_check2:
	lw $t8, 0($t6)			#we keep on adding the carry unless we reach end of ans
	beq $t8, -1, remove_padding1	#after we reach end of ans, we remove the padded zeroes to restore it to original size
	add $t8,$t8,$a1			#add carry to current digit
	li $t7, 10
	div $t8, $t7
	mflo $a1			#a1 contains the carry from the operation
	mfhi $t8			#t8 contains the digit from the operation
	sw $t8, 0($t6)			#store the updated digit in ans
	lw $t6, 4($t6)
	b carry_check2	


#This is done when the product has been calculated
#t0 is now used to store the head of reversed list
#a check is implemented to remove unnecessary zeroes in the product 
reverse_ans1:
	li $a0, 8
	li $v0, 9
	syscall
	li $t7, -1		
	sw $t7, 0($v0)			#A new linked list is created with t0 storing the head and initial node containing -1
	sw $zero, 4($v0)
	move $t0,$v0
	b reverse_ans2			#now the list is reversed by taking input in reverse from ans
		
#$t1 stores the value of current node in ans 
reverse_ans2:
	lw $t1, 0($t3)
	beq $t1, -1 remove_zero		#if we remove end of ans, list has been reversed and we remove extra zeroes
	li $a0, 8
	li $v0, 9
	syscall
	sw $t1, 0($v0)			#Store the current digit in ans at head of the current list, thus reversing the ans list 
	sw $t0, 4($v0)
	move $t0,$v0			#Updating the new head
	lw $t3, 4($t3)	
	b reverse_ans2


#to remove unnecessary zeroes after list has been reversed
remove_zero:
	lw $s1, 4($t0)			
	lw $s0, 0($s1)			# $s1 stores the address of the next element in the list. $s0 stores the data in the
	beq $s0, -1, print_start	# next node. If the next node has -1, we are at the end of the list. It has to be printed 
					# irrespective of whether it is 0 or not
					
				
	lw $t1, 0($t0)			#t1 stores the input value in head of reversed list
	bnez $t1, print_start		#if not zero, start printing
	lw $t0, 4($t0)			#else update t0 to the next node, thus removing the node containing 0
	b remove_zero

remove_padding1:
	addi $t6,$t9,0			#set the number of zeroes to be removed
	b remove_padding2

remove_padding2:			#remove padded zeroes from temp
	beqz $t6, jump_2		#once zeroes are removed, go to jump_2 which links back to the multiplier
	lw $t2, 4($t2)
	addi $t6,$t6,-1
	b remove_padding2
	

print_start:				#print output message
	la $a0, output_msg
	li $v0, 4
	syscall
	b print_list

print_list:				#print the linked list
	lw $a0, 0($t0)			
	beq $a0, -1, exit		#exit, once you have reached the end of list
	li $v0, 1			#print current digit
	syscall
	la $a0, space_msg		#print space
	li $v0, 4
	syscall
	lw $t0, 4($t0)			#go to next digit
	b print_list
	

err:					#print error message
	la $a0, err_msg
	li $v0, 4
	syscall

exit:					#exit
	la $a0, nl_msg
	li $v0, 4
	syscall	
	li $v0, 10
	syscall


.data
query_msg: .asciiz "Enter the input : \n"
space_msg: .asciiz " "
nl_msg: .asciiz "\n"
output_msg: .asciiz "The product is :- \n"
err_msg: .asciiz "Empty number \n"


