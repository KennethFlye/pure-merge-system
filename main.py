from Controller.ArticleController import ArticleController
from ApiAccess import ApiAccess


# testController = ArticleController()

status = ApiAccess.getstatus_ml()
check = ApiAccess.evaluate_ml("Role")
print(status)
print(check)


# testController.addArticles("C:/Users/mille/PycharmProjects/mergePure/Data/SampleDataMergeSystemCSV.csv")