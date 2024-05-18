"""This module contains the code to solve the simplified deuteron equation and
get the eigenvalue (only bound state of the system) and eigenfunction.

Important information about units of measurements:
    Units used:
        - Distances: fm
        - Mass: MeV / c**2
        - Energy: MeV
    We will define the Planck constant with the next dimensions:
        h_bar * c = 197.327 MeV * fm
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import potential as pot
import get_values as get
