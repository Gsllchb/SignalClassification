# coding: utf-8
from sklearn.externals import joblib
from sklearn.metrics import log_loss, roc_curve, auc
import matplotlib.pyplot as plt

import dot
from util import *

PATH = "Models/150079861715.pkl"

MIN_TPRS = (0.90, 0.95, 0.99)


def main():
    clf = joblib.load(PATH)
    X, y = load_data("Data/test_set.zip")
    y_pred = clf.predict_proba(X)[:, 1]

    logloss = log_loss(y, y_pred)
    print("logloss: {}".format(logloss))

    fprs, tprs, thresholds = roc_curve(y, y_pred)

    auc_score = auc(fprs, tprs)
    print("auc: {}".format(auc_score))

    pa_nr_and_threshold = get_pa_nr_and_threshold(fprs, tprs, thresholds, MIN_TPRS)
    print("PA\tNR\tthreshold")
    for pa, nr, threshold in pa_nr_and_threshold:
        print("{}\t{}\t{}".format(pa, nr, threshold))

    plt.plot(fprs, tprs)
    plt.plot((0, 1), (0, 1), "--")
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.show()


if __name__ == '__main__':
    main()
