def main():

	string = "Copyright|~|nn   (|~|(   c|~|nn   )|~|)   2015|~|cd   Harlan|~|np   Haskins|~|np   Permission|~|nn   is|~|vb   hereby|~|rb   granted|~|vb   ,|~|,   free|~|np   of|~|in   charge|~|nn   ,|~|,   to|~|to   any|~|dt   person|~|nn   obtaining|~|vb   a|~|dt   copy|~|nn   of|~|in   this|~|dt   software|~|nn   and|~|cc   associated|~|jj   documentation|~|nn   files|~|nn   (|~|(   the|~|dt   \"|~|\"   Software|~|nn   ,|~|,   to|~|to   deal|~|vb   in|~|in   the|~|dt   Software|~|np   without|~|in   restriction|~|nn   ,|~|,   including|~|vb   without|~|in   limitation|~|nn   the|~|dt   rights|~|nn   to|~|to   use|~|vb   ,|~|,   copy|~|vb   ,|~|,   modify|~|vb   ,|~|,   merge|~|vb   ,|~|,   publish|~|vb   ,|~|,   distribute|~|vb   ,|~|,   sublicense|~|vb   ,|~|,   and|~|cc   /|~|sym   or|~|cc   sell|~|vb   copies|~|nn   of|~|in   the|~|dt   Software|~|np   ,|~|,   and|~|cc   to|~|to   permit|~|vb   persons|~|nn   to|~|to   whom|~|pr   the|~|dt   Software|~|np   is|~|vb   furnished|~|vb   to|~|to   do|~|vb   so|~|rb   ,|~|,   subject|~|vb   to|~|to   the|~|dt   following|~|jj   conditions|~|nn   :|~|:   The|~|dt   above|~|in   copyright|~|nn   notice|~|nn   and|~|cc   this|~|dt   permission|~|nn   notice|~|nn   shall|~|md   be|~|vb   included|~|vb   in|~|in   all|~|md   copies|~|nn   or|~|cc   substantial|~|jj   portions|~|nn   of|~|in   the|~|dt   Software|~|np   .|~|.   THE|~|dt   SOFTWARE|~|nn   IS|~|vb   PROVIDED|~|vb   \"|~|\"   AS|~|rb   IS|~|vb   ,|~|,   WITHOUT|~|in   WARRANTY|~|nn   OF|~|in   ANY|~|dt   KIND|~|nn   ,|~|,   EXPRESS|~|vb   OR|~|cc   IMPLIED|~|vb   ,|~|,   INCLUDING|~|vb   BUT|~|cc   NOT|~|rb   LIMITED|~|jj   TO|~|to   THE|~|dt   WARRANTIES|~|nn   OF|~|in   MERCHANTABILITY|~|nn   ,|~|,   FITNESS|~|nn   FOR|~|in   A|~|dt   PARTICULAR|~|jj   PURPOSE|~|nn   AND|~|cc   NONINFRINGEMENT|~|nn   .|~|.   IN|~|in   NO|~|dt   EVENT|~|nn   SHALL|~|md   THE|~|dt   AUTHORS|~|nn   OR|~|cc   COPYRIGHT|~|nn   HOLDERS|~|nn   BE|~|vb   LIABLE|~|jj   FOR|~|in   ANY|~|dt   CLAIM|~|nn   ,|~|,   DAMAGES|~|nn   OR|~|cc   OTHER|~|jj   LIABILITY|~|nn   ,|~|,   WHETHER|~|in   IN|~|in   AN|~|dt   ACTION|~|nn   OF|~|in   CONTRACT|~|nn   ,|~|,   TORT|~|nn   OR|~|cc   OTHERWISE|~|rb   ,|~|,   ARISING|~|vb   FROM|~|in   ,|~|,   OUT|~|in   OF|~|in   OR|~|cc   IN|~|in   CONNECTION|~|nn   WITH|~|in   THE|~|dt   SOFTWARE|~|nn   OR|~|cc   THE|~|dt   USE|~|nn   OR|~|cc   OTHER|~|jj   DEALINGS|~|nn   IN|~|in   THE|~|dt   SOFTWARE|~|nn   .|~|.   "



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

	states, symbols, newDFA = mkNewDFA()
	print( newExtractNotice(states, symbols, newDFA, string) )



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

	DFA[(0, '(', '(')] = 1
	DFA[(1, '(', '(')] = 11
	DFA[(2, '(', '(')] = 11
	DFA[(3, '(', '(')] = 11
	DFA[(4, '(', '(')] = 11
	DFA[(5, '(', '(')] = 11
	DFA[(6, '(', '(')] = 11
	DFA[(7, '(', '(')] = 11
	DFA[(8, '(', '(')] = 11
	DFA[(9, '(', '(')] = 11
	DFA[(10, '(', '(')] = 11
	DFA[(11, '(', '(')] = 11
	DFA[(12, '(', '(')] = 11
	DFA[(13, '(', '(')] = 11

	DFA[(0, ')', ')')] = 11
	DFA[(1, ')', ')')] = 11
	DFA[(2, ')', ')')] = 3
	DFA[(3, ')', ')')] = 11
	DFA[(4, ')', ')')] = 11
	DFA[(5, ')', ')')] = 11
	DFA[(6, ')', ')')] = 11
	DFA[(7, ')', ')')] = 11
	DFA[(8, ')', ')')] = 11
	DFA[(9, ')', ')')] = 11
	DFA[(10, ')', ')')] = 11
	DFA[(11, ')', ')')] = 11
	DFA[(12, ')', ')')] = 3
	DFA[(13, ')', ')')] = 11

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
	DFA[(10, 'X', 'cd')] = 11
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
	DFA[(10, 'X', 'np')] = 11
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
	DFA[(6, 'X', 'in')] = 11
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

	DFA[(0, ',', ',')] = 11
	DFA[(1, ',', ',')] = 11
	DFA[(2, ',', ',')] = 11
	DFA[(3, ',', ',')] = 11
	DFA[(4, ',', ',')] = 5
	DFA[(5, ',', ',')] = 11
	DFA[(6, ',', ',')] = 5
	DFA[(7, ',', ',')] = 11
	DFA[(8, ',', ',')] = 11
	DFA[(9, ',', ',')] = 11
	DFA[(10, ',', ',')] = 11
	DFA[(11, ',', ',')] = 11
	DFA[(12, ',', ',')] = 11
	DFA[(13, ',', ',')] = 11

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
	DFA[(4, 'X', 'sym')] = 11
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
def newExtractNotice( states, symbols, DFA, string ):
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

		if currentWord.lower() in symbols and currentTag != '.' and currentTag != 'in':
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

	return extractedNotice




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









