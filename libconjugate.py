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
	
regular = open('regularverbs.txt').read().split('\n')
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
		# Check for spelling-change verb, like commencer.
		# See <http://french.about.com/od/grammar/a/spellingchangec.htm>
		if stem[-1] == 'c' and ending[0] in ('a', 'o'):
			stem = stem[:-1] + 'ç'
		# Check for spelling-change verb, like arranger.
		# See <http://french.about.com/od/grammar/a/spellingchangeg.htm>
		if stem[-1] == 'g' and ending[0] in ('a', 'o'):
			stem = stem + 'e'
	return stem + ending


