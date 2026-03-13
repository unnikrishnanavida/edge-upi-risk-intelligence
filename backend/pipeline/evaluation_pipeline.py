from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score


class ModelEvaluator:

    def evaluate(self, y_true, y_pred, y_prob):

        results = {}

        results["precision"] = precision_score(y_true, y_pred)
        results["recall"] = recall_score(y_true, y_pred)
        results["f1"] = f1_score(y_true, y_pred)
        results["roc_auc"] = roc_auc_score(y_true, y_prob)

        return results