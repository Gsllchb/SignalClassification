# coding: utf-8
import pandas as pd

import dot
from constants import *


def load_data(path: str):
    dtype = {
        "layer": DTYPE_LAYER,
        "left_time": DTYPE_TIME,
        "time": DTYPE_TIME,
        "right_time": DTYPE_TIME,
        "left_energy": DTYPE_ENERGY,
        "energy": DTYPE_ENERGY,
        "right_energy": DTYPE_ENERGY,
        "signal": DTYPE_SIGNAL,
    }
    data = pd.read_csv(path, dtype=dtype, engine="c")

    features = (
        "layer",
        "left_time",
        "time",
        "right_time",
        "left_energy",
        "energy",
        "right_energy",
    )
    target = "signal"
    X = data.loc[:, features]
    y = data.loc[:, target]
    return X, y


def get_pa_nr_and_threshold(fprs, tprs, thresholds, min_tprs):
    res = []
    for min_tpr in min_tprs:
        for fpr, tpr, threshold in zip(fprs, tprs, thresholds):
            if tpr >= min_tpr:
                res.append((tpr, 1 - fpr, threshold))
                break
    return res
