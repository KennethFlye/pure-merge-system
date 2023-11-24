from ApiAccess.MLApiAccess import MLApiAccess
class MLController:
    def __init__(self):
        self.ml_access = MLApiAccess()

    def get_accuracy_score(self, title_string1, title_string2):
        acc_score = self.ml_access.evaluate_titles(title_string1, title_string2)
