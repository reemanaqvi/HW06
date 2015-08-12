#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body

def uses_all(w, req):
	for letter in req:
		if letter not in w:
			return False
		else:
			return True


def uses_vowels():
	f = open('words.txt')
	req = "aeiou"
	count = 0
	for line in f:
		if uses_all (line, req):
			count += 1
			

def uses_aeiouy():
	f = open('words.txt')
	req = "aeiouy"
	count = 0
	for line in f:
		if uses_all (line, req):
			count += 1
		


##############################################################################
def main():
    pass  # Call your function(s) here.
    print uses_all("betwirknd", "bg")
    uses_vowels()
    uses_aeiouy()
if __name__ == '__main__':
    main()
