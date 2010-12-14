from nltk.corpus import wordnet as wn

for holonym in wn.synsets('robot')[0].hypernym_paths()[0]:
	print hypernym.lemma_names