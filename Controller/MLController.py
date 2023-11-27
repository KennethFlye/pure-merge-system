from ApiAccess.MLApiAccess import MLApiAccess
class MLController:
    def __init__(self):
        self.ml_access = MLApiAccess()

    def get_accuracy_score(self, title_string1, title_string2):
        acc_score = self.ml_access.evaluate_titles(title_string1, title_string2)

        acc_score_extracted = self.extract_accuracies(acc_score)

        return acc_score_extracted

    def extract_accuracies(self, acc_dict):
        accuracies_list = []
        if acc_dict is not None:
            percentage_title1 = acc_dict['result']['title1'][0]
            percentage_title2 = acc_dict['result']['title2'][0]

            accuracies_list.append(percentage_title1)
            accuracies_list.append(percentage_title2)

        return accuracies_list
