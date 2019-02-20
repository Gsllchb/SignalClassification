# coding: utf-8
import pandas as pd
from sklearn.model_selection import train_test_split

import dotdot
from constants import *

RENAME_MAP = {
    "layer": "layer",
    "ldetmt0": "left_time",
    "mdetmt0": "time",
    "rdetmt0": "right_time",
    "le": "left_energy",
    "me": "energy",
    "re": "right_energy",
    "isSignal": "signal"
}
USECOLS = RENAME_MAP.keys()


def main():
    dtype = {
        "layer": DTYPE_LAYER,
        "ldetmt0": DTYPE_TIME,
        "mdetmt0": DTYPE_TIME,
        "rdetmt0": DTYPE_TIME,
        "le": DTYPE_ENERGY,
        "me": DTYPE_ENERGY,
        "re": DTYPE_ENERGY,
        "isSignal": DTYPE_SIGNAL,
    }

    signals = pd.read_csv(
        "signals.zip",
        usecols=USECOLS,
        dtype=dtype,
        engine="c"
    )

    backgrounds = pd.read_csv(
        "backgrounds.zip",
        usecols=USECOLS,
        dtype=dtype,
        engine="c",
    )

    data = backgrounds.append(signals, ignore_index=True)
    del backgrounds
    del signals
    data.rename(columns=RENAME_MAP, inplace=True)

    train_and_val_data, test_data = train_test_split(
        data,
        test_size=300_000,
        stratify=data["signal"],
        random_state=SEED,
    )
    train_data, val_data = train_test_split(
        train_and_val_data,
        test_size=300_000,
        stratify=train_and_val_data["signal"],
        random_state=SEED,
    )

    test_data.to_csv("test_set.zip", index=False, compression="zip")
    val_data.to_csv("val_set.zip", index=False, compression="zip")
    train_data.to_csv("train_set.zip", index=False, compression="zip")


if __name__ == '__main__':
    main()
