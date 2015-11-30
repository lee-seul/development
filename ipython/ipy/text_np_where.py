# coding: utf-8
# test_np_where.py

# python 

import numpy as np
import matplotlib.pyplot as plt

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])

result1 = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]

print result

# ipython

result2 = np.where(cond, xarr, yarr)
