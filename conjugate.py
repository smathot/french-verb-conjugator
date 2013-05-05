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

import colorama
import sys
import libconjugate

if __name__ == '__main__':
	
	verb = sys.argv[-1]
	for tense in libconjugate.tenses:
		print
		print colorama.Style.BRIGHT + tense + colorama.Style.RESET_ALL
		if tense != 'past participle':
			for pronoun in libconjugate.pronouns:
				c = libconjugate.conjugate(verb, pronoun, tense)
				print '%s\t%s' % (pronoun , c)
		else:
			c = libconjugate.conjugate(verb, None, tense)
			print 'j\'ai / je suis %s' % c
	print