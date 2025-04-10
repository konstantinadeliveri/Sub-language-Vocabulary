import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import sys

file = 'file.txt'


# Open the input text file and the file containing symbols to be removed
with open(file, 'r', encoding="utf-8") as f, open('symbols.txt', 'r', encoding="utf-8") as sm:
    # Read all lines (symbols) from the file and remove newline characters
    lst = sm.readlines()
    stp_list = [i[:-1] for i in lst] # Cleaned list of unwanted symbols or tokens

    # Redirect the output to a new text file
    sys.stdout = open('output.txt', 'w', encoding="utf-8")

    # Iterate through each line in the input file
    for token in f:
        # Tokenize the line into individual words
        words = word_tokenize(token)
         # Remove any word that exists in the list of symbols
        removed_words = [word for word in words if not word in stp_list]
        # Join the cleaned words back into a string
        text_sent = ' '.join(removed_words)
        # Write the cleaned sentence to the output file
        print(text_sent)

sys.stdout.close()
