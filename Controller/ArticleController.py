import pandas as pd
import re
import os
from ApiAccess.DBApiAccess import DBApiAccess
from Model.Article import Article


class ArticleController:
    def __init__(self):
        self.api_access = DBApiAccess()

    def addArticles(self, filePath):
        data = pd.read_csv(filePath, delimiter=";", encoding="ISO-8859-1", on_bad_lines='skip')

        articleList = []

        for row in data.itertuples():
            # TODO: Comments som en liste og ikke bare en lang streng (Ved ikke hvornår den går fra comment til comment)
            # TODO: Categories som en liste og ikke bare en lang streng (Mellemrum mellem hver kategori)
            # TODO: Versions som en liste og ikke bare en lang streng (Json Format?)
            # TODO: Authors Parsed som en liste og ikke bare en lang streng ([Efternavn, Fornavn, mellemrum])

            authors = self.AuthorsToList(row.authors)
            comments = self.CommentsToList(row.comments)

            article = Article(row.id, row.submitter, authors, row.title, row.comments, row.journalRef, row.doi,
                              row.reportNo, row.categories, row.license, row.abstract, row.versions, row.update_date)
            articleList.append(article)
            # print(f'{row.authors}')
            # print(f'{row.comments}')
            # print(f'Kategorier: {row.categories}')
            # print(f'Versioner: {row.versions}')
            # print('____________________________________________________________________')
            # print(' ')

        return articleList

    def AuthorsToList(self, authors):
        authorsList = [author.strip() for author in authors.split(",")]
        return authorsList
        pass

    def CommentsToList(self, comments):
        pass

    def merge_articles(self, preflist, textlist):
        # split lists for api to handle
        bool_list_left = preflist[::2]
        bool_list_right = preflist[1::2]
        text_list_left = textlist[::2]
        text_list_right = textlist[1::2]

        # combine the lists for saving
        comb_list_left = [val for pair in zip(text_list_left, bool_list_left) for val in pair]
        comb_list_right = [val for pair in zip(text_list_right, bool_list_right) for val in pair]

        # make lists comparable with db
        comb_list_left = self.type_refactoring(comb_list_left)
        comb_list_right = self.type_refactoring(comb_list_right)

        # add group number to list
        grp_no = self.find_group_number()
        comb_list_left.append(grp_no)
        comb_list_right.append(grp_no)

        print(f'# Left list: {comb_list_left}')
        print(f'# Right list: {comb_list_right}')

        # return success or not?
        self.save_articles_to_db(comb_list_left, comb_list_right)

    def save_articles_to_db(self, listLeft, listRight):
        # TODO call to_json
        result = self.api_access.post_to_db(listLeft, listRight)
        if result is not None:
            print('yippie its saved')
        else:
            print('oh no saving failed')
            # TODO return error to gui

    def find_group_number(self):
        # find the latest group number
        grp_no_json = self.api_access.get_group_number()
        print('# Highest group number: ' + str(grp_no_json))

        # extract number
        grp_no_list = [int(s) for s in re.findall(r'\d+', str(grp_no_json))]  # extract as list of integers

        return grp_no_list[0]

    def type_refactoring(self, art_list):
        # start at index 1, then skip to the second index after that, and so on
        for i in range(1, len(art_list), 2):
            # convert to int, then to bool
            bool_val = bool(int(art_list[i]))
            # replace stringified integer with bool
            art_list[i] = bool_val

        print('# Type refactored list: ' + str(art_list))
        return art_list
