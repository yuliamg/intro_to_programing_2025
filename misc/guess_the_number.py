#!/usr/bin/env python
'''
Simple demo of algorthims and big O via num guesser
'''
import random

found = False
num = random.choice(list(range(1,21)))

print('Guess the number I have in mind between 1 - 20')

while not found:
	user_num = int(input('Choose a number: '))
	if user_num == num:
		found = True
		print('You found the number!')
	elif user_num > num:
		print('Lower')
	elif user_num < num:
		print('Higher')
	elif user_num == 99:
		print('The chosen number was:', num)
		found = True
