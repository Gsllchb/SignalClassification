# coding: utf-8
"""分别作信号和噪音数(密度)在沉积能量、漂移时间、半径及phi上的分布图"""
import matplotlib.pyplot as plt
import pandas as pd

import dotdot
from constants import *

BIN_NUM = 50


def main():
    signals = pd.read_csv("../Data/signals.zip")
    backgrounds = pd.read_csv("../Data/backgrounds.zip")

    signal_label = "signal"
    background_label = "background"

    for density in (True, False):
        y_label = "hit density" if density else "hit"

        # energy distribution
        plt.hist(
            np.log2(signals.me),
            BIN_NUM,
            density=density,
            alpha=0.5,
            label=signal_label,
        )
        plt.hist(
            np.log2(backgrounds.me),
            BIN_NUM,
            density=density,
            alpha=0.5,
            label=background_label,
        )
        plt.legend()
        plt.xlabel("log2(energy)")
        plt.ylabel(y_label)
        plt.show()

        # drift time distribution
        plt.hist(
            signals.mdetmt0,
            BIN_NUM,
            density=density,
            alpha=0.5,
            label=signal_label,
        )
        plt.hist(
            backgrounds.mdetmt0,
            BIN_NUM,
            density=density,
            alpha=0.5,
            label=background_label,
        )
        plt.legend()
        plt.xlabel("time")
        plt.ylabel(y_label)
        plt.show()

        # radius distribution
        plt.hist(
            signals.r,
            NUM_LAYER,
            density=density,
            alpha=0.5,
            label=signal_label,
        )
        plt.hist(
            backgrounds.r,
            NUM_LAYER,
            density=density,
            alpha=0.5,
            label=background_label,
        )
        plt.legend()
        plt.xlabel("r")
        plt.ylabel(y_label)
        plt.show()

        # phi distribution
        plt.hist(
            signals.phi,
            BIN_NUM,
            density=density,
            alpha=0.5,
            label=signal_label,
        )
        plt.hist(
            backgrounds.phi,
            BIN_NUM,
            density=density,
            alpha=0.5,
            label=background_label,
        )
        plt.legend()
        plt.xlabel("phi")
        plt.ylabel(y_label)
        plt.show()


if __name__ == '__main__':
    main()
