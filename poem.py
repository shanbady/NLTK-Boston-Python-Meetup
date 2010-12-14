from nltk_contrib.readability.textanalyzer import syllables_en
from nltk.corpus import cmudict,wordnet as wn
import nltk
import re


# requires the installation of the nltk_contrib package which is available at the google code project page
textchunk = '''
	One of the very difficult parts of the decision I made on the 
	financial crisis was to use hardworking people's money to
	help prevent there to be a crisis.
	
	I want to share with you an interesting program for two reasons, one, 
	it's interesting, and two, my wife thought of it or 
	has actually been involved with it; she didn't think of it. 
	But she thought of it for this speech.

	I'm telling you there's an enemy that would like to attack America, Americans, again. 
	There just is. 
	That's the reality of the world. 
	And I wish him all the very best.
	
	This is my maiden voyage.
	My first speech since I was the president of the United States and I couldn't think of a better 
	place to give it than Calgary, Canada.
	'''
	
textchunk += '''
	They want to deliver vast amounts of information over the Internet.
	And again, the Internet is not something that you just dump something on. 
	It's not a big truck. It's a series of tubes. And if you don't understand, 
	those tubes can be filled and if they are filled, when you put your message in, 
	it gets in line and it's going to be delayed by anyone that puts into that tube 
	enormous amounts of material, enormous amounts of material
	'''
	
poem = ''
wordmap = [] # a list that will contain a tuple (word,syllable_count)
words = nltk.word_tokenize(textchunk)
for iter,word in enumerate(words):	
	word += " "
	syls = syllables_en.count(word)
	wordmap.append((word,syls))
	
	
	
def findSyllableWord(word,syllableSize): 
	synsets = wn.synsets(word)
	for syns in synsets:
		name = syns.name
		lemmas =  syns.lemma_names
		for wordstring in lemmas:
			if(syllables_en.count(wordstring) == syllableSize and wordstring != word):
				return {'word':word,'syllable':syllableSize}
	return	{'word':word,'syllable':syllables_en.count(word)}


lineNo = 1
charNo = 0
tally = 0
for syllabicword in wordmap:
	s = syllabicword[1]
	wordtoAdd = syllabicword[0]
	if lineNo == 1:
		if tally < 5:
			if tally + int(s) > 5 and wordtoAdd.isalpha():
				num = 5 - tally
				similarterm = findSyllableWord(wordtoAdd,num)
				wordtoAdd = similarterm['word']
				s = similarterm['syllable']
			tally += int(s)
			poem += wordtoAdd
		else:
			poem += " ---"+str(tally)+"\n"
			if wordtoAdd.isalpha():
				poem += wordtoAdd
			tally = s
			lineNo = 2
	elif lineNo == 2:
		if tally < 7:
			if tally + int(s) > 7 and wordtoAdd.isalpha():
				num = 7 - tally
				similarterm = findSyllableWord(wordtoAdd,num)
				wordtoAdd = similarterm['word']
				s = similarterm['syllable']
			tally += int(s)
			poem += wordtoAdd
		else:
			poem += " ---"+str(tally)+"\n"
			if wordtoAdd.isalpha():
				poem += wordtoAdd
			tally = s
			lineNo = 3
	elif lineNo == 3:
		if tally < 5:
			if tally + int(s) > 5 and wordtoAdd.isalpha():
				num = 5 - tally
				similarterm = findSyllableWord(wordtoAdd,num)
				wordtoAdd = similarterm['word']
				s = similarterm['syllable']
			tally += int(s)
			poem += wordtoAdd
		else:
			poem += " ---"+str(tally)+"\n\n"
			if wordtoAdd.isalpha():
				poem += wordtoAdd
			tally = s
			lineNo = 1
	charNo+=1


print poem