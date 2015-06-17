"""
Given a tag string this will return the integer value
corresponding to its place in the DFA transition table
takes in a string that is a tag or a key word
returns an integer
"""
def getTransIndex( tag ):

	if tag.lower() == 'copyright':
		return 0
	elif tag == '(':
		return 1
	elif tag.lower() == 'c':
		return 2
	elif tag == ')':
		return 3
	elif tag == 'sym':
		return 4
	elif tag == 'cd':
		return 5
	elif tag == ',':
		return 6
	elif tag == 'np':
		return 7
	elif tag == '--':
		return 9
	# if I the tag is nothing above return to the end state
	else:
		return 8

"""
Given a specific option [1,2] will create the DFA that corresponds
to one of the two valid DFAs to validate copyright notices.

It would make it clearer if I called the function above but that
is processing power.
See the corresponding numbers above to understand the transition matrix

CURRENTLY the DFA is very strict any deviation will result in the dropping
of the possible tag. This can be an issue with foreign words. My suggestion would
be to allow a one tag deviation directly back to where it 'should' be.... The
issue with this is the complexity of that problem would be implementing spellcheck.


NEED A BETTER DFA IMPLEMENTATION.....
Currently I state allowed transitions then make those, it might be better to state
not allowed transitions then go to failure if that occurs. Or this might be the
happy medium of the two is to implement a guarenteed failure transitions
but allow others. For instance if I see this tag while in this state go to failure.


Need to allow:
copyright 1990 by the organization
copyright 2000 Steve and the Exablox co.
"""
def createDFA( option ):
	if option == 1:
		copyrightTrans = [1, 4, 5]
		leftParen = [2]
		cTrans = [3]
		rightParen = [5]
		symTrans = [5]
		cdTrans = [6, 7, 9]
		commaTrans = [5, 7]
		npTrans = [6, 7, 8]
		endTrans = [8]
		dashTrans = [9, 5]

	elif option == 2:
		copyrightTrans = [1, 4, 7]
		leftParen = [2]
		cTrans = [3]
		rightParen = [7]
		symTrans = [7]
		cdTrans = [6, 8, 9]
		commaTrans = [5]
		npTrans = [7, 6, 5]
		endTrans = [8]
		dashTrans = [9, 5]

	else:
		return None

	DFA = [copyrightTrans, leftParen, cTrans, rightParen, symTrans, cdTrans,
			commaTrans, npTrans, endTrans, dashTrans ]
	return DFA


"""
Given a DFA and a tagged string with the delimeter |~| this will
extract the copyright notice if it exists in the given string. returns the
string of a copyright notice(s) or None.
"""
def extractNotice( DFA, string ):
	extractedNotice = ''
	# assuming this is a valid string that this function can take
	string = string.strip()
	string = string.split()
	# string should now be a list of word|~|tag strings.

	currentIndex = 0
	lastIndex = len( string ) # this makes the while statement a lookup rather than a compute each time
	currentState = 8          # initialize my state machine
	potentialNotice = ''      # initalize my notice outside of the loop
	while currentIndex < lastIndex:

		temp = string[currentIndex]
		temp = temp.split('|~|')
		currentWord = temp[0]
		currentTag = temp[1]
		# read in the values
		# Perform state machine tests and transitions
		if currentState == 8 and potentialNotice != '': # if in the accept state
				extractedNotice = extractedNotice + potentialNotice + '\n'
				potentialNotice = ''

		if currentWord.lower() == 'copyright':
			if potentialNotice != '': # if there is something in the notice it is probably good
				extractedNotice = extractedNotice + potentialNotice + '\n'

			currentState = getTransIndex( currentWord )
			potentialNotice = currentWord + ' '
			currentIndex += 1

		elif getTransIndex( currentTag ) in DFA[ currentState ] and currentState != 8:
			if getTransIndex( currentTag ) != 8:
				potentialNotice = potentialNotice + currentWord + ' '
			currentState = getTransIndex( currentTag )
			currentIndex += 1

		elif getTransIndex( currentWord ) in DFA[ currentState ] and currentState != 8:
			if getTransIndex( currentTag ) != 8:
				potentialNotice = potentialNotice + currentWord + ' '
			potentialNotice = potentialNotice + currentWord + ' '
			currentState = getTransIndex( currentWord )
			currentIndex += 1

		else:
			potentialNotice = ''
			currentState = 8
			currentIndex += 1

	if currentState == 8 and potentialNotice != '': # if in the accept state
				extractedNotice = extractedNotice + potentialNotice + '\n'
				potentialNotice = ''

	return extractedNotice


def main():
	DFA1 = createDFA( 1 )
	DFA2 = createDFA( 2 )

	string = "Copyright|~|nn   (|~|(   C|~|nn   )|~|)   2003|~|cd   Free|~|np   Software|~|np   Foundation|~|np   ,|~|,   Inc|~|np   .|~|.   This|~|dt   configure|~|jj   script|~|nn   is|~|vb   free|~|jj   software|~|nn   ;|~|:   the|~|dt   Free|~|np   Software|~|np   Foundation|~|np   gives|~|vb   unlimited|~|jj   permission|~|nn   to|~|to   copy|~|vb   ,|~|,   distribute|~|vb   and|~|cc   modify|~|vb   it|~|pr   .|~|.   -|~|--   M4sh|~|np   Initialization|~|nn   .|~|.   -|~|--   $|~|sym   echo|~|vb   $|~|sym   cfgfile|~|fw   \"|~|\"   ||~|sym   sed|~|fw   '|~|\"   s|~|nn   `|~|\"   -|~|--   Provide|~|vb   generalized|~|fw   library|~|nn   -|~|--   building|~|fw   support|~|nn   services|~|nn   .|~|.   Generated|~|vb   automatically|~|rb   by|~|in   $|~|sym   PROGRAM|~|nn   (|~|(   GNU|~|np   $|~|sym   PACKAGE|~|nn   $|~|sym   VERSION|~|nn   $|~|sym   TIMESTAMP|~|np   )|~|)   NOTE|~|nn   :|~|:   Changes|~|vb   made|~|vb   to|~|to   this|~|dt   file|~|nn   will|~|md   be|~|vb   lost|~|fw   :|~|:   look|~|fw   at|~|in   ltmain|~|fw   .|~|.   sh|~|fw   .|~|.   Copyright|~|nn   (|~|(   C|~|nn   )|~|)   1996|~|cd   ,|~|,   1997|~|cd   ,|~|,   1998|~|cd   ,|~|,   1999|~|cd   ,|~|,   2000|~|cd   ,|~|,   2001|~|cd   Free|~|np   Software|~|np   Foundation|~|np   ,|~|,   Inc|~|np   .|~|.   This|~|dt   file|~|nn   is|~|vb   part|~|dt   of|~|in   GNU|~|np   Libtool|~|np   :|~|:   Originally|~|rb   by|~|in   Gordon|~|np   Matzigkeit|~|np   <|~|(   gord|~|fw   @|~|sym   gnu|~|np   .|~|.   ai|~|fw   .|~|.   mit|~|np   .|~|.   edu|~|nn   ,|~|,   1996|~|cd   This|~|dt   program|~|nn   is|~|vb   free|~|jj   software|~|nn   ;|~|:   you|~|pr   can|~|md   redistribute|~|vb   it|~|pr   and|~|cc   /|~|sym   or|~|cc   modify|~|vb   it|~|pr   under|~|in   the|~|dt   terms|~|nn   of|~|in   the|~|dt   GNU|~|np   General|~|np   Public|~|np   License|~|np   as|~|in   published|~|vb   by|~|in   the|~|dt   Free|~|np   Software|~|np   Foundation|~|np   ;|~|:   either|~|cc   version|~|nn   2|~|cd   of|~|in   the|~|dt   License|~|np   ,|~|,   or|~|cc   (|~|(   at|~|in   your|~|pr   option|~|nn   )|~|)   any|~|dt   later|~|jj   version|~|nn   .|~|.   This|~|dt   program|~|nn   is|~|vb   distributed|~|vb   in|~|in   the|~|dt   hope|~|nn  "


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


	print( extractNotice(DFA1, string) )
	print( extractNotice(DFA2, string) )


main()












