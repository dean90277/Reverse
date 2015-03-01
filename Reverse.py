#!/bin/usr/python

complementary = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'t', 'T':'a', 'C':'g', 'G':'c'}
keeprunning = True

while (keeprunning == True):

	seq_output = ""
	seq_input = input("Please input a sequence: ")

	for base in seq_input:
		if (base in complementary): seq_output = complementary[base] + seq_output
		
	if (len(seq_output) == len(seq_input)):			#Any invalid input will result in different lengths
		print ("Input Sequence = " + seq_input)
		print ("Reversed Complementary Sequence = " + seq_output)
		if (input("Do you want to continue? (y:yes, others:no) ") == 'y'):
			keeprunning = True
		else: 
			keeprunning = False
	else:
		if (input("please input a valid sequence. Do you want to continue? (y:yes, others:no) ") == 'y'):
			keeprunning = True
		else: 
			keeprunning = False


print ("Thank you for using this program. Good bye.")



