from nltk import ne_chunk,pos_tag
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
'''
	import nltk
	nltk.download('words')
	nltk.download('punkt')
	nltk.download('maxent_treebank_pos_tagger')
	nltk.download('maxent_ne_chunker')
'''


TreeBankTokenizer = TreebankWordTokenizer()
PunktTokenizer = PunktSentenceTokenizer()
text = '''
The Boston Celtics are a National Basketball Association (NBA) team based in Boston, MA. They play in the Atlantic Division
 of the Eastern Conference. Founded in 1946, the team is currently owned by 
 Boston Basketball Partners LLC. The Celtics play their home games at the TD Garden,
 which they share with the Boston Blazers (NLL), and the Boston Bruins of the NHL.
 
 The Celtics have dominated the league during the late 50's and through the mid 80's, 
 with the help of many Hall of Famers which include Bill Russell, Bob Cousy, John Havlicek, 
 Larry Bird and legendary Celtics coach Red Auerbach, 
 combined for a 795 - 397 record that helped the Celtics win 16 Championships.
'''

sentences = PunktTokenizer.tokenize(text)
tokens = [TreeBankTokenizer.tokenize(sentence) for sentence in sentences]
tagged = [pos_tag(token) for token in tokens]
chunked = [ne_chunk(taggedToken) for taggedToken in tagged]

chunked[0].draw()
chunked[-1].draw()
chunked[-3].draw()

print chunked



