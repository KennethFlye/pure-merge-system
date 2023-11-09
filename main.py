from Controller.ArticleController import ArticleController
from ApiAccess import ApiAccess
<<<<<<< HEAD
import os
from GUI.MainMenu import MainMenu
from Database.DbArticle import DbArticle
=======
>>>>>>> parent of 52a6d38 (Merge branch 'develop' into api-integration)


<<<<<<< HEAD
status = ApiAccess.getstatus_ml()
check = ApiAccess.evaluate_ml('Role')
print(status)
print(check)

currentDirectory = os.path.dirname(__file__)
filePath = os.path.join(currentDirectory, 'Data', 'SampleDataMergeSystemCSV.csv')
=======
# testController = ArticleController()
>>>>>>> parent of 52a6d38 (Merge branch 'develop' into api-integration)

status = ApiAccess.getstatus_ml()
check = ApiAccess.evaluate_ml("Role")
print(status)
print(check)


# testController.addArticles("C:/Users/mille/PycharmProjects/mergePure/Data/SampleDataMergeSystemCSV.csv")