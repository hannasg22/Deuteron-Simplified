"""Here we define the root finding process. We take the functions from
'schro_equation.py', which has the system we need to solve. For that system, we
will use an integration process that will first be solved with the initial
guess we made for the energy eigenvalue (defined in 'generate_data.py' and
saved in 'values_deuteron.jsonl'.

So, to follow this process we will use two functions implemented by SciPy
    - solve_ivp --> to find the eigenvalue from the equation system
    - root_scalar --> to find the E value which obeys the boundary condition
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import schro_equation as eq
import get_values as get

# DIFFERENCE BETWEEN EIGENFUNCTIONS WITH E_GUESS AND OUR BOUNDARY CONDITION
def error_E(E_guess):
    """This function analyses if the result obtained with E_guess matches the
    desired boundary condition.

    For that we solve the system of equations with E_guess and compare the
    result in the ending point with the desried boundary condition.

    Inputs:
        E_guess: value of E for which we solve the equations

    Output:
        error: difference between the final point value with E_guess
               and the actual value we want to achieve
    """
    us_fin = get.boundary_condition()
    E_guess = get.energy_guess()

    # Solve the system with 'RK45' method
    solution_guess = solve_ivp(lambda r, y: eq.radial_equation(r, y, E_guess),
                            r_range, init_cond, method='RK45', max_step=0.01)
    # Difference between solution with E_guess and the actual value we look for
    error_us = solution_guess.y[0][-1] - us_fin
    # Total error
    error = error_us + error_ud
    return error

