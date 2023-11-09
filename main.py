from Controller.ArticleController import ArticleController
from ApiAccess import MLApiAccess
import os
from GUI.MainMenu import MainMenu
from Database.DbArticle import DbArticle

testController = ArticleController()

currentDirectory = os.path.dirname(__file__)
filePath = os.path.join(currentDirectory, 'Data', 'SampleDataMergeSystemCSV.csv')

# Start ML API before running
# status = ApiAccess.getstatus_ml()
# check = ApiAccess.evaluate_ml("Role")
# print(status)
# print(check)

articleList = testController.addArticles(filePath)

db = DbArticle()
db.TestDatabase()

main = MainMenu()
main.setup(articleList)
