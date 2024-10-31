
text = "My name is  vivek's"

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

no_punctuation =""
for char in text:
    if char not in punctuations:
        no_punctuation = no_punctuation+char
print(no_punctuation)


## using NLTK tokenizer ##

from nltk.tokenize import RegexpTokenizer
text = "My name is  vivek's"
tokenizer = RegexpTokenizer(r'\w+')
final_text = tokenizer.tokenize(text)
print(final_text)


text = "My name is  vivek's"
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punc = text
for char in text :
    if char in punctuations:
        no_punc = no_punc.replace(char,"")
print(no_punc)