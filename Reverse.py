#!/bin/usr/python

Complimentary = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'t', 'T':'a', 'C':'g', 'G':'c'}
Continue = True

while (Continue == True):

	Seq_output = ""
	Seq_input = raw_input("Please input a sequence: ")

	for base in Seq_input:
		if (base in Complimentary): Seq_output = Complimentary[base] + Seq_output
		
	if (len(Seq_output) == len(Seq_input)):			#Any invalid input will result in different lengths
		print "Input Sequence = " + Seq_input
		print "Reversed Complimentary Sequence = " + Seq_output
		if (raw_input("Do you want to continue? (y:yes, others:no) ") == 'y'):
			Continue = True
		else: 
			Continue = False
	else:
		if (raw_input("please input a valid sequence. Do you want to continue? (y:yes, others:no) ") == 'y'):
			Continue = True
		else: 
			Continue = False


print "Thank you for using this program. Good bye."



