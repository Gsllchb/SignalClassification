# coding: utf-8
import numpy as np

SEED = 666

DTYPE_LAYER = np.int8
DTYPE_SIGNAL = np.int8
DTYPE_TIME = np.int16
DTYPE_ENERGY = np.float32


N_WIRES = 4482
N_LAYERS = 18
N_CELLS = tuple(range(198, 301, 6))
assert sum(N_CELLS) == N_WIRES
