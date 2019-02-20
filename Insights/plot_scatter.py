# coding: utf-8
import random

import matplotlib.pyplot as plt
import pandas as pd

import dotdot
from constants import *


def main():
    signals = pd.read_csv("../Data/signals.zip")
    backgrounds = pd.read_csv("../Data/backgrounds.zip")

    n_event = max(signals["tn"]) + 1

    for _ in range(20):
        event_id = random.randrange(0, n_event)
        plt.scatter(
            signals[signals.tn == event_id]["mdetmt0"],
            np.log10(signals[signals.tn == event_id]["me"]),
            s=2,
            label="signal"
        )
        plt.scatter(
            backgrounds[backgrounds.tn == event_id]["mdetmt0"],
            np.log10(backgrounds[backgrounds.tn == event_id]["me"]),
            s=2,
            label="backgrounds"
        )
        plt.legend()
        plt.xlabel("time")
        plt.ylabel("log10(energy)")
        plt.title("event_id: {}".format(event_id))
        plt.show()


if __name__ == '__main__':
    main()
