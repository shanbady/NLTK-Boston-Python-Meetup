import nltk


rawtext = '''
The Boston Celtics are a National Basketball Association (NBA) team based in Boston, MA. They play in the Atlantic Division
 of the Eastern Conference. Founded in 1946, the team is currently owned by 
 Boston Basketball Partners LLC. The Celtics play their home games at the TD Garden,
 which they share with the Boston Blazers (NLL), and the Boston Bruins of the NHL.
 
 The Celtics have dominated the league during the late 50's and through the mid 80's, 
 with the help of many Hall of Famers which include Bill Russell, Bob Cousy, John Havlicek, 
 Larry Bird and legendary Celtics coach Red Auerbach, 
 combined for a 795 - 397 record that helped the Celtics win 16 Championships.
'''
rawtext = rawtext.lower()



text = nltk.Text(nltk.word_tokenize(rawtext))


# Frequency of any given word
print '-- Counting'
print text.count("boston")

# concordance
print '-- Concordance'
print text.concordance("basketball")

# similarity
print '-- similarity'
print text.similar("game")


print '-- contexts'
text.common_contexts(["celtics" ,"win","boston","basketball"])

# lexical dispersion
text.dispersion_plot(["celtics", "boston", "basketball"])
