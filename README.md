# Sub-language-Vocabulary
### Author - Konstantina Deliveri

## Description
Sublanguage Vocabulary Translator is a GUI Tkinter application developed in Python, created during the development process of "Machine Learning in Sublanguage Vocabulary" thesis for Ionian University.
The main window(basic window) contains five different buttons representing five different jobs.
After pressing one of the five main buttons the main window is hidden and a new window opens in its place that looks like a translator.
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
• Cooking
• Crafting
• Construction
• Hospitality

## Libraries
The libraries that were used:
• Tkinter
• Googletrans
• Pandas
• Eng_to_ipa

```python```
pip install googletrans==4.0.0rc1
pip install pandas
pip install eng-to-ipa

## OS
The application was built in Windows x64-bit, it runs only in Windows x64
