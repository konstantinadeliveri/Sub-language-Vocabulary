# Sub-language-Vocabulary
### Author - Konstantina Deliveri

## Description
Sublanguage Vocabulary Translator is a GUI Tkinter application developed in Python, created during the development process of "Machine Learning in Sublanguage Vocabulary Learning" thesis for Ionian University.
The main window(basic window) contains five different buttons representing five different jobs.
After pressing one of the five main buttons, a new window opens in its place that looks like a translator.
The user enters a query and by clicking the Translate button the application searches in domain-specific vocabularies if that query exists.
If it exists it returns the query as well as an example sentence, pronunciation in english, translation and the translated example sentence of each query based on the language the user chose and places it in a TreeView area.
If the query doesn't exist the application returns a corresponding message.
By checking the checkbox the user translates also the columns that will be displayed on top of the TreeView area.
The user has also the capability to download a CSV file with all the generated queries that were entered, identified and translated by clicking the Download button.
The user may also clear the whole TreeView area by pressing the Clear Button.
Back button is used to return back to the main window that contains the different job areas.

## Domain-Specific Vocabularies
The domain-specific vocabularies that contain terms and example sentences of each term were created for five different jobs.
The vocabularies were created after proper web scrapping of wikipedia articles and machine learning methods of extracting Terminology.
Then, manually adding the example sentence of each term taken from the wikipedia articles.
• Agriculture
 Cooking
• Crafting
• Construction
• Hospitality

## Folders
• **Files** folder contains the original files after preprocessing and the focus words file with contextual features. <br>
• **Python_Scripts** folder contains the frontend.py and backend.py files as well as **Files** folder that has all the 5 different vocabularies. <br>
• **Terms and predictions** contains the files-results of terms after ML approach. <br>
• **codes** file contains all the crawling and preprocessing codes in Python as well as the symbols.txt (special symbols document) and stopwords.txt (custom stopwords list document). <br>
• **/dist** folder contains the Sub-Vocabulary Translator.exe standalone file.
```
.
├── Files
│   ├── DATA_AFTER_LEMM.txt
|   ├── DATA_AFTER_STEMM.txt
|   ├── DATA_BEFORE_LEMM_STEMM.txt
│   └── FOCUS_WORDS.txt
├── Python_Scripts
│   ├── Files
|   | ├── agriculture_vocabulary_examples.csv
|   | ├── construction_vocabulary_examples.csv
|   | ├── cooking_vocabulary_examples.csv
|   | ├── crafting_vocabulary_examples.csv
|   | └── hospitality_vocabulary_examples.csv
|   ├── Images
|   | ├── translation.ico
|   | └── vocabulary.ico
|   ├──backend.py
│   └── frontend.py
├── Terms and predictions
│   ├── STEMM_TERMS.csv
|   ├── TERMS.csv
│   └── explain_predictions_full_table.csv
├── codes
|  ├── 1_data_crawl
|  | └──crawler.py
|  ├── 2_Tokenization_Remove_punc_symbols_numbers
|  | ├── 2_1_token_remove_punct
|  | | └── tk_rem_punc.py
|  | ├── 2_2_Remove_symbols
|  | | ├── rem_symb.py
|  | | └── symbols.txt
|  | ├── 2_3_remove_digits
|  |   └── rem_num.py
|  ├── 3_Remove_Stopwords
|  | ├── rm_stp.py
|  | └── stopwords.txt
|  └── 4_Stemming_Lemmatization
|    ├── Lemmatization
|    | └── lemm.py
|    └── Stemming
|      └── stemm.py
├── dist
│   └── Sub-language Vocabulary Translator
│     ├──_internal
|     └── Sub-Vocabulary Translator.exe
├── LICENSE
└── README.md
```
## Libraries
The libraries that were used:
• Tkinter
• Googletrans
• Pandas
• Eng_to_ipa

```
pip install googletrans==4.0.0rc1
pip install pandas
pip install eng-to-ipa
```

## OS
The application was built in Windows x64-bit, it runs only in Windows x64
