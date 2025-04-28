from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import sys


file = 'file.txt'
stemmer = PorterStemmer()

with open(file, 'r', encoding="utf8") as f:
    sys.stdout = open('output.txt', 'w', encoding="utf8")
    for line in f:
        token = word_tokenize(line)
        stem_out = ' '.join([stemmer.stem(i) for i in token])
        print(stem_out)


sys.stdout.close()
