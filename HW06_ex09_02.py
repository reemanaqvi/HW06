#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body

def has_no_e():
	f = open('words.txt')	
	e_count = 0.0
	total_lines = 0.0
	for line in f:
		if 'e' not in line:
			print line
			e_count +=1	
		total_lines +=1
	words_no_e = (e_count/total_lines) * 100 
	print str(words_no_e) + "%"
			


##############################################################################
def main():
     # Call your function(s) here.
    has_no_e()
if __name__ == '__main__':
    main()
