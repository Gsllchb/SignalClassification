# coding: utf-8
"""分别作信号和噪音数(密度)在沉积能量、漂移时间、半径及phi上的分布图"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from constants import *

BIN_NUM = 50


def main():
    signals = pd.read_csv("../Data/signals.zip")
    backgrounds = pd.read_csv("../Data/backgrounds.zip")

    signal_label = "signal"
    background_label = "background"

    density = True
    y_label = "hit density"

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
    plt.xlabel("deposit energy (log2 scale)")
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
    plt.xticks(range(-100, 1201, 200))
    plt.xlabel("drift time")
    plt.ylabel(y_label)
    plt.show()

    # layer distribution
    plt.hist(
        signals.layer,
        N_LAYERS,
        density=density,
        alpha=0.5,
        label=signal_label,
    )
    plt.hist(
        backgrounds.layer,
        N_LAYERS,
        density=density,
        alpha=0.5,
        label=background_label,
    )
    plt.legend()
    plt.xticks(np.arange(0, 18, 1))
    plt.xlabel("layer")
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
