import tkinter as tk
from Model.Article import Article
from Controller.ArticleController import ArticleController
from GUI.MainMenuFunc import MenuFunc
import pandas as pd
import math  # TODO cannot do nan at this level


class MainMenu:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pure Merge")
        self.buttons_val = []
        self.labels = []

    def create_row(self, parent, label_text_type, label_text, label2_text):
        # frame = tk.Frame(parent)
        # frame.pack(fill=tk.X)

        current_row = len(parent.grid_slaves())

        # The article field types
        labelType = tk.Label(parent, text=label_text_type, name='rowType')  # name prevents inclusion unless stated
        labelType.grid(row=current_row, column=0, sticky='w')

        # First article field values
        label = tk.Label(parent, text=label_text, wraplength=1000)
        label.grid(row=current_row, column=1)
        self.labels.append(label)

        # Second article field values
        label2 = tk.Label(parent, text=label2_text, wraplength=1000)
        label2.grid(row=current_row, column=4, sticky='w')
        self.labels.append(label2)

        # First and second checkbutton
        # button1 = tk.Button(parent, text=button1_text)
        isPressed1 = tk.IntVar()
        button1 = tk.Checkbutton(parent, variable=isPressed1)
        button1.grid(row=current_row, column=2)
        if label2.cget('text') == 'nan':
            button1.select()

        self.buttons_val.append(isPressed1)

        # button2 = tk.Button(parent, text=button2_text)
        isPressed2 = tk.IntVar()
        button2 = tk.Checkbutton(parent, variable=isPressed2)
        button2.grid(row=current_row, column=3)
        if label.cget('text') == 'nan':
            button2.select()

        self.buttons_val.append(isPressed2)

    def setup(self, articleList):
        articleVariables = articleList[0].getListOfVariables()  # index number does not matter?
        print(articleVariables)

        for i in range(13):
            counter = i * 2
            article1 = articleList[counter]  # first field values
            article2 = articleList[counter + 1]  # second field values
            variable = articleVariables[i]  # field value types
            # print(variable)
            self.create_row(self.root, f'{variable}:', f'{getattr(article1, variable)}',
                            f'{getattr(article2, variable)}')

        self.create_merge_row(self.root)

        # self.root.wm_state('iconic')  # used to minimize on startup

        self.root.mainloop()

    def create_merge_row(self, parent):
        current_row = len(parent.grid_slaves())

        buttonAccept = tk.Button(parent, text='Accept Merge', bg='green', command=self.buttonAccept)
        buttonAccept.grid(row=current_row, column=0, sticky='w')

        buttonCancel = tk.Button(parent, text='Cancel Merge', bg='red', command=self.buttonCancel)
        buttonCancel.grid(row=current_row, column=1, sticky='w')

    def isIterable(self, item):
        try:
            iter(item)
            return True
        except TypeError:
            return False

    def buttonAccept(self):
        bools, strings = self.checkTicks()

        # for testing
        for item in bools:
            print(f"{item}: {self.isIterable(item)}")

        strings.pop(-3)  # hackerman
        print(str(len(bools)) + ' < bool | string > ' + str(len(strings)))  # always includes last labeltype object
        print(bools)
        print(strings)
        # TODO add check if columns lack ticks, fix formatting as mentioned line 91-92

        # itererer gennem hver string i strings, comparer hver index i bools og strings, if nummer = 1: incl string
        merged_article = [string for string, number in zip(strings, bools) if number == '1']

        print(merged_article)  # returns empty list because authors is a list maybe

    def buttonCancel(self):
        self.root.destroy()
        MenuFunc.cancel_merge(self)

    def checkTicks(self):
        bin_val_list = []
        text_list = []
        for widget in reversed(self.root.grid_slaves()):
            if isinstance(widget, tk.Checkbutton):
                variable = widget.cget('variable')
                value = self.root.getvar(variable)
                bin_val_list.append(str(value))  # stringify to make iterable
            elif isinstance(widget, tk.Label):
                # could add check to see if text = column name and then get rid of it
                text = widget.cget('text')
                text_list.append(text)

        return bin_val_list, text_list
