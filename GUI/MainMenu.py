import tkinter as tk
from Model.Article import Article

class MainMenu:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pure Merge")

    def create_row(self, parent, label_text_type, label_text, label2_text):
        #frame = tk.Frame(parent)
        #frame.pack(fill=tk.X)

        current_row = len(parent.grid_slaves())

        labelType = tk.Label(parent, text=label_text_type)
        labelType.grid(row=current_row, column=0, sticky='w')

        label = tk.Label(parent, text=label_text, wraplength=1000)
        label.grid(row=current_row, column=1)

        #button1 = tk.Button(parent, text=button1_text)
        isPressed1 = tk.BooleanVar()
        button1 = tk.Checkbutton(parent, variable=isPressed1)
        button1.grid(row=current_row, column=2)

        #button2 = tk.Button(parent, text=button2_text)
        isPressed2 = tk.BooleanVar()
        button2 = tk.Checkbutton(parent, variable=isPressed2)
        button2.grid(row=current_row, column=3)

        label2 = tk.Label(parent, text=label2_text, wraplength=1000)
        label2.grid(row=current_row, column=4, sticky='w')

    def setup(self, articleList):
        articleVariables = articleList[1].getListOfVariables()

        for i in range(14):
            counter = i*2
            article1 = articleList[counter]
            article2 = articleList[counter+1]
            variable = articleVariables[i]
            self.create_row(self.root, f'{variable}:',  f'{getattr(article1, variable) }', f'{getattr(article2, variable)}')

        self.create_merge_row(self.root)

        self.root.mainloop()

    def create_merge_row(self, parent):
        current_row = len(parent.grid_slaves())

        buttonAccept = tk.Button(parent, text='Accept Merge', bg='green', command=self.buttonAccept)
        buttonAccept.grid(row=current_row, column=0, sticky='w')

        buttonCancel = tk.Button(parent, text='Cancel Merge', bg='red', command=self.buttonCancel)
        buttonCancel.grid(row=current_row, column=1, sticky='w')

    def buttonAccept(self):
        pass

    def buttonCancel(self):
        pass