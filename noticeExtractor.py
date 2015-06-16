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
	# if I the tag is nothing above return to the end state
	else:
		return 8

"""
Given a specific option [1,2] will create the DFA that corresponds
to one of the two valid DFAs to validate copyright notices.

It would make it clearer if I called the function above but that
is processing power.
See the corresponding numbers above to understand the transition matrix
"""
def createDFA( option ):
	if option == 1:
		copyrightTrans = [1, 4, 5]
		leftParen = [2]
		cTrans = [3]
		rightParen = [5]
		symTrans = [5]
		cdTrans = [6, 7]
		commaTrans = [5, 7]
		npTrans = [6, 7, 8]
		endTrans = [8]

	elif option == 2:
		copyrightTrans = [1, 4, 7]
		leftParen = [2]
		cTrans = [3]
		rightParen = [7]
		symTrans = [7]
		cdTrans = [6, 8]
		commaTrans = [5]
		npTrans = [7, 6, 5]
		endTrans = [8]

	else:
		return None

	DFA = [copyrightTrans, leftParen, cTrans, rightParen, symTrans, cdTrans,
			commaTrans, npTrans, endTrans ]
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
			potentialNotice = potentialNotice + currentWord + ' '
			currentState = getTransIndex( currentTag )
			currentIndex += 1

		elif getTransIndex( currentWord ) in DFA[ currentState ] and currentState != 8:
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

	string = "Attempt|~|nn   to|~|to   guess|~|vb   a|~|dt   canonical|~|jj   system|~|nn   name|~|nn   .|~|.   Copyright|~|nn   (|~|(   C|~|nn   )|~|)   1992|~|cd   ,|~|,   1993|~|cd   ,|~|,   1994|~|cd   ,|~|,   1995|~|cd   ,|~|,   1996|~|cd   ,|~|,   1997|~|cd   ,|~|,   1998|~|cd   ,|~|,   1999|~|cd   ,|~|,   2000|~|cd   ,|~|,   2001|~|cd   ,|~|,   2002|~|cd   ,|~|,   2003|~|cd   ,|~|,   2004|~|cd   ,|~|,   2005|~|cd   ,|~|,   2006|~|cd   ,|~|,   2007|~|cd   ,|~|,   2008|~|cd   ,|~|,   2009|~|cd   ,|~|,   2010|~|cd   Free|~|np   Software|~|np   Foundation|~|np   ,|~|,   Inc|~|np   .|~|."

	print( extractNotice(DFA1, string) )
	print( extractNotice(DFA2, string) )


main()












