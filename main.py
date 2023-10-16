from Controller.ArticleController import ArticleController
from GUI.MainMenu import MainMenu
from Database.DbArticle import DbArticle

testController = ArticleController()

articleList = testController.addArticles("C:/Users/mille/PycharmProjects/mergePure/Data/SampleDataMergeSystemCSV.csv")

#db = DbArticle()
#db.TestDatabase()

main = MainMenu()
main.setup(articleList)