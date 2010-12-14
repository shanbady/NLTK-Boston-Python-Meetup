#!/usr/bin/env python
from nltk.corpus import wordnet as wn

Aword = 'language'
Bword = 'barrier'

synsetsA = wn.synsets(Aword)
synsetsB = wn.synsets(Bword)

groupA= [wn.synset(str(synset.name)) for synset in synsetsA]
groupB = [wn.synset(str(synset.name)) for synset in synsetsB]

similars = []

for sseta in groupA:
	for ssetb in groupB:
		path_similarity = sseta.path_similarity(ssetb)
		wup_similarity = sseta.wup_similarity(ssetb)
		
		if path_similarity is not None:
			similars.append({
				'path':path_similarity,
				'wup':wup_similarity,
				'wordA':sseta,
				'wordB':ssetb,
				'wordA_definition':sseta.definition,
				'wordB_definition':ssetb.definition
			})
			
similars = sorted(similars, key=lambda item: item['path'],reverse=True)

for item in similars:
	print item['wordA'],"\n",item['wordA_definition']
	print item['wordB'],"\n",item['wordB_definition']
	print 'Path similarity - ',item['path'],"\n"
