from Controller.ArticleController import ArticleController
import os
from GUI.MainMenu import MainMenu
from Database.DbArticle import DbArticle

testController = ArticleController()

currentDirectory = os.path.dirname(__file__)
filePath = os.path.join(currentDirectory, 'Data', 'SampleDataMergeSystemCSV.csv')

articleList = testController.addArticles(filePath)

db = DbArticle()
db.TestDatabase()

main = MainMenu()
main.setup(articleList)
