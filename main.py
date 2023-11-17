from Controller.ArticleController import ArticleController
import os
from GUI.MainMenu import MainMenu
from Database.DbArticle import DbArticle
from ApiAccess import ApiAccess

testController = ArticleController()

status = ApiAccess.getstatus_ml()
check = ApiAccess.evaluate_ml("Role")
print(status)
print(check)

# testController.addArticles("C:/Users/mille/PycharmProjects/mergePure/Data/SampleDataMergeSystemCSV.csv")
currentDirectory = os.path.dirname(__file__)
filePath = os.path.join(currentDirectory, 'Data', 'SampleDataMergeSystemCSV.csv')

articleList = testController.addArticles(filePath)

db = DbArticle()
db.TestDatabase()

main = MainMenu()
main.setup(articleList)
