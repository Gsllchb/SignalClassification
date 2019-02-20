# coding: utf-8
import numpy as np

SEED = 666

DTYPE_LAYER = np.int8
DTYPE_SIGNAL = np.int8
DTYPE_TIME = np.int16
DTYPE_ENERGY = np.float32


NUM_WIRE = 4482
NUM_LAYER = 18
NUM_CELL = tuple(range(198, 301, 6))
assert sum(NUM_CELL) == NUM_WIRE
