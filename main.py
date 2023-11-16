from Controller.ArticleController import ArticleController
from ApiAccess.DBApiAccess import DBApiAccess
import os
from GUI.MainMenu import MainMenu
from Database.DbArticle import DbArticle

testController = ArticleController()

currentDirectory = os.path.dirname(__file__)
filePath = os.path.join(currentDirectory, 'Data', 'SampleDataMergeSystemCSV.csv')

# Start ML API before running
articles = DBApiAccess.get_articles_from_db()
# check = DBApiAccess.evaluate_db("Role")
print('List of articles: ' + str(articles))
# print(check)

articleList = testController.addArticles(filePath)

db = DbArticle()
db.TestDatabase()

main = MainMenu()
main.setup(articleList)
