# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd

from util import *

EVENT_ID = 666


def main():
    signals = pd.read_csv("../Data/signals.zip")
    signals = signals[signals["tn"] == EVENT_ID]
    backgrounds = pd.read_csv("../Data/backgrounds.zip")
    backgrounds = backgrounds[backgrounds["tn"] == EVENT_ID]

    offset = 36
    for layer, n_cell in enumerate(N_CELLS):
        theta = 2 * np.pi * np.arange(n_cell) / n_cell
        r = np.full((n_cell, ), offset + layer)
        plt.polar(theta, r, "ko", markersize=0.25)

    theta = []
    r = []
    for hit in backgrounds.itertuples():
        theta.append(2 * np.pi * hit.cell / N_CELLS[hit.layer])
        r.append(hit.layer + offset)
    plt.polar(theta, r, "ro", markersize=2, label="background")

    theta.clear()
    r.clear()
    for hit in signals.itertuples():
        theta.append(2 * np.pi * hit.cell / N_CELLS[hit.layer])
        r.append(hit.layer + offset)
    plt.polar(theta, r, "bo", markersize=2, label="signal")

    plt.yticks(tuple())
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
