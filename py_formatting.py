text = "morning"
def first_upper(text):
    if text:
        return text[0].upper() + text[1:]
    else:
        return text
text = first_upper(text)
print(text)

word = "MAMBO"
def all_uppercase(word):
    return word.isupper()
word= all_uppercase(word)
print(word)

white = "     poa"
def whitespace(white):
    return white.lstrip()
white = whitespace(white)
print(white)