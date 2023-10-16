import os
import pymssql
from decouple import config


class DbArticle:
    #global cursor

    def __init__(self):
        connection = pymssql.connect(config('SERVER'), config('USER'), config('PASSWORD'), config('CATALOG'))
        self.cursor = connection.cursor(as_dict=True)


    def insertArticles(self, articleList):
        for article in articleList:
            self.addSubmitter(article.submitter)
            pass
            #Tjekkes efter om der findes submitter i databasen, hvis ikke opret den
            #Tjekkes efter om alle forfatterne findes i databasen, hvis ikke opret dem
            #Tilføj de kommentar der er til databasen
            #Tjek om kategorierne findes i databasen, hvis ikke opret dem
            #Tjek om Authors Parsed findes i databasen, hvis ikke tilføj dem

            #Tilføj artiklen

    def addSubmitter(self, submitter):
        pass

    def TestDatabase(self):
        self.cursor.execute('SELECT * FROM Author')
        for row in self.cursor:
            print("Name=%s" % (row['name']))