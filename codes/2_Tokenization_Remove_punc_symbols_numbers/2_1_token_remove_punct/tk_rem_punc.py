#libraries
import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import sys



file = 'file.txt'
punc = str.maketrans('','', string.punctuation)    # mapped punctuation

with open(file, 'r', encoding="utf-8") as f:
    sys.stdout = open('output_1.txt', 'w', encoding="utf-8")
    for line in f:
        data = sent_tokenize(line)                          #split in sentences
        for sentence in data:
            token = word_tokenize(sentence)                 #split in words in each sentence

            strip_token = sentence.translate(punc)          #remove all punctuation
            low_token = strip_token.lower()                 #lower case text

            print(low_token)

sys.stdout.close()
