from Controller.ArticleController import ArticleController
from ApiAccess.DBApiAccess import DBApiAccess
import os
from GUI.MainMenu import MainMenu
from Database.DbArticle import DbArticle

testController = ArticleController()

currentDirectory = os.path.dirname(__file__)
filePath = os.path.join(currentDirectory, 'Data', 'SampleDataMergeSystemCSV.csv')

# Start ML API before running
print('# List of articles from db: ')
articles = DBApiAccess.get_articles_from_db()
for a in articles:
    print('# ' + str(a))

articleList = testController.addArticles(filePath)

db = DbArticle()
db.TestDatabase()

main = MainMenu()
main.setup(articleList)
