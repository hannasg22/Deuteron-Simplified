"""Here we will solve through an initial value problem and a root finding method
the equations.

We actually do not know the initial value of us' and it must be a guess, but
the only part in which it will affect will be in the normalization of the
function. Therefore, we can use whatever guess we want and find the proper E
value: the eigenvalue.

"""
# DIFFERENCE BETWEEN EIGENFUNCTIONS WITH E_GUESS AND OUR BOUNDARY CONDITIONS
def error_E(E_guess, r_range, init_cond, us_fin, ud_fin):
    """This function analyses if the results obtained with E_guess
    match the desired boundary conditions.

    For that we solve the system of equations with E_guess and compare
    the result in the ending point with the desried boundary conditions.

    Inputs:
        E_guess: value of E for which we solve the equations
        r_range: range of r in which we evaluate the equations
        init_cond: Initial conditions for the value of the functions
                   and its derivatives
        us_fin: desired boundary condition for the final point of us
        ud_fin: same but for ud

    Output:
        error: difference between the final point values with E_guess
               and the actual values we want to achieve
    """
    
    solut_guess = solve_ivp(lambda r, y: radial_equations(r, y, E_guess),
                            r_range, init_cond, method='RK45', max_step=0.01)
    # Difference between solution with E_guess and the actual value we look for
    error_us = solut_guess.y[0][-1] - us_fin
    error_ud = solut_guess.y[2][-1] - ud_fin
    # Total error
    error = error_us + error_ud
    return error
