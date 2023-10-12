import pandas as pd
from Model.Article import Article

class ArticleController():
    def __init__(self):
        pass

    def addArticles(self, filePath):
        data = pd.read_csv(filePath, delimiter=";", encoding="ISO-8859-1", on_bad_lines='skip')

        articleList = []

        for row in data.itertuples():

            article = Article(row.id, row.submitter, row.authors, row.title, row.comments, row.journalRef, row.doi, row.reportNo, row.categories, row.license, row.abstract, row.versions, row.update_date, row.authors_parsed)
            articleList.append(article)


