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
	count = 0
	for letter in req:
		if letter in w:
			count +=1
	if count == len(req):
		return True
	else:
		return False

def words_use_all(req):
	fin = open("words.txt")
	count = 0
	for word in fin:
		if uses_all(word, req):
			count +=1
	print count 


		


##############################################################################
def main():
    print words_use_all("aeiou")
    print words_use_all("aeiouy")    
if __name__ == '__main__':
    main()
