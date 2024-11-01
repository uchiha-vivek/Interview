# Removing stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

text = "I want to remove all the stopwords in a given sentence."
stop_words = set(stopwords.words('english'))
words_token = nltk.word_tokenize(text)
final_text = [i for i in words_token if i  not in stop_words ]
print(final_text)

###############################################
text = "I want to remove all the stopwords in a given sentence."
stop_words=['want','all','the','in','a']
words_token = nltk.word_tokenize(text)
final_text = [i for i in words_token if i not in stop_words ]
print(final_text)