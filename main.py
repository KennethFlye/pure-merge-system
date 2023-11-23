import re

from Controller.ArticleController import ArticleController
from ApiAccess.DBApiAccess import DBApiAccess
import os
from GUI.MainMenu import MainMenu
# from Database.DbArticle import DbArticle

art_controller = ArticleController()

currentDirectory = os.path.dirname(__file__)
filePath = os.path.join(currentDirectory, 'Data', 'SampleDataMergeSystemCSV.csv')

# Start DB API before running
print('# List of articles from db: ')
articles = DBApiAccess.get_articles_from_db()
for a in articles:
    print('# ' + str(a))

articleList = art_controller.addArticles(filePath)

# db = DbArticle()
# db.TestDatabase()  # unused

# groupno = DBApiAccess.get_group_number()
# groupno = [int(s) for s in re.findall(r'\d+', str(groupno))]  # lent from articlecontroller.findgroupno
# s_index = groupno[0]
# if groupno[0] % 2 != 0:
#     s_index += 1  # probably needs to be potential incrementing or w/e
#
# print(f"# Latest group number: {groupno}, rounded up to index: {s_index}")

main = MainMenu()
main.setup(articleList, 0)  # kun lige tal eller s_index
