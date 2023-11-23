import tkinter as tk
from Model.Article import Article
from Controller.ArticleController import ArticleController


class MainMenu:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pure Merge")
        self.buttons_val = []
        self.labels = []
        self.article_controller = ArticleController()
        self.save_status_msg = tk.StringVar()

    def create_row(self, parent, label_text_type, label_text, label2_text):
        # frame = tk.Frame(parent)
        # frame.pack(fill=tk.X)

        current_row = len(parent.grid_slaves())

        # The article field types
        labelType = tk.Label(parent, text=label_text_type)  # name prevents inclusion unless stated
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

    def setup(self, articleList, starting_index):
        articleVariables = articleList[0].getListOfVariables()  # index number does not matter?
        print(articleVariables)

        for i in range(len(articleVariables)):
            article1 = articleList[starting_index]  # first row values
            article2 = articleList[starting_index + 1]  # second row values
            variable = articleVariables[i]  # field value types

            # create the grid row with column name and row values according to the column name
            self.create_row(self.root, f'{variable}:', f'{getattr(article1, variable)}',
                            f'{getattr(article2, variable)}')

        self.create_merge_row(self.root)

        self.root.wm_state('iconic')  # used to minimize on startup

        tk.Message(self.root, textvariable=self.save_status_msg)  # TODO fix the message popup: __init__, setup, buttonAccept

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

        # simple lack of checks in checkbox checker
        result = self.has_consecutive_ones_or_zeros(bools)
        if result:
            print("NOTICE! The list has three consecutive 1s or 0s.")

        text = self.article_controller.merge_articles(bools, strings)
        self.save_status_msg.set(text)
        print(text)

    def buttonCancel(self):
        self.root.destroy()

    def checkTicks(self):
        bin_val_list = []
        text_list = []
        text_types_list = Article.getListOfVariables()
        for widget in reversed(self.root.grid_slaves()):
            if isinstance(widget, tk.Checkbutton):
                variable = widget.cget('variable')
                value = self.root.getvar(variable)
                bin_val_list.append(str(value))  # stringify to make iterable
            elif isinstance(widget, tk.Label):
                # could add check to see if text = column name and then get rid of it
                text = widget.cget('text')
                # Add check to prevent collection text_types
                if text[:-1] not in text_types_list:
                    text_list.append(text)

        # visual confirmation
        print('# Bool list: ' + str(bin_val_list))
        print('# Text list: ' + str(text_list))
        print(f'# Length of lists: bool = {str(len(bin_val_list))}, string = {str(len(text_list))}')

        return bin_val_list, text_list

    def has_consecutive_ones_or_zeros(self, bit_list):
        joined_list = ''.join(bit_list)  # Convert the list to a single string for pattern matching
        # patterns only take half of illegal choices into account, should be extended with something like '01001'
        if '111' in joined_list or '000' in joined_list:
            print(joined_list)
            return True
        return False
