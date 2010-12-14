

from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import word_tokenize
from nltk import pos_tag


text = '''
Jack and Jill went up the hill to fetch a pail of water
'''
tokens = nltk.pos_tag(word_tokenize(text))

chunk = ChunkRule("<.*>+", "Chunk all the text")
chink = ChinkRule("<VBD|IN|\.>", "Leave verbs and prepositions out of this")
split = SplitRule("<DT><NN>", "<DT><NN>","Chunk on sequences of determiner+noun phrases")

chunker = RegexpChunkParser([chunk, chink, split],chunk_node='NP')
chunked = chunker.parse(tokens)
chunked.draw()




# ANOTHER WAY TO DO THIS USING THE "REGEX PARSER"
'''
import nltk
from nltk import pos_tag, word_tokenize
text = """
Jack and Jill went up the hill to fetch a pail of water. Jack fell down and broke his crown and jill came tumbling after.
"""
tagged_tokens = pos_tag(word_tokenize(text))

grammar = """
  NP:
    {<.*>+}         
    }<VBD|IN>+{      
  """
chunk = nltk.RegexpParser(grammar)
tree = chunk.parse(tagged_tokens)
tree.draw()
'''