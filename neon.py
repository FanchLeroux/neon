# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:06:56 2025

@author: fleroux
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits

filename = "ngc4065_panstarrs_g.fits"

path = Path(__file__).parent / filename

#hdul = fits.open(path)

with fits.open(path) as hdul:
   hdul.verify('fix')
   data = np.array(hdul[0].data)
   
plt.imshow(np.log(data), cmap='viridis')
plt.show()