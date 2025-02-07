import nltk 

sentence = "Mbasu came home early enough"

tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged= nltk.pos_tag(tokens)
tagged[0:6]
print (tagged)
print (sentence)


