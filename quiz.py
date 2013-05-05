#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
This file is part of french-verb-conjugator.

french-verb-conjugator is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

french-verb-conjugator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with french-verb-conjugator. If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import colorama
from random import choice, seed, sample, shuffle
from time import time
from libconjugate import *

def challenge(verb, pronoun, tense):
	
	"""
	Handles a single challenge.
	
	Arguments:
	verb		--	The verb (e.g., 'commencer')
	pronoun		--	The pronoun (e.g., 'je')
	tense		--	The tense (e.g., 'present')
	
	Returns:
	True or False depending on whether the response was correct.	
	"""		
			  
	query =  colorama.Style.BRIGHT + verb + colorama.Style.RESET_ALL + \
		' (%s): %s ' % (tense, pronoun)
	response = raw_input(query)
	if response == 'q':
		sys.exit()
	answer = conjugate(verb, pronoun, tense)
	if response == answer:
		print colorama.Fore.GREEN + 'Correct!'
		correct = True
	else:
		correct = False
		print colorama.Fore.RED + 'Incorrect! The correct answer is "%s"' \
			% answer
	print colorama.Fore.RESET
	return correct

def quiz(length):
	
	"""
	Runs a test.
	
	Arguments:
	length		--	The number of conjugations asked.
	"""
	
	print
	print colorama.Style.BRIGHT + 'Welcome to the French verb conjugator test!'
	print colorama.Style.RESET_ALL
	print '- You will be asked to conjugate a verb for a specific pronoun and tense.'
	print '- The test consists of %d conjugations.' % length
	print '- Try to be as fast and accurate as possible!'	
	print
	print 'Press enter to begin! Type \'q\' at any time to exit.'
	response = raw_input()
	if response == 'q':
		return

	# Make a selection that favours the irregular verbs
	selection = irregular.keys() + sample(regular, length-len(irregular))
	shuffle(selection)
	
	seed()	
	correct = 0
	i = 0
	t1 = time()
	
	for verb in selection:		
		tense = choice(tenses)
		if tense == 'past participle':
			pronoun = ''
		else:
			pronoun = choice(pronouns)		
		print '%d / %d' % (i+1, length)		
		correct += challenge(verb, pronoun, tense)
		i += 1

	acc = 100.*correct/i
	t = time() - t1
	score = 100.*acc/t
	print colorama.Style.BRIGHT + 'Your results:' + colorama.Style.RESET_ALL
	print 'Accuracy: %.0f%%' % acc
	print 'Time passed: %.1fs' % t
	print 'Score: %.0f' % score
		
	print
	print 'End of test!'
	print

if __name__ == '__main__':
	
	colorama.init()
	quiz(20)
