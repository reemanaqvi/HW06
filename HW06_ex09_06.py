#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body
def is_abecedarian(word):
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	else:
		return is_abecedarian(word[1:])

##############################################################################
def main():
    # pass  # Call your function(s) here.
    counter = 0
    fin = open("words.txt", "r")
    for word in fin:
    	if is_abecedarian(word):
    		counter +=1
    fin.close()
    print ("The number of abecedarian words is: %d") %(counter)
if __name__ == '__main__':
    main()
