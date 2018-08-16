# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:27:54 2018

@author: 502755426
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contour(x, y, z)