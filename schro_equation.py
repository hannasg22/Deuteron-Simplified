"""This module contains the simplified deuteron equation we want to solve to
get the eigenvalue (only bound state of the system) and the eigenfunction.

Important information about units of measurements:
    Units used:
        - Distances: fm
        - Mass: MeV / c**2
        - Energy: MeV
    We defined the reduced Planck constant with the next dimensions:
        h_bar * c = 197.327 MeV * fm
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import potential as pot

def radial_equation(r, y, E):
    """This function defines from our 2nd order differential equation a system
    of 2 1st order ODEs, generated to later solve the problem with SciPy.

    We have the eigenfunction 'us' representing the l=0 s-wave. From there, we
    define:
        dus: 1st derivative of the eigenfunction us, which will be named as vs
        dvs: 2nd derivative of the eigenfunction us (1st derivative of vs)
    Inputs:
        r: distance between both nucleons
        E: energy value
        y: vector which will contain the variables [us, vs]
    Output:
        [dus, dvs]: the system of 1st order ODEs which will be solved with
                    SciPy
    """

    us, vs = y
    # Definition of needed parameters
    h_bar = 197.327 # Reduced Planck constant
    M = 938.918 # 2 times the reduced mass of deuteron

    # System of equations we want to solve
    dus = vs
    dvs = (M / (h_bar**2)) * (pot.V_c_squarewell(r) - E) * us

    return [dus, dvs]
