import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import backend

class App (tk.Tk):
    def __init__(self):
        #Initialize Tk and set basic window
        super().__init__()

        # Set the style to 'xpnative'
        style = ttk.Style(self)
        style.theme_use('xpnative')
        style.configure('TButton', font=("Times New Roman", 12,'bold'), width=30, padding=10, background='azure4', relief="flat")
        style.map('TButton', foreground=[('hover', 'dark blue')], background=[('hover', 'DarkSlateGrey')])

        #Get screen width and height
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # make app the same size
        self.geometry('%dx%d'%(width,height))

        #Title of app
        self.title('Sublanguage Vocabulary')
        self.iconbitmap(os.path.join(os.path.dirname(__file__), 'Images', 'vocabulary.ico'))

        #Background color
        self.configure(background='AntiqueWhite3')

        #Create the main window widgets
        l1=tk.Label(self)
        l1.configure(text='Sublanguage Vocabulary', font=("Times New Roman", 20, 'bold'), foreground="black", background='AntiqueWhite3')
        l1.pack(side=TOP, pady=50)

        l2=tk.Label(self)
        l2.configure(text='Select Job', font=("Times New Roman", 20, 'bold'), foreground="black", background='AntiqueWhite3')
        l2.pack(side=TOP, pady=30)


        b1=ttk.Button (self, command=self.show_agriculture_frame)
        b1.configure(text='Agriculture')
        b1.pack(side=TOP, pady=15)

        b2=ttk.Button (self, command=self.show_cooking_frame)
        b2.configure(text='Cooking')
        b2.pack(side = TOP, pady=15)

        b3=ttk.Button (self, command=self.show_crafting_frame)
        b3.configure(text='Crafting')
        b3.pack(side=TOP, pady=15)

        b4=ttk.Button (self, command=self.show_construction_frame)
        b4.configure(text='Construction')
        b4.pack(side=TOP, pady=15)

        b5=ttk.Button (self, command=self.show_hospitality_frame)
        b5.configure(text='Hospitality')
        b5.pack(side=TOP, pady=15)

        l4=tk.Label(self)
        l4.configure(text='This GUI Application was created for a thesis at Ionian University.\nThis Application is a Sub-language Vocabulary Translator for the jobs of Agriculture, Cooking, Crafting, Construction and Hospitality.\n\n© Ionian University 2025\n\nAuthor - Konstantina Deliveri')
        l4.configure(font=("Times New Roman", 10), foreground='black', background='AntiqueWhite3')
        l4.place(relx=0.5, rely=0.85, anchor=CENTER)

        #Create a reference to the new window
        self.new_window = None

    def create_new_window(self, title, domain_name, color, csv_file):

        #Hide the main window
        self.withdraw()
        #Create the new window with message boxes and buttons
        self.new_window = tk.Toplevel()
        self.new_window.geometry('%dx%d'%(self.winfo_screenwidth(),self.winfo_screenheight()))#Size based on screen width and height
        self.new_window.config(background=color)

        self.new_window.title(title)
        self.new_window.iconbitmap(os.path.join(os.path.dirname(__file__), 'Images', 'vocabulary.ico'))

        # Set the style to 'xpnative'
        new_style=ttk.Style(self.new_window)
        new_style.theme_use('xpnative')
        new_style.configure('TButton', font=("Times New Roman", 12,'bold'), padding=5, background='azure4')
        new_style.map('TButton', foreground=[('hover', 'dark blue')], background=[('hover', 'DarkSlateGrey')])
        new_style.configure('TFrame', background=color)

        l5=tk.Label(self.new_window)
        l5.configure(text='Enter word:', font=("Times New Roman", 15, 'bold'), foreground='black', background=color)
        l5.place(x=150, y=200)

        entry=ttk.Entry(self.new_window)
        entry.configure(width=20)
        entry.place(x=280, y=201)

        l6=tk.Label(self.new_window)
        l6.configure(text='Choose Language:', font=("Times New Roman", 15, 'bold'), foreground="black", background=color)
        l6.place(x=950, y=200)

        lang = ttk.Combobox(self.new_window, justify = 'center', width =15, values=backend.get_languages(), state='readonly',font=('Times New Roman',12,'bold'))
        lang.place(x=1150, y=200)
        lang.bind("<<ComboboxSelected>>", lambda event: backend.update_language(lang))
        lang.current(21)

        #Add label
        l7 = tk.Label(self.new_window, text='This is the sub-language vocabulary of\n 'f"{domain_name}", font=("Times New Roman", 30), background=color)
        l7.pack(side=TOP, pady=10)

        frame = ttk.Frame(self.new_window)
        frame.pack(padx=50, pady=201)

        #Create a list of columns
        self.new_window.columns=['Word','Example','Pronunciation','Translated Word','Translated Example']
        self.new_window.original=self.new_window.columns[:] #Create a copy of columns as original
        tree=ttk.Treeview(frame, columns=self.new_window.columns, show='headings', height=12)
        #For setting TreeView width
        tree.column('Word', width=250)
        tree.column('Example', width=350, stretch=True)
        tree.column('Pronunciation', width=150)
        tree.column('Translated Word', width=250)
        tree.column('Translated Example', width=350, stretch=True)

        #Add scrollbar to the Treeviews
        scrollbar1 = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
        scrollbar2 = ttk.Scrollbar(frame, orient='horizontal', command=tree.xview)

        tree.configure(yscrollcommand=scrollbar1.set, xscrollcommand=scrollbar2.set)

        #Use the grid geometry manager to place the treeview and scrollbars inside the frame
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar1.grid(row=0, column=1, sticky="ns")
        scrollbar2.grid(row=1, column=0, sticky="ew")

        #Add a checkbox
        check_var=tk.IntVar()

        check=tk.Checkbutton(self.new_window, variable=check_var, command=lambda: self.checkbox_check(lang.get(), check_var, tree))
        check.configure(bg=color,font=('Times New Roman', 16), height=1, width=1)
        check.place(x=600, y=200)

        l8 = tk.Label(self.new_window, text='Translate Header:', font=('Times New Roman', 12, 'bold'), bg=color)
        l8.place(x=470, y=203)

        #Add buttons
        b6 = ttk.Button(self.new_window,  command=lambda: self.translate_query(tree, entry, lang.get(), csv_file))
        b6.configure(text="Translate", width=15)
        b6.place(x=710, y=200)

        #Bind the Enter Key to do what b6 button does
        self.new_window.bind('<Return>',lambda event: self.translate_query(tree, entry, lang.get(), csv_file))

        b7 = ttk.Button(self.new_window, command=lambda: self.clear_area(tree))
        b7.configure(text="Clear", width=8)
        b7.place(x=125, y=700)

        b8 = ttk.Button(self.new_window, command=lambda: self.download_file(tree,lang.get(),domain_name,check_var))
        b8.configure(text="Download", width=15)
        b8.place(x=250, y=700)

        b9 = ttk.Button(self.new_window, command=self.show_main_frame)
        b9.configure(text="Back", width=10)
        b9.place(x=1300, y=700)

        #Add style and borders
        new_style.configure('Treeview', font=('Helvetica', 12), borderwidth=2)
        new_style.configure('Treeview.Heading', font=('Helvetica', 14), borderwidth=2)



    #Get query and translate it using backend function, insert it in treeview
    def translate_query(self, tree, entry, lang, csv_file):
        query = entry.get().lower()
        if not query:
            messagebox.showerror("Error", "Please enter text to translate")
            return
        else:
            output = backend.translate_query(lang, query, csv_file)
            if output is not None:
                for col in output.keys():
                    tree.heading(col, text=col)
                #Insert data into Treeview
                tree.insert('', 'end', values=(output['Word'], output['Example'], output['Pronunciation'], output['Translated Word'], output['Translated Example']))

            entry.delete(0, END)#Delete entry when translated

    #Delete rows and columns from treeview
    def clear_area(self, tree):
        #Remove all columns from the tree
        for col in tree['columns']:
            tree.heading(col, text='')
        #Delete all items in the tree
        for item in tree.get_children():
            tree.delete(item)

    #Download csv file function
    def download_file(self,tree,lang,domain_name,var):
        if not tree.get_children():
            messagebox.showwarning('Warning','There are no words.\nTranslate words first and then Save file')
        else:
            output=backend.download_csv(tree, lang, domain_name, var)

    #Checkbox function
    def checkbox_check(self, lang, var, tree):
        #Check if there are items in tree if not return message else translate headings
        if not tree.get_children():
            messagebox.showinfo('Information', 'Headings automatically displayed when text area has words.\nTranslate a word and then check the Translate Headings checkbox.')
        else:
            #Check if checkbox checked and get translated columns from backend
            if var.get()==1:
                translated_columns = backend.translate_columns(lang, tree)
                for i, col in enumerate(translated_columns):
                    tree.heading(tree["columns"][i], text=col)
            else:
                #Restore original columns
                for i, col in enumerate(self.new_window.original):
                    tree.heading(tree["columns"][i], text=col)

    #Function that destroys top level window and shows main/basic window
    def show_main_frame(self):
        #Destroy the new window
        self.new_window.destroy()
        #Style back to original
        self.style=ttk.Style()
        self.style.theme_use('xpnative')
        self.style.configure('TButton', font=("Times New Roman", 12,'bold'), width=30, padding=10, background='azure4', relief="flat")
        self.style.map('TButton', foreground=[('hover', 'dark blue')], background=[('hover', 'DarkSlateGrey')])
        #Show the main window/stop minimising main window
        self.deiconify()

    #Windows for several domains
    def show_agriculture_frame(self):
        self.create_new_window("Agriculture Sub-Vocabulary" , 'Agriculture', color='lightgreen', csv_file=os.path.join(os.path.dirname(__file__), 'Files', 'agriculture_vocabulary_examples.csv'))

    def show_cooking_frame(self):
        self.create_new_window("Cooking Sub-Vocabulary", 'Cooking', color='salmon', csv_file=os.path.join(os.path.dirname(__file__), 'Files', 'cooking_vocabulary_examples.csv'))

    def show_crafting_frame(self):
        self.create_new_window("Crafting Sub-Vocabulary", 'Crafting', color='lightsteelblue', csv_file=os.path.join(os.path.dirname(__file__), 'Files', 'crafting_vocabulary_examples.csv'))

    def show_construction_frame(self):
        self.create_new_window("Construction Sub-Vocabulary", 'Construction', color='navajowhite', csv_file=os.path.join(os.path.dirname(__file__), 'Files', 'construction_vocabulary_examples.csv'))

    def show_hospitality_frame(self):
        self.create_new_window("Hospitality Sub-Vocabulary", 'Hospitality', color='lightskyblue', csv_file=os.path.join(os.path.dirname(__file__), 'Files', 'hospitality_vocabulary_examples.csv'))


if __name__ == '__main__':
    app = App()
    app.mainloop()
