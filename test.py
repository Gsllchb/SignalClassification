# coding: utf-8
from sklearn.externals import joblib
from sklearn.metrics import log_loss, roc_curve, auc
import matplotlib.pyplot as plt

import dot
from util import *

PATH = "Models/150079861715.pkl"

MIN_TPR = 0.99


def main():
    clf = joblib.load(PATH)
    X, y = load_data("Data/test_set.zip")
    y_pred = clf.predict_proba(X)[:, 1]

    logloss = log_loss(y, y_pred)
    print("logloss: {}".format(logloss))

    fprs, tprs, _ = roc_curve(y, y_pred)

    auc_score = auc(fprs, tprs)
    print("auc: {}".format(auc_score))

    for fpr, tpr in zip(fprs, tprs):
        if tpr >= MIN_TPR:
            msg = "signal acceptance: {}, background rejection: {}."
            print(msg.format(tpr, 1 - fpr))
            break

    plt.plot(fprs, tprs)
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.show()


if __name__ == '__main__':
    main()
