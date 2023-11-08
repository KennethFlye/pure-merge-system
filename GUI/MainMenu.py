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
        self.buttons = []
        self.labels = []

    def create_row(self, parent, label_text_type, label_text, label2_text):
        # frame = tk.Frame(parent)
        # frame.pack(fill=tk.X)

        current_row = len(parent.grid_slaves())

        # TODO if labeltexttype and type of labeltext not equal, highlight the other article
        # or if labeltext empty highlight other article
        # somehting along the lines of:
        # is_label_nan = label_text is None  # or math.isnan(label_text)
        # if is_label2_nan:
        #     isPressed1 = tk.BooleanVar(value=True)

        # The article field types
        labelType = tk.Label(parent, text=label_text_type)
        labelType.grid(row=current_row, column=0, sticky='w')

        # First article field values
        label = tk.Label(parent, text=label_text, wraplength=1000)
        label.grid(row=current_row, column=1)
        self.labels.append(label)  # TODO move to end of code to keep label1 and 2 together

        # First and second checkbutton
        # button1 = tk.Button(parent, text=button1_text)
        isPressed1 = tk.IntVar()
        button1 = tk.Checkbutton(parent, variable=isPressed1)
        button1.grid(row=current_row, column=2)
        button1.select()
        self.buttons.append(isPressed1)

        # button2 = tk.Button(parent, text=button2_text)
        isPressed2 = tk.IntVar()
        button2 = tk.Checkbutton(parent, variable=isPressed2)
        button2.grid(row=current_row, column=3)
        self.buttons.append(isPressed2)  # TODO selection methods does not seem to work when called before the mainloop()

        # Second article field values
        label2 = tk.Label(parent, text=label2_text, wraplength=1000)
        label2.grid(row=current_row, column=4, sticky='w')
        self.labels.append(label2)

    def setup(self, articleList):
        articleVariables = articleList[0].getListOfVariables()  # index number does not matter?
        print(articleVariables)

        for i in range(14):
            counter = i * 2
            article1 = articleList[counter]  # first field values
            article2 = articleList[counter + 1]  # second field values
            variable = articleVariables[i]  # field value types
            # print(variable)
            self.create_row(self.root, f'{variable}:', f'{getattr(article1, variable)}',
                            f'{getattr(article2, variable)}')

        self.create_merge_row(self.root)

        self.checkTicks(self.root)

        self.root.wm_state('iconic')  # used to minimize on startup

        self.root.mainloop()

    def create_merge_row(self, parent):
        current_row = len(parent.grid_slaves())

        buttonAccept = tk.Button(parent, text='Accept Merge', bg='green', command=self.buttonAccept)
        buttonAccept.grid(row=current_row, column=0, sticky='w')

        buttonCancel = tk.Button(parent, text='Cancel Merge', bg='red', command=self.buttonCancel)
        buttonCancel.grid(row=current_row, column=1, sticky='w')

    def buttonAccept(self):
        MenuFunc.accept_merge(self)

    def buttonCancel(self):
        self.root.destroy()
        MenuFunc.cancel_merge(self)

    def checkTicks(self, parent):
        for widget in reversed(parent.grid_slaves()):
            if isinstance(widget, tk.Label):
                text = widget.cget('text')  # TODO add param to label_text_type to sort out
                print(text)
            elif isinstance(widget, tk.Checkbutton):
                # btnvar = widget.cget('variable')
                # print(btnvar + 'has val' + str(btnval))
                variable = widget.cget('variable')
                bool_var = self.root.getvar(variable)
                # value = bool_var.get()
                print(f"Checkbutton Variable: {bool_var}, Value: {'na'}")
            else:
                print('no further relevant widgets')

# class MainMenu:
#     # Existing code...
#
#     def check_widgets(self):
#         current_row_widgets = self.root.grid_slaves()
#         for widget in current_row_widgets:
#             if isinstance(widget, tk.Label):
#                 label_text = widget.cget('text')
#                 print(f"Label Text: {label_text}")
#             elif isinstance(widget, tk.Checkbutton):
#                 variable = widget.cget('variable')
#                 print(f"Checkbutton Variable: {variable}")
#
#     # Other methods...
