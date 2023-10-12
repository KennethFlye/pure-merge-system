import os
import pymssql
from decouple import config


class DbArticle:
    global cursor

    def __init__(self):
        connection = pymssql.connect(config('SERVER'), config('USER'), config('PASSWORD'), config('CATALOG'))
        cursor = connection.cursor(as_dict=True)

    def TestDatabase(self):
        cursor.execute('SELECT * FROM authors')
        for row in cursor:
            print("Name=%s" % (row['name']))