import pandas as pd
import os
from Model.Article import Article

class ArticleController():
    def __init__(self):
        pass

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

            article = Article(row.id, row.submitter, authors, row.title, row.comments, row.journalRef, row.doi, row.reportNo, row.categories, row.license, row.abstract, row.versions, row.update_date, row.authors_parsed)
            articleList.append(article)
            #print(f'{row.authors}')
            #print(f'{row.comments}')
            #print(f'Kategorier: {row.categories}')
            #print(f'Versioner: {row.versions}')
            #print(f'Authors parsed: {row.authors_parsed}')



        return articleList

    def AuthorsToList(self, authors):
        authorsList = [author.strip() for author in authors.split(",")]
        return authorsList
        pass

    def CommentsToList(self, comments):
        pass
