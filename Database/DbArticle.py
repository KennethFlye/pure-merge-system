import os
import pymssql
from decouple import config


class DbArticle:
    #global cursor

    def __init__(self):
        connection = pymssql.connect(config('SERVER'), config('USER'), config('PASSWORD'), config('CATALOG'))
        self.cursor = connection.cursor(as_dict=True)

    def TestDatabase(self):
        self.cursor.execute('SELECT * FROM Author')
        for row in self.cursor:
            print("Name=%s" % (row['name']))