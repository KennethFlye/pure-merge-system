from Controller.ArticleController import ArticleController
from ApiAccess import ApiAccess


# testController = ArticleController()

status = ApiAccess.getstatus()
check = ApiAccess.evaluate("Role")
print(status)
print(check)


# testController.addArticles("C:/Users/mille/PycharmProjects/mergePure/Data/SampleDataMergeSystemCSV.csv")