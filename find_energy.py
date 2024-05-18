"""Here we define the root finding process.

We take the function from 'schro_equation.py', which has the system we need to
solve. We then use an integration process that gives the function lg the system
of equations with the given parameters.

So, to follow this process we will use the functions from SciPy:
    - solve_ivp --> to solve the equation with the introcued energy value
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import potential as pot
import schro_equation as eq
import get_values as get

# DIFFERENCE BETWEEN EIGENFUNCTIONS WITH E_GUESS AND OUR BOUNDARY CONDITION
def error_E(E_guess):
    """This function analyses if the result obtained with E_guess matches the
    desired boundary condition.

    For that we solve the system of equations with E_guess and compare the
    result in the ending point with the desired boundary condition us_fin.

    Inputs:
        E: value of energy for which we solve the equations

    Output:
        error: difference between the final point value with E_guess and the
               actual value we want to achieve
    """

    # Get the conditions to solve the problem
    ini_cond = get.initial_conditions()
    us_fin = get.boundary_condition()
    r_range = get.range_of_radius()

    # Solve for E_guess
    solution_guess = solve_ivp(lambda r, y: eq.radial_equation(r, y, E_guess),
                               r_range, ini_cond, method='RK45', max_step=0.01)

    # Difference between solution with E_guess and the actual value we want
    error = solution_guess.y[0][-1] - us_fin

    return error
