from nltk import word_tokenize,WordNetLemmatizer,NaiveBayesClassifier,classify,MaxentClassifier
from nltk.corpus import stopwords
import random
import os, glob,re



commonwords = stopwords.words('english')
wordlemmatizer = WordNetLemmatizer()


def email_features(sent):
	features = {}
	wordtokens = [wordlemmatizer.lemmatize(word.lower()) for word in word_tokenize(sent)]
	for word in wordtokens:
		if word not in commonwords:
			features[word] =  True
	return features


hamtexts  = []
spamtexts  = []

for infile in glob.glob( os.path.join('ham/', '*.txt')):
	text_file = open(infile, "r")
	hamtexts.append(text_file.read())
	text_file.close()

for infile in glob.glob( os.path.join('spam/', '*.txt') ):
	text_file = open(infile, "r")
	spamtexts.append(text_file.read())
	text_file.close()
	
	


mixedemails =	([(email,'spam') for email in spamtexts] + [(email,'ham') for email in hamtexts])

random.shuffle(mixedemails)
featuresets = [(email_features(n), g) for (n,g) in mixedemails]

size = int(len(featuresets) * 0.35)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = NaiveBayesClassifier.train(train_set)
#classifier = MaxentClassifier.train(train_set,'Powell',3)


print 'accuracy: ', classify.accuracy(classifier,test_set)
classifier.show_most_informative_features(30)
print 'labels:',classifier.labels()
while(True):
	featset = email_features(raw_input("Enter text to classify: "))
	print classifier.classify(featset)
