def main():

	string = "#|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   /|~|sym   usr|~|fw   /|~|sym   bin|~|fw   /|~|sym   service|~|nn   #|~|sym   #|~|sym   A|~|dt   convenient|~|fw   wrapper|~|nn   for|~|in   the|~|dt   /|~|sym   etc|~|fw   /|~|sym   init|~|fw   .|~|.   d|~|fw   init|~|fw   scripts|~|nn   .|~|.   #|~|sym   #|~|sym   This|~|dt   script|~|nn   is|~|vb   a|~|dt   modified|~|vb   version|~|nn   of|~|in   the|~|dt   /|~|sym   sbin|~|fw   /|~|sym   service|~|nn   utility|~|nn   found|~|vb   on|~|in   #|~|sym   Red|~|np   Hat|~|np   /|~|sym   Fedora|~|np   systems|~|np   (|~|(   licensed|~|vb   GPLv2|~|np   +|~|,   )|~|)   .|~|.   #|~|sym   #|~|sym   Copyright|~|nn   (|~|(   C|~|nn   )|~|)   2006|~|cd   Red|~|np   Hat|~|np   ,|~|,   Inc|~|np   .|~|.   All|~|md   rights|~|nn   reserved|~|vb   .|~|.   #|~|sym   Copyright|~|nn   (|~|(   C|~|nn   )|~|)   2008|~|cd   Canonical|~|np   Ltd|~|np   .|~|.   #|~|sym   *|~|sym   August|~|np   2008|~|cd   -|~|--   Dustin|~|np   Kirkland|~|np   <|~|(   kirkland|~|fw   @|~|sym   canonical|~|jj   .|~|.   com|~|nn   >|~|)   #|~|sym   #|~|sym   This|~|dt   program|~|nn   is|~|vb   free|~|np   software|~|nn   ;|~|:   you|~|pr   can|~|md   redistribute|~|vb   it|~|pr   and|~|cc   /|~|sym   or|~|cc   modify|~|vb   #|~|sym   it|~|pr   under|~|in   the|~|dt   terms|~|nn   of|~|in   the|~|dt   GNU|~|np   General|~|np   Public|~|np   License|~|np   as|~|in   published|~|vb   by|~|in   #|~|sym   the|~|dt   Free|~|np   Software|~|np   Foundation|~|np   ;|~|:   either|~|cc   version|~|nn   2|~|cd   of|~|in   the|~|dt   License|~|np   ,|~|,   or|~|cc   #|~|sym   (|~|(   at|~|in   your|~|pr   option|~|nn   )|~|)   any|~|dt   later|~|jj   version|~|nn   .|~|.   #|~|sym   #|~|sym   This|~|dt   program|~|nn   is|~|vb   distributed|~|vb   in|~|in   the|~|dt   hope|~|nn   that|~|in   it|~|pr   will|~|md   be|~|vb   useful|~|jj   ,|~|,   #|~|sym   but|~|cc   WITHOUT|~|in   ANY|~|dt   WARRANTY|~|nn   ;|~|:   without|~|in   even|~|rb   the|~|dt   implied|~|vb   warranty|~|nn   of|~|in   #|~|sym   MERCHANTABILITY|~|nn   or|~|cc   FITNESS|~|nn   FOR|~|in   A|~|dt   PARTICULAR|~|jj   PURPOSE|~|nn   .|~|.   See|~|vb   the|~|dt   #|~|sym   GNU|~|np   General|~|np   Public|~|np   License|~|np   for|~|in   more|~|jj   details|~|nn   .|~|.   #|~|sym   #|~|sym   You|~|pr   should|~|md   have|~|vb   received|~|vb   a|~|dt   copy|~|vb   of|~|in   the|~|dt   GNU|~|np   General|~|np   Public|~|np   License|~|np   #|~|sym   along|~|in   with|~|in   this|~|dt   program|~|nn   ;|~|:   if|~|in   not|~|rb   ,|~|,   write|~|vb   to|~|to   the|~|dt   Free|~|np   Software|~|np   #|~|sym   Foundation|~|np   ,|~|,   Inc|~|np   .|~|.   ,|~|,   59|~|cd   Temple|~|np   Place|~|np   ,|~|,   Suite|~|np   330|~|cd   ,|~|,   Boston|~|np   ,|~|,   MA|~|np   02111|~|cd   -|~|--   1307|~|cd   USA|~|np   #|~|sym   #|~|sym   On|~|in   Debian|~|np   GNU|~|np   /|~|sym   Linux|~|np   systems|~|np   ,|~|,   the|~|dt   complete|~|jj   text|~|nn   of|~|in   the|~|dt   GNU|~|np   General|~|np   #|~|sym   Public|~|np   License|~|np   can|~|md   be|~|vb   found|~|vb   in|~|in   `|~|sym   /|~|sym   usr|~|fw   /|~|sym   share|~|fw   /|~|sym   common|~|fw   -|~|--   licenses|~|nn   /|~|sym   GPL|~|np   -|~|--   2|~|cd   '|~|\"   .|~|.   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   #|~|sym   "

	# expand contractions:
	string = string.replace("ain't", "are not")
	string = string.replace("won't", "will not")
	string = string.replace("can't", "cannot")
	string = string.replace("n't", " not")
	string = string.replace("'re", " are")
	string = string.replace("'m", " am")
	string = string.replace("'ll", " will")
	string = string.replace("'ve", " have")

	# Need to perform the compression of number . number
	# Need to perform the compression of propperNoun .
	# NEED TO REMOVE OR SOMEHOW HANDLE NON-ASCII CHARACTERS <- IF THIS OCCURS NON GRACEFUL FAILURE
	string = compressNP( string )
	string = newExtractNotice( string )

	print( string )



"""
Makes the DFA's transition states and symbols then returns them
"""
def mkNewDFA():
	states = [ x for x in range(14) ]
	symbols = [ 'copyright', 'c', '(', ')', 'cd', 'np', 'dt', 'in', '--', ',', '.', 'sym', 'cc']
	DFA = dict()
	DFA[(0, 'copyright', 'nn')] = 0
	DFA[(1, 'copyright', 'nn')] = 0
	DFA[(2, 'copyright', 'nn')] = 0
	DFA[(3, 'copyright', 'nn')] = 0
	DFA[(4, 'copyright', 'nn')] = 0
	DFA[(5, 'copyright', 'nn')] = 0
	DFA[(6, 'copyright', 'nn')] = 0
	DFA[(7, 'copyright', 'nn')] = 0
	DFA[(8, 'copyright', 'nn')] = 0
	DFA[(9, 'copyright', 'nn')] = 0
	DFA[(10, 'copyright', 'nn')] = 0
	DFA[(11, 'copyright', 'nn')] = 0
	DFA[(12, 'copyright', 'nn')] = 0
	DFA[(13, 'copyright', 'nn')] = 0


	DFA[(0, 'c', 'nn')] = 2
	DFA[(1, 'c', 'nn')] = 2
	DFA[(2, 'c', 'nn')] = 11
	DFA[(3, 'c', 'nn')] = 11
	DFA[(4, 'c', 'nn')] = 11
	DFA[(5, 'c', 'nn')] = 11
	DFA[(6, 'c', 'nn')] = 11
	DFA[(7, 'c', 'nn')] = 11
	DFA[(8, 'c', 'nn')] = 11
	DFA[(9, 'c', 'nn')] = 11
	DFA[(10, 'c', 'nn')] = 11
	DFA[(11, 'c', 'nn')] = 11
	DFA[(12, 'c', 'nn')] = 11
	DFA[(13, 'c', 'nn')] = 11

	DFA[(0, 'X', '(')] = 1
	DFA[(1, 'X', '(')] = 11
	DFA[(2, 'X', '(')] = 11
	DFA[(3, 'X', '(')] = 11
	DFA[(4, 'X', '(')] = 11
	DFA[(5, 'X', '(')] = 11
	DFA[(6, 'X', '(')] = 11
	DFA[(7, 'X', '(')] = 11
	DFA[(8, 'X', '(')] = 11
	DFA[(9, 'X', '(')] = 11
	DFA[(10, 'X', '(')] = 11
	DFA[(11, 'X', '(')] = 11
	DFA[(12, 'X', '(')] = 11
	DFA[(13, 'X', '(')] = 11

	DFA[(0, 'X', ')')] = 11
	DFA[(1, 'X', ')')] = 3
	DFA[(2, 'X', ')')] = 3
	DFA[(3, 'X', ')')] = 11
	DFA[(4, 'X', ')')] = 11
	DFA[(5, 'X', ')')] = 11
	DFA[(6, 'X', ')')] = 11
	DFA[(7, 'X', ')')] = 11
	DFA[(8, 'X', ')')] = 11
	DFA[(9, 'X', ')')] = 11
	DFA[(10, 'X', ')')] = 11
	DFA[(11, 'X', ')')] = 11
	DFA[(12, 'X', ')')] = 3
	DFA[(13, 'X', ')')] = 11

	DFA[(0, 'X', 'cd')] = 6
	DFA[(1, 'X', 'cd')] = 11
	DFA[(2, 'X', 'cd')] = 11
	DFA[(3, 'X', 'cd')] = 6
	DFA[(4, 'X', 'cd')] = 6
	DFA[(5, 'X', 'cd')] = 6
	DFA[(6, 'X', 'cd')] = 6
	DFA[(7, 'X', 'cd')] = 6
	DFA[(8, 'X', 'cd')] = 11
	DFA[(9, 'X', 'cd')] = 11
	DFA[(10, 'X', 'cd')] = 10
	DFA[(11, 'X', 'cd')] = 11
	DFA[(12, 'X', 'cd')] = 6
	DFA[(13, 'X', 'cd')] = 6

	DFA[(0, 'X', 'np')] = 4
	DFA[(1, 'X', 'np')] = 11
	DFA[(2, 'X', 'np')] = 11
	DFA[(3, 'X', 'np')] = 4
	DFA[(4, 'X', 'np')] = 4
	DFA[(5, 'X', 'np')] = 4
	DFA[(6, 'X', 'np')] = 4
	DFA[(7, 'X', 'np')] = 4
	DFA[(8, 'X', 'np')] = 4
	DFA[(9, 'X', 'np')] = 4
	DFA[(10, 'X', 'np')] = 10
	DFA[(11, 'X', 'np')] = 11
	DFA[(12, 'X', 'np')] = 4
	DFA[(13, 'X', 'np')] = 4

	DFA[(0, 'X', 'dt')] = 9
	DFA[(1, 'X', 'dt')] = 11
	DFA[(2, 'X', 'dt')] = 11
	DFA[(3, 'X', 'dt')] = 9
	DFA[(4, 'X', 'dt')] = 9
	DFA[(5, 'X', 'dt')] = 9
	DFA[(6, 'X', 'dt')] = 9
	DFA[(7, 'X', 'dt')] = 9
	DFA[(8, 'X', 'dt')] = 9
	DFA[(9, 'X', 'dt')] = 11
	DFA[(10, 'X', 'dt')] = 11
	DFA[(11, 'X', 'dt')] = 11
	DFA[(12, 'X', 'dt')] = 11
	DFA[(13, 'X', 'dt')] = 9

	DFA[(0, 'X', 'in')] = 11
	DFA[(1, 'X', 'in')] = 11
	DFA[(2, 'X', 'in')] = 11
	DFA[(3, 'X', 'in')] = 11
	DFA[(4, 'X', 'in')] = 8
	DFA[(5, 'X', 'in')] = 11
	DFA[(6, 'X', 'in')] = 8
	DFA[(7, 'X', 'in')] = 11
	DFA[(8, 'X', 'in')] = 11
	DFA[(9, 'X', 'in')] = 11
	DFA[(10, 'X', 'in')] = 11
	DFA[(11, 'X', 'in')] = 11
	DFA[(12, 'X', 'in')] = 11
	DFA[(13, 'X', 'in')] = 8

	DFA[(0, 'X', '--')] = 11
	DFA[(1, 'X', '--')] = 11
	DFA[(2, 'X', '--')] = 11
	DFA[(3, 'X', '--')] = 11
	DFA[(4, 'X', '--')] = 7
	DFA[(5, 'X', '--')] = 11
	DFA[(6, 'X', '--')] = 7
	DFA[(7, 'X', '--')] = 11
	DFA[(8, 'X', '--')] = 11
	DFA[(9, 'X', '--')] = 11
	DFA[(10, 'X', '--')] = 11
	DFA[(11, 'X', '--')] = 11
	DFA[(12, 'X', '--')] = 11
	DFA[(13, 'X', '--')] = 11

	DFA[(0, 'X', ',')] = 11
	DFA[(1, 'X', ',')] = 11
	DFA[(2, 'X', ',')] = 11
	DFA[(3, 'X', ',')] = 11
	DFA[(4, 'X', ',')] = 5
	DFA[(5, 'X', ',')] = 11
	DFA[(6, 'X', ',')] = 5
	DFA[(7, 'X', ',')] = 11
	DFA[(8, 'X', ',')] = 11
	DFA[(9, 'X', ',')] = 11
	DFA[(10, 'X', ',')] = 11
	DFA[(11, 'X', ',')] = 11
	DFA[(12, 'X', ',')] = 11
	DFA[(13, 'X', ',')] = 11

	DFA[(0, 'X', '.')] = 11
	DFA[(1, 'X', '.')] = 11
	DFA[(2, 'X', '.')] = 11
	DFA[(3, 'X', '.')] = 11
	DFA[(4, 'X', '.')] = 10
	DFA[(5, 'X', '.')] = 11
	DFA[(6, 'X', '.')] = 10
	DFA[(7, 'X', '.')] = 11
	DFA[(8, 'X', '.')] = 11
	DFA[(9, 'X', '.')] = 11
	DFA[(10, 'X', '.')] = 11
	DFA[(11, 'X', '.')] = 11
	DFA[(12, 'X', '.')] = 11
	DFA[(13, 'X', '.')] = 11

	DFA[(0, 'X', 'sym')] = 12
	DFA[(1, 'X', 'sym')] = 12
	DFA[(2, 'X', 'sym')] = 11
	DFA[(3, 'X', 'sym')] = 11
	DFA[(4, 'X', 'sym')] = 10
	DFA[(5, 'X', 'sym')] = 11
	DFA[(6, 'X', 'sym')] = 11
	DFA[(7, 'X', 'sym')] = 11
	DFA[(8, 'X', 'sym')] = 11
	DFA[(9, 'X', 'sym')] = 11
	DFA[(10, 'X', 'sym')] = 11
	DFA[(11, 'X', 'sym')] = 11
	DFA[(12, 'X', 'sym')] = 11
	DFA[(13, 'X', 'sym')] = 11

	DFA[(0, 'X', 'cc')] = 11
	DFA[(1, 'X', 'cc')] = 11
	DFA[(2, 'X', 'cc')] = 11
	DFA[(3, 'X', 'cc')] = 11
	DFA[(4, 'X', 'cc')] = 13
	DFA[(5, 'X', 'cc')] = 11
	DFA[(6, 'X', 'cc')] = 13
	DFA[(7, 'X', 'cc')] = 11
	DFA[(8, 'X', 'cc')] = 13
	DFA[(9, 'X', 'cc')] = 13
	DFA[(10, 'X', 'cc')] = 11
	DFA[(11, 'X', 'cc')] = 11
	DFA[(12, 'X', 'cc')] = 11
	DFA[(13, 'X', 'cc')] = 11

	DFA[(0, 'X', 'X')] = 11
	DFA[(1, 'X', 'X')] = 11
	DFA[(2, 'X', 'X')] = 11
	DFA[(3, 'X', 'X')] = 11
	DFA[(4, 'X', 'X')] = 10
	DFA[(5, 'X', 'X')] = 11
	DFA[(6, 'X', 'X')] = 10
	DFA[(7, 'X', 'X')] = 11
	DFA[(8, 'X', 'X')] = 11
	DFA[(9, 'X', 'X')] = 11
	DFA[(10, 'X', 'X')] = 11
	DFA[(11, 'X', 'X')] = 11
	DFA[(12, 'X', 'X')] = 11
	DFA[(13, 'X', 'X')] = 11

	return states, symbols, DFA



"""
Given a DFA and a tagged string with the delimeter |~| this will
extract the copyright notice if it exists in the given string. returns the
string of a copyright notice(s) or None.
"""
def newExtractNotice( string ):
	states, symbols, DFA = mkNewDFA()

	extractedNotice = ''
	# assuming this is a valid string that this function can take
	string = string.strip()
	string = string.split()
	# string should now be a list of word|~|tag strings.

	currentState = 11          # initialize my state machine
	potentialNotice = ''      # initalize my notice outside of the loop
	for word in string:

		word = word.strip()
		word = word.split('|~|')
		currentWord = word[0]
		currentTag = word[1]

		if currentState == 10:
			extractedNotice = extractedNotice + potentialNotice + '\n'
			potentialNotice = ''

		if currentWord.lower() == 'copyright' or currentWord.lower() == 'c':
			currentState = DFA[(currentState, currentWord.lower(), currentTag)]
		elif currentTag in symbols:
			currentState = DFA[(currentState, 'X', currentTag)]
		else:
			currentState = DFA[(currentState, 'X', 'X')]

		if currentState == 0:
			if len(potentialNotice) > 12:  # this is to ensure that there is at least more than one word.
				extractedNotice = extractedNotice + potentialNotice + '\n'
				potentialNotice = currentWord + ' '
			else:
				potentialNotice = currentWord + ' '
		elif currentState != 11 and currentState != 10:
			potentialNotice = potentialNotice + currentWord + ' '

	# the final check is more vauge because of short strings that might not have
	# the time to transition to the final accept state
	if currentState == 10 or currentState == 6 or currentState == 4:
		extractedNotice = extractedNotice + potentialNotice + '\n'

	if extractedNotice != '':
		return extractedNotice
	return 'No notice could be found.'




"""
DFA required for the compression of numbers in a string
"""
def mkNumCompressDFA():
	states = [0, 1, 2, 3]
	symbols = [ 'cd', '.']

	DFA = dict()
	DFA[(0, 'X', 'cd')] = 0
	DFA[(1, 'X', 'cd')] = 3
	DFA[(2, 'X', 'cd')] = 0
	DFA[(3, 'X', 'cd')] = 0

	DFA[(0, '.', '.')] = 1
	DFA[(1, '.', '.')] = 2
	DFA[(2, '.', '.')] = 2
	DFA[(3, '.', '.')] = 2

	DFA[(0, '?', '.')] = 2
	DFA[(1, '?', '.')] = 2
	DFA[(2, '?', '.')] = 2
	DFA[(3, '?', '.')] = 2

	DFA[(0, '!', '.')] = 2
	DFA[(1, '!', '.')] = 2
	DFA[(2, '!', '.')] = 2
	DFA[(3, '!', '.')] = 2

	DFA[(0, 'X', 'X')] = 2
	DFA[(1, 'X', 'X')] = 2
	DFA[(2, 'X', 'X')] = 2
	DFA[(3, 'X', 'X')] = 2

	return states, symbols, DFA

"""
Given a string this will compress floating point numnbers
or numbers that contain a decimal point
"""
def compressNumInString( string ):
	states, symbols, DFA = mkNumCompressDFA()

	finalString = ''
	# assuming this is a valid string that this function can take
	string = string.strip()
	string = string.split()
	# string should now be a list of word|~|tag strings.

	currentState = 2          # initialize my state machine
	compNum = ''      # initalize my notice outside of the loop
	saveNum = ''
	for word in string:
		word = word.strip()
		word = word.split('|~|')

		if word[1] == '.':
			currentState = DFA[(currentState, word[0], word[1])]
		elif word[1] == 'cd':
			currentState = DFA[(currentState, 'X', word[1])]
		else:
			currentState = DFA[(currentState, 'X', 'X')]

		if currentState == 0:
			finalString = finalString + saveNum
			compNum = word[0]
			saveNum = word[0] + '|~|' + word[1] + '   '
		elif currentState == 1:
			compNum = compNum + '.'
			saveNum = saveNum + word[0] + '|~|' + word[1] + '   '
		elif currentState == 2:
			finalString = finalString + saveNum
			saveNum = ''
			finalString = finalString + word[0] + '|~|' + word[1] + '   '
		elif currentState == 3:
			compNum = compNum + word[0]
			saveNum = compNum + '|~|cd   '
			currentState = 0

	if currentState != 2:
		finalString = finalString + saveNum

	return finalString



"""
Given a string this will compress propper nouns and periods into a single tag
that is a propper noun
"""
def compressNP( string ):
	finalString = ''
	# assuming this is a valid string that this function can take
	string = string.strip()
	string = string.split()
	# string should now be a list of word|~|tag strings.

	prevTag = ''

	for word in string:
		word = word.strip()
		word = word.split('|~|')

		if prevTag == 'np' and word[0] == '.':
			finalString = finalString + '.|~|np   '
		elif prevTag == 'np' and word[1] == 'np':
			finalString = finalString + '|~|np   ' + word[0]
		elif prevTag == 'np' and word[0] != '.':
			finalString = finalString + '|~|np   ' + word[0] + '|~|' + word[1] + '   '
		elif word[1] == 'np':
			finalString = finalString + word[0]
		else:
			finalString = finalString + word[0] + '|~|' + word[1] + '   '

		prevTag = word[1]

	if prevTag == 'np':
		finalString = finalString + '|~|np   '

	return finalString


main()









