# coding: utf-8
import datetime

from sklearn.externals import joblib
from sklearn.metrics import log_loss, roc_auc_score
from sklearn.tree import DecisionTreeClassifier

import dot
from util import *


MIN_SAMPLES_LEAF = 384


LOG_FILE = "train.log"
DUMP_PATH_FMT = "Models/{}.pkl"
LOG_FMT = """
{time}
model id: {model_id}
{clf}
logloss: {logloss}
auc: {auc}
"""


def main():
    print("loading data...")
    X_train, y_train = load_data("Data/train_set.zip")

    clf = DecisionTreeClassifier(
        min_samples_leaf=MIN_SAMPLES_LEAF,
        class_weight="balanced",
        random_state=SEED,
    )

    print("training model...")
    clf.fit(X_train, y_train)

    model_id = abs(hash(clf))
    print("model id: {}".format(model_id))

    X_val, y_val = load_data("Data/val_set.zip")
    y_pred = clf.predict_proba(X_val)[:, 1]
    logloss = log_loss(y_val, y_pred)
    auc = roc_auc_score(y_val, y_pred)
    print("logloss: {}".format(logloss))
    print("auc: {}".format(auc))

    print("dumping...")
    joblib.dump(clf, DUMP_PATH_FMT.format(model_id), compress=True)

    print("logging...")
    content = LOG_FMT.format(
        time=datetime.datetime.now(),
        model_id=model_id,
        clf=clf,
        logloss=logloss,
        auc=auc,
    )
    with open(LOG_FILE, mode="a", encoding="utf-8") as f:
        f.write(content)

    print("All done!!!\a")


if __name__ == '__main__':
    main()
