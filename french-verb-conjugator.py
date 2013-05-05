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

pronouns = 'je', 'tu', 'il', 'nous', 'vous', 'ils'
tenses = 'present', 'future', 'imperfect', 'conditional', 'past participle'

endings = {
	
	'er' : {
		'present' : ['e', 'es', 'e', 'ons', 'ez', 'ent'],
		'future' : ['erai', 'eras', 'era', 'erons', 'erez', 'eront'],
		'imperfect' : ['ais', 'ais', 'ait', 'ions', 'iez', 'aient'],
		'conditional' : ['erais', 'erais', 'erait', 'erions', 'eriez', \
			'eraient'],
		'past participle' : 'é'
		},
	'ir' : {
		'present' : ['is', 'is', 'it', 'issons', 'issez', 'issent'],
		'future' : ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
		'imperfect' : ['issais', 'issais', 'issait', 'issions', 'issiez', \
			'issaient'],
		'conditional' : ['irais', 'irais', 'irait', 'irions', 'iriez', \
			'iraient'],
		'past participle' : 'i'
		},
	're' : {
		'present' : ['s', 's', '', 'ons', 'ez', 'ent'],
		'future' : ['rai', 'ras', 'ra', 'rons', 'rez', 'ront'],
		'imperfect' : ['ais', 'ais', 'ait', 'ions', 'iez', 'aient'],
		'conditional' : ['rais', 'rais', 'rait', 'rions', 'riez', 'raient'],
		'past participle' : 'u'
		},
	}
	
irregular = {
	
	'aller' : {
		'present' : ['vais', 'vas', 'va', 'allons', 'allez', 'vont'],
		'future' : ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
		'imperfect' : ['allais', 'allais', 'allait', 'allions', 'alliez', \
			'allaient'],
		'conditional' : ['irais', 'irais', 'irait', 'irions', 'iriez', \
			'iraient'],
		'past participle' : 'allé'
		},
	
	'avoir' : {
		'present' : ['ai', 'as', 'a', 'avons', 'avez', 'ont'],
		'future' : ['aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront'],
		'imperfect' : ['avais', 'avais', 'avait', 'avions', 'aviez', 'avaient'],
		'conditional' : ['aurais', 'aurais', 'aurait', 'aurions', 'auriez', \
			'auraient'],
		'past participle' : 'eu'
		},	
		
	'être' : {
		'present' : ['suis', 'es', 'est', 'sommes', 'êtes', 'sont'],
		'future' : ['serai', 'seras', 'sera', 'serons', 'serez', 'seront'],
		'imperfect' : ['étais', 'étais', 'était', 'étions', 'étiez', 'étaient'],
		'conditional' : ['serais', 'serais', 'serait', 'serions', 'seriez', \
			'seraient'],
		'past participle' : 'été'
		},
		
	'devoir' : {
		'present' : ['dois', 'dois', 'doit', 'devons', 'devez', 'doivent'],
		'future' : ['devrais', 'devras', 'devra', 'devrons', 'devrez', \
			'devront'],
		'imperfect' : ['devais', 'devais', 'devait', 'devions', 'deviez', \
			'devaient'],
		'conditional' : ['devrais', 'devrais', 'devrait', 'devrions', \
			'devriez', 'devraient'],
		'past participle' : 'dû'
		},		
	
	'faire' : {
		'present' : ['fais', 'fais', 'fait', 'faisons', 'faites', 'font'],
		'future' : ['ferai', 'feras', 'fera', 'ferons', 'ferez', 'feront'],
		'imperfect' : ['faisais', 'faisais', 'faisait', 'faisions', 'faisez', \
			'faisaient'],
		'conditional' : ['ferais', 'ferais', 'ferait', 'ferions', 'feriez', \
			'feraient'],
		'past participle' : 'fait'
		},
		
	'mettre' : {
		'present' : ['mets', 'mets', 'met', 'mettons', 'mettez', 'mettent'],
		'future' : ['mettrai', 'mettras', 'mettra', 'mettrons', 'mettrez', \
			'mettront'],
		'imperfect' : ['mettais', 'mettais', 'mettait', 'mettions', 'mettiez', \
			'mettaient'],
		'conditional' : ['mettrais', 'mettrais', 'mettrait', 'mettrions', \
			'mettriez', 'mettraient'],
		'past participle' : 'mis'
		},			
	
	'pouvoir' : {
		'present' : ['peux', 'peux', 'peut', 'pouvons', 'pouvez', 'peuvent'],
		'future' : ['pourrai', 'pourras', 'pourra', 'pourrons', 'pourrez', \
			'pourront'],
		'imperfect' : ['pouvais', 'pouvais', 'pouvait', 'pouvions', 'pouviez', \
			'pouvaient'],
		'conditional' : ['pourrais', 'pourrais', 'pourrait', 'pourrions', \
			'pourriez', 'pourraient'],
		'past participle' : 'pu'
		},	
	
	'savoir' : {
		'present' : ['sais', 'sais', 'sait', 'savons', 'savez', 'savent'],
		'future' : ['saurai', 'sauras', 'saura', 'saurons', 'saurez', \
			'sauront'],
		'imperfect' : ['savais', 'savais', 'savait', 'savions', 'saviez', \
			'savaient'],
		'conditional' : ['saurais', 'saurais', 'saurait', 'saurions', \
			'sauriez', 'sauraient'],
		'past participle' : 'su'
		},		
	
	'voir' : {
		'present' : ['vois', 'vois', 'voit', 'voyons', 'voyez', 'voient'],
		'future' : ['verrai', 'verras', 'verra', 'verrons', 'verrez', \
			'verront'],
		'imperfect' : ['voyais', 'voyais', 'voyait', 'voyions', 'voyiez', \
			'voyaient'],
		'conditional' : ['verrais', 'verrais', 'verrait', 'verrions', \
			'verriez', 'verraient'],
		'past participle' : 'vu'
		},	
	
	}
	
regular = ['aimer', 'arriver', 'chanter', 'chercher', 'danser', 'demander', \
	'dépenser', 'détester', 'donner', 'écouter', 'étudier', 'fermer', 'goûter', \
	'jouer', 'laver', 'parler', 'passer', 'penser', 'porter', 'regarder', \
	'rêver', 'sembler', 'skier', 'travailler', 'trouver', 'visiter', 'voler', \
	'abolir', 'agir', 'avertir', 'bâtir', 'bénir', 'choisir', 'établir', \
	'étourdir', 'finir', 'grossir', 'guérir', 'malgrir', 'nourrir', 'obéir', \
	'punir', 'réfléchir', 'remplir', 'réussir', 'rougir', 'vieillir', 'attendre', \
	'défendre', 'descendre', 'entendre', 'étendre', 'fondre', 'perdre', \
	'prétendre', 'rendre', 'répandre', 'répondre', 'vendre']

verbs = regular + irregular.keys()

def conjugate(verb, pronoun, tense):
	
	"""
	Conjugates a French verb.
	
	Arguments:
	verb		--	The verb (e.g., 'commencer')
	pronoun		--	The pronoun (e.g., 'je')
	tense		--	The tense (e.g., 'present')
	
	Returns:
	The conjugated verb.
	"""
	
	if verb in irregular:
		if tense == 'past participle':
			return irregular[verb][tense]
		return irregular[verb][tense][pronouns.index(pronoun)]		
	pattern = verb[-2:]
	stem = verb[:-2]
	if tense == 'past participle':
		ending = endings[pattern][tense]
	else:
		ending = endings[pattern][tense][pronouns.index(pronoun)]	
	return stem + ending

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

def test(length):
	
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
			pronoun = 'j\'ai/ je suis'
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
	test(20)

