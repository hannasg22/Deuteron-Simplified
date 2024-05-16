"""Here we will solve through an initial value problem and a root finding method
the equations.

We actually do not know the initial value of us' and it must be a guess, but
the only part in which it will affect will be in the normalization of the
function. Therefore, we can use whatever guess we want and find the proper E
value: the eigenvalue.

"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import root_scalar
import potential as pot
import get_values as get
import schro_equation as eq

# DIFFERENCE BETWEEN EIGENFUNCTION WITH E_GUESS AND OUR BOUNDARY CONDITION
def error_E(E_guess):
    """This function analyses if the result obtained with E_guess matchs the
    desired boundary condition.

    For that we solve the system of equations with E_guess and compare the
    result in the ending point with the desried boundary condition.

    Inputs:
        E_guess: value of E for which we solve the equations

    Output:
        error: difference between the final point value with E_guess and the
               actual value we want to achieve
    """

    # Here we implement the needed data in the function
    r_values = get.range_of_radius()
    initial_values = get.initial_conditions()
    final_value = get.boundary_condition()

    # Solve system with solve_ivp function using RK45 method
    solut_guess = solve_ivp(lambda r, y: radial_equations(r, y, E_guess),
                            r_values, initial_values, method='RK45', max_step=0.01)

    # Difference between solution with E_guess and the actual value we look for
    error = solut_guess.y[0][-1] - final_value

    return error
