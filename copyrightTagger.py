"""
Define my transition matrix given the size
This makes a square matrix with the values initialized to 0
"""
def mkTransMatrix( size ):
	# error checking is for the weak and non-prototypes
	transMatrix = [[0 for x in range(size)] for x in range(size)]
	return transMatrix

"""
Few things here since I am assuming this is going to be read like a book
from the top to the bottom, mostly because this pretains to me and I know
to look for this. If the transition matrix had a global reference so that I
don't have to keep passing it arround that would be supper. Same goes for the
dicionary of the single word (tag, frequency) pair
"""


"""
The transition matrix is a little weird so I will explain what is happening.
Given the previous and the current POS tags the incrementTransMatrix function
will call another function "getTagIndex" what that does is return the index of
the 2d array that that tag is located see that function for more details.
Here is the important part:
the transition matrix is a 2d array and I am not sure how python stores its matricies
'lists' whatever, but what does matter is if I access the same way every time it will
be fine and the underarching structure does not matter.
The matrix works by the from this tag to the next tag idea. Written out on paper
the row is the from and the column is the to part. For instance from POS noun to POS
verb results in a likely hood of ___
likelyhood = transMatrix[noun][verb]
in more formal words:
transitionProbability = transMatrix[prev POS tag][current POS tag]

THIS IS JUST THE COUNTER AFTER ALL CORPUS ARE READ I WILL CALCULATE PROBABILITY
"""
def incrementTransMatrix( transMatrix, prevTag, currTag ):
	# error checking is for the weak and non-prototypes
	transMatrix[prevTag][currTag] += 1
	return transMatrix


"""
Given a POS string return the index that this tag refers to in the transMatrix
returns an integer
"""
def getTagIndex( POSTag ):
	# error checking is for the weak and non-prototypes
	# POSTag needs to be a string and this should be done with a switch statemnt
	# or some define or enum, or this is fine too.

	if POSTag == 'bos':
		return 0
	elif POSTag == '$':
		return 1
	elif POSTag == '"':
		return 2
	elif POSTag == '(':
		return 3
	elif POSTag == ')':
		return 4
	elif POSTag == ',':
		return 5
	elif POSTag == '--':
		return 6
	elif POSTag == '.':
		return 7
	elif POSTag == ':':
		return 8
	elif POSTag == 'cc':
		return 9
	elif POSTag == 'cd':
		return 10
	elif POSTag == 'dt':
		return 11
	elif POSTag == 'fw':
		return 12
	elif POSTag == 'jj':
		return 13
	elif POSTag == 'ls':
		return 14
	elif POSTag == 'nn':
		return 15
	elif POSTag == 'np':
		return 16
	elif POSTag == 'pos':
		return 17
	elif POSTag == 'pr':
		return 18
	elif POSTag == 'rb':
		return 19
	elif POSTag == 'sym':
		return 20
	elif POSTag == 'to':
		return 21
	elif POSTag == 'uh':
		return 22
	elif POSTag == 'vb':
		return 23
	elif POSTag == 'md':
		return 24
	elif POSTag == 'in':
		return 25
	else:
		print( "UNKNOWN TAG IS: ", POSTag)


"""
Given a POS Index return the string that this tag refers to in the transMatrix
returns an integer
"""
def getTagStr( POSIndex ):
	# error checking is for the weak and non-prototypes
	# POSIndex needs to be an int and this should be done with a switch statemnt
	# or some define or enum, or this is fine too.

	if POSIndex == 0:
		return 'bos'
	elif POSIndex == 1:
		return '$'
	elif POSIndex == 2:
		return '"'
	elif POSIndex == 3:
		return '('
	elif POSIndex == 4:
		return ')'
	elif POSIndex == 5:
		return ','
	elif POSIndex == 6:
		return '--'
	elif POSIndex == 7:
		return '.'
	elif POSIndex == 8:
		return ':'
	elif POSIndex == 9:
		return 'cc'
	elif POSIndex == 10:
		return 'cd'
	elif POSIndex == 11:
		return 'dt'
	elif POSIndex == 12:
		return 'fw'
	elif POSIndex == 13:
		return 'jj'
	elif POSIndex == 14:
		return 'ls'
	elif POSIndex == 15:
		return 'nn'
	elif POSIndex == 16:
		return 'np'
	elif POSIndex == 17:
		return 'pos'
	elif POSIndex == 18:
		return 'pr'
	elif POSIndex == 19:
		return 'rb'
	elif POSIndex == 20:
		return 'sym'
	elif POSIndex == 21:
		return 'to'
	elif POSIndex == 22:
		return 'uh'
	elif POSIndex == 23:
		return 'vb'
	elif POSIndex == 24:
		return 'md'
	elif POSIndex == 25:
		return 'in'
	else:
		print( "UNKNOWN TAG IS: ", POSIndex)


"""
gets the size required for the transition matrix
This is the number of tags I have, currently its 26 possible tags
"""
def getNumTags():
	return 26


"""
This is the object that the dictionary is made out of
The dictionary has a key that is a word and the value is an array of these tag
objects
"""
class TagFrequency():
	__slots__ = ('tag', 'frequency')

	def __init__(self, tag, frequency):
		self.tag = tag
		self.frequency = frequency


"""
This takes a dictionary, a given word and a tag
This will check to see if the dictionary has seen the words before
if it has it will check if the tag exists for that word, if exists it will
increment proppery
if not this will create a dictionary entry for the word and/or tag and
set their values to 1
"""
def incrementUnigramWord( dictionary, word, tag ):
	# maybe check to see if the dictionary is made, basically assume nothing
	# then noone can break your code, but again prototype so eeehh
	incremented = False
	if word in dictionary:
		for tagObject in dictionary[word]:  # need to check all the possible tag object a given word might have
			if tag == tagObject.tag:        # hey ive seen this tag before, so increment
				tagObject.frequency += 1    # NOT SURE IF THIS IS BY REFFERENCE OR VALUE COULD BE AN ISSUE
				incremented = True
		if incremented == False:            # I have not seen this tag so make a new one with seen value == 1
			newTagObject = TagFrequency( tag, 1 )
			dictionary[word].append( newTagObject )
	else:
		dictionary[word] = []               # initialize the word in the dictionary to be an array
		newTagObject = TagFrequency( tag, 1 )  # make a new tag object to append
		dictionary[word].append( newTagObject )

	return dictionary



"""
Before this function is called, the dictionary is just the summation
of all the occurances of word->(tag, # of occurances) with, this
isn't actually useful for calculating probability unless.... yea just don't do
that, it will be confusing for anyone. Anyway this converts the given
dictionary assuming it has not been done before into a probability dictionary
of the tag that a word will have.

Its methods like these where private methods are nice so you don't have
to worry about this being called more than once, but such is life.
"""
def convertDictionaryToProb( dictionary ):
	for keyWord in dictionary.keys():
		total = 0
		for tagObject in dictionary[keyWord]:   # sum all the occurances
			total += tagObject.frequency
		for tagObject in dictionary[keyWord]:
			# hey be careful about division because of int and float division and conversions
			tagObject.frequency = float( tagObject.frequency ) / float( total )  # divide by total occurances to get probability
	return dictionary                           # return the dictionary


"""
See above to infer what I want here....
This converts an transition matrix that is just the summation to its' probability
counter part. This also like the majority of the above comments might be nice to
be a private method and should be a real number between: (0,1)
"""
def convertTransMatrixToProb( transMatrix ):
	for row in range( getNumTags() ):        # implied 0
		total = 0
		for col in range( getNumTags() ):    # implied 0
			total += transMatrix[row][col]
		for col in range( getNumTags() ):    # implied 0
			# once again the above function "convertDict" looks real similar
			# however can't be done at the same time, and watch for integer and float changes
			# with respect to division and desired output
			# because unlike the dictionary 0s may be inculed so its: 0 / 0 which will crash
			# careful ^^^^
			if total != 0:
				transMatrix[row][col] = float( transMatrix[row][col] ) / float( total )
	return transMatrix


"""
THE ALGORITHM THE IMPORTANT PART OF THIS THING
HEY LOOK AT ME IM THE BRAIN IN THIS PROGRAM
the implementation of the Viterbi Algorithm to determine the part of speech
for any given sentence or section of code.
For any given tag to find the probability of that tag
P( tag|word ) = P( word|tag ) * max( P( tag transition )*Previous likelyhood, .... )

In a nice typed defined language sentence would be a string
or an array of char*
"""
def tagSentence( sentence, transMatrix, dictionary ):
	sentence = sentence.strip()
	sentence = sentence.split()
	sentLength = len( sentence ) + 1       # I need one for the base beginning of sentence part
	sentenceMatrix = [[0 for x in range(sentLength)] for x in range(getNumTags())]
	# above is the sentence array initialization

	# Initialize the first
	sentenceMatrix[getTagIndex('bos')][0] = 1.0     # the max probablity something can be
	for wordIndex in range( len( sentence ) ):
		for tagIndex in range( getNumTags() ):
			bestProb = 0
			for someTagIndex in range( getNumTags() ):
				# the probability of the previous * the transition from previoius to current
				possibleMaxProb = sentenceMatrix[someTagIndex][wordIndex] * transMatrix[someTagIndex][tagIndex]
				if possibleMaxProb > bestProb:
					bestProb = possibleMaxProb

			for tagObject in dictionary[sentence[wordIndex]]:
				if getTagStr( tagIndex ) == tagObject.tag:
					sentenceMatrix[tagIndex][wordIndex+1] = bestProb * tagObject.frequency
	# THE MATRIX IS CREATED.... I Think I am not in the best states of mind while I am writing this
	# I'll do some checks to see if this works I really don't want to work right now
	# The operations above are on the order of number of tags squared times the number of words in the sentence
	# less than N cubbed but not by much and very memory inefficient lots of null places or 0s in the matrix

	# Now go back through the matrix setting the POS for each word to be the max probability given the sentence matrix
	finalSentence = '|~|bos   '
	for wordIndex in range( len( sentence ) ):
		tag = ''
		tagProb = 0
		for tagIndex in range( getNumTags() ):
			if sentenceMatrix[tagIndex][wordIndex+1] > tagProb:
				tagProb = sentenceMatrix[tagIndex][wordIndex+1]
				tag = getTagStr( tagIndex )
		finalSentence = finalSentence + sentence[wordIndex] + '|~|' + tag + '   '
	print( finalSentence )



"""
Sanity check
Check is good
"""
def printUnigramDict( dictionary ):
	for word in dictionary.keys():
		for tagObject in dictionary[word]:
			print(word, tagObject.tag, tagObject.frequency)

"""
Sanity check number 2
"""
def printTransitionMatrix( transMatrix ):
	string = ''
	for row in range(0, getNumTags()):
		for col in range(0, getNumTags()):
			string = string + ' | ' + str(transMatrix[row][col])
		print( string )
		string = ''	

"""
READ IN THE FILE
"""
def readCorpus():

	# initialize the dictionary.... Easy
	dictionary = {}
	#initialize the transition matrix, requires the number of tags
	transMatrix = mkTransMatrix( getNumTags() )

	# I need some variables
	prevTag = 'bos'
	currTag = ''

	for line in open( "copyrightCorpus1.in" ):
		line = line.strip()
		line = line.split()
		for word in line:
			word = word.split( '|~|' )
			currTag = word[1]
			# add the current word to the unigram dictionary (single word probability)
			dictionary = incrementUnigramWord( dictionary, word[0], currTag )
			# add the current tag transition to the transition matrix
			transMatrix = incrementTransMatrix( transMatrix, getTagIndex(prevTag), getTagIndex(currTag) )
			prevTag = currTag     # set the prev tag to the current tag so I can keep track of transitions

			# so this is extremely naive because of the other things that the period could mean
			# all I am doing now is for every instance of a period I consider it to be a new sentence
			# floating point numbers, abbreviated buisnesses will cause problems
			if prevTag == '.':
				prevTag = 'bos'

	dictionary = convertDictionaryToProb( dictionary )
	transMatrix = convertTransMatrixToProb( transMatrix )

	tagSentence( 'Copyright ( c ) 2001 GNU', transMatrix, dictionary)



readCorpus()













