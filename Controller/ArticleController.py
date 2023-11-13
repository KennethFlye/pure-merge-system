import pandas as pd
import os
from ApiAccess import DBApiAccess
from Model.Article import Article


class ArticleController():
    def __init__(self):
        api_access = DBApiAccess

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

    def MergedArticles(self, preflist, textlist):
        # split lists for api to handle
        bool_list_left = preflist[::2]
        bool_list_right = preflist[1::2]
        text_list_left = textlist[::2]
        text_list_right = textlist[1::2]
        # print(f'left list: {text_list_left}')
        # print(f'right list: {text_list_right}')

        # combine the list for extraction
        comb_list_left = [val for pair in zip(text_list_left, bool_list_left) for val in pair]
        comb_list_right = [val for pair in zip(text_list_right, bool_list_right) for val in pair]
        print(f'left list: {comb_list_left}')
        print(f'right list: {comb_list_right}')

    def save_articles_to_db(self):
        # TODO send article lists to db
        pass
