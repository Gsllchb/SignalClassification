# coding: utf-8
from sklearn.externals import joblib
from sklearn.metrics import log_loss, roc_auc_score, roc_curve

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

    auc = roc_auc_score(y, y_pred)
    print("auc: {}".format(auc))

    fprs, tprs, _ = roc_curve(y, y_pred)
    for fpr, tpr in zip(fprs, tprs):
        if tpr >= MIN_TPR:
            msg = "signal acceptance: {}, background rejection: {}."
            print(msg.format(tpr, 1 - fpr))
            break


if __name__ == '__main__':
    main()
