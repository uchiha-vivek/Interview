import nltk
nltk.download('wordnet')

from nltk.stem.wordnet import WordNetLemmatizer

stemmer = WordNetLemmatizer()

text = """issues issue company companies"""
text = text.lower()  # Convert text to lowercase
for word in text.split():
    print(word, "--->", stemmer.lemmatize(word)) 
