import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import sys

file = 'file.txt'

with open(file, 'r', encoding="utf-8") as f, open('stopwords.txt', 'r', encoding="utf-8") as st:
    lst = st.readlines()
    stp_list = [i[:-1] for i in lst]
    sys.stdout = open('output_4.txt', 'w', encoding="utf8")
    for token in f:
        words = word_tokenize(token)
        removed_words = [word for word in words if not word in stp_list]
        text_sent = ' '.join(removed_words)
        print(text_sent)

sys.stdout.close()
