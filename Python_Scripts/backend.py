import pandas as pd
from tkinter.filedialog import asksaveasfilename as fd
from tkinter import messagebox
from googletrans import LANGUAGES, Translator
import eng_to_ipa as ipa


# Get languages by name
def get_languages():
        return list(LANGUAGES.values())

#update language
def update_language(lang):
    lang = lang.get()
    for code, name in LANGUAGES.items():
        if name == lang:
            lang_code = code
            break


def translate_query(lang, query, csv):
    try:
        #Read csv file
        df=pd.read_csv(csv)

        # Check if the entry is present in the 'Word' column
        row = df.loc[df['Word'] == query]
        # Get 'Example' and 'Word' columns from row
        example = row['Example'].values[0]
        word = row['Word'].values[0]

        translator = Translator()
        pronunciation = ipa.convert(word)
        translated_word = translator.translate(word, dest=lang).text
        translated_example = translator.translate(example, dest=lang).text
        output={'Word': word, 'Example': example, 'Pronunciation': pronunciation, 'Translated Word': translated_word, 'Translated Example': translated_example}

        return output

    except IndexError:
        messagebox.showinfo("Information", "Word not found in dictionary\nTry another word.")

        return None

def translate_columns(lang, tree):
    # Get column headings
    columns = [tree.heading(column)["text"] for column in tree['columns']]
    #Call Translator
    translator = Translator()
    #Create an empty list
    translated_columns = []
    for col in columns:
        translation = translator.translate(col, dest=lang).text
        translated_columns.append(translation)
    return translated_columns

def download_csv(tree,lang,name,var):
    # Get the data from the treeview
    data = []
    # Get columns
    columns=[]
    #check if checkbox is checked
    if var.get() == 1:
        col = translate_columns(lang, tree)
        columns.append(col)
    else:
        for col in tree['columns']:
            columns.append(tree.heading(col)['text'])
    data.append(columns)# append data with column list first
    #Loop each row in TreeView
    for row in tree.get_children():
        rows=[]# create an empty list of rows
        #loop over each cell in the current row
        for i in tree.item(row)['values']:
            rows.append(i) #for each cell retrieve values
        data.append(rows) #append the data list with the row list

    df = pd.DataFrame(data[1:], columns=data[0]) #costruct dataframe with columns in first row and the rest of the list is rows data

    
    #save dataframe to csv file
    filename=fd(defaultextension='.csv', filetypes=[('CSV files', '*.csv')], initialfile=f"{name}_full_csv_file_{lang}.csv")
    if filename:
        df.to_csv(filename, index=False)
