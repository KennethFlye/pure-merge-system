import tkinter as tk
from Model.Article import Article

class MainMenu:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pure Merge")

    def create_row(self, parent, label_text_type, label_text, button1_text, button2_text, label2_text):
        frame = tk.Frame(parent)
        frame.pack(fill=tk.X)

        labelType = tk.Label(frame, text=label_text_type, width=15, anchor='w')
        labelType.pack(side=tk.LEFT)

        label = tk.Label(frame, text=label_text, wraplength=400, anchor='w')
        label.pack(side=tk.LEFT)

        button1 = tk.Button(frame, text=button1_text)
        button1.pack(side=tk.LEFT)

        button2 = tk.Button(frame, text=button2_text)
        button2.pack(side=tk.LEFT)

        label2 = tk.Label(frame, text=label2_text, wraplength=400, anchor='w')
        label2.pack(side=tk.LEFT)

    def setup(self, articleList):
        articleVariables = articleList[1].getListOfVariables()

        for i in range(14):
            counter = i*2
            article1 = articleList[counter]
            article2 = articleList[counter+1]
            variable = articleVariables[i]
            self.create_row(self.root, f'{variable}:',  f'{getattr(article1, variable) }', f'1', f'2', f'{getattr(article2, variable)}')

        self.root.mainloop()
