from nltk.corpus import brown
from nltk import Text
brown_words = brown.words(categories='humor')
brownText = Text(brown_words)
brownText.collocations()
brownText.count("car")
brownText.concordance("oil")
brownText.dispersion_plot(['car', 'document', 'funny', 'oil'])
brownText.similar('humor')

