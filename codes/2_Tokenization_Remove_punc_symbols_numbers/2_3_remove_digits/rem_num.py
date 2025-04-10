#import necessary libraries
import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import sys


file = 'file.txt'
num = str.maketrans('','',string.digits)        #map digits

with open(file, 'r', encoding="utf8") as f:     #read file
    sys.stdout = open('output_3.txt', 'w', encoding="utf8")
    for line in f:                               #split in sentences
        data = sent_tokenize(line)
        for sentence in data:                   #split in words in each sentence
            token = word_tokenize(sentence)
            strip_token = sentence.translate(num)    #remove all digits
            print(strip_token)
sys.stdout.close()
