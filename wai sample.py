import nltk

name = input('your name: ')
print('Hi ', name, 'i\'m wAI, your personal assistant')
sentence = input("Input a message: ")
def tokens(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens
tokens = tokens(sentence)
print(tokens)

def  tagged(tokens):
    tagged = nltk.pos_tag(tokens)
    return tagged
    
tagged = tagged(tokens)
print(tagged[0:50])
print(len(tagged))