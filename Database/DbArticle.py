import os
import pymssql
from decouple import config


class DbArticle:

    AuthorExistsSQL = "SELECT CASE WHEN EXISTS(SELECT * FROM [Author] WHERE name = %s)THEN CAST(1 AS BIT) ELSE CAST(0 AS BIT) END AS Result"
    def __init__(self):
        connection = pymssql.connect(config('SERVER'), config('USER'), config('PASSWORD'), config('CATALOG'))
        self.cursor = connection.cursor(as_dict=True)


    def insertArticles(self, articleList):
        for article in articleList:
            # Tjekkes efter om der findes submitter i databasen, hvis ikke opret den
            self.addSubmitter(article.submitter)
            # Tjekkes efter om alle forfatterne findes i databasen, hvis ikke opret dem
            self.addAuthors(article.author)
            # Tilføj de kommentar der er til databasen
            self.addComments(article.comments)
            # Tjek om kategorierne findes i databasen, hvis ikke opret dem
            self.addCategories(article.categories)
            # Tjek om Authors Parsed findes i databasen, hvis ikke tilføj dem
            # self.addAuthorsParsed(article.authorsParsed)

            # Tilføj artiklen


            pass






    def addSubmitter(self, submitter):
        #self.cursor.execute(self.AuthorExistsSQL, [submitter])
        #self.cursor[0]
        pass



    def addAuthors(self, author):
        pass

    def addComments(self, comments):
        pass

    def addCategories(self, categories):
        pass

    def addAuthorsParsed(self, authorsParsed):
        pass

    def TestDatabase(self):
        self.cursor.execute('SELECT * FROM Author')
        for row in self.cursor:
            print("Name=%s" % (row['name']))
        self.cursor.execute(self.AuthorExistsSQL, "B. Tables")
        for row in self.cursor:
            print("Answer = %s" % (row['Result']))