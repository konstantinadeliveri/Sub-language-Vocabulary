from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import sys


file = 'file.txt'
lemmatizer = WordNetLemmatizer()

with open(file, 'r', encoding="utf8") as f:
    sys.stdout = open('output_5.txt', 'w', encoding="utf8")
    for line in f:
        token = word_tokenize(line)
        lemm_out = ' '.join([lemmatizer.lemmatize(i) for i in token])
        print(lemm_out)


sys.stdout.close()
