"""We define the root finding process to achieve the proper eigenvalue.

We take the function 'radial_equation' from schro_equation.py, which
contains the system we must solve. We then solve it inside the 'error_E'
function through an integration method for the inserted energy value.

So, to carry out the integration we make use of the next SciPy function:
    - integrate.solve_ivp --> solves the system with the inserted E
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar

import potential as pot
import schro_equation as eq
import get_values as get


def error_E(E_guess):
    """This function analyses if the result obtained with E_guess
    matches the desired boundary condition.

    We solve the system of equations with E_guess and compare the
    result in the final point with the desired boundary condition
    us_fin.

    Inputs:
        E_guess: value of energy for which we solve the equations
    Output:
        error: difference between the final point value with E_guess and
               the actual value we want to achieve
    """
    # Get the conditions from the data file
    ini_cond = get.initial_conditions()
    us_fin = get.boundary_condition()
    r_range = get.range_of_radius()

    # Solve system for E_guess
    solution_guess = solve_ivp(lambda r, y: eq.radial_equation(r, y, E_guess),
                               r_range, ini_cond, method='RK45', max_step=0.01)
    
    # Difference between solution with E_guess and the boundary condition
    error = solution_guess.y[0][-1] - us_fin
    return error
