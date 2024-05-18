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
import matplotlib.pyplot as plt
import schro_equation as eq
import get_values as get
import potential as pot

# DIFFERENCE BETWEEN EIGENFUNCTIONS WITH E_GUESS AND OUR BOUNDARY CONDITION
def error_E(E):
    """This function analyses if the result obtained with E_guess matches the
    desired boundary condition.

    For that we solve the system of equations with E_guess and compare the
    result in the ending point with the desried boundary condition.

    Inputs:
        E: value of emergy for which we solve the equations

    Output:
        error: difference between the final point value with E_guess
               and the actual value we want to achieve
    """
    # Get info from get_values
    r_range = get.range_of_radius()
    ini_cond = get.initial_conditions()
    us_fin = get.boundary_condition()
    E_guess = get.energy_guess()

    # Solve the system with 'RK45' method
    solution_guess = solve_ivp(lambda r, y: eq.radial_equation(r, y, E_guess),
                               r_range, ini_cond, method='RK45', max_step=0.01)
    # Difference between solution with E_guess and the actual value we look for
    error = solution_guess.y[0][-1] - us_fin
    return error

energy_value = root_scalar(error_E, bracket=[-5.0, 5.0])
E_binding = energy_value.root
print(E_binding)

solution_final = solve_ivp(lambda r, y: eq.radial_equation(r, y, E_binding),
                           get.range_of_radius(), get.initial_conditions(),
                           method='RK45', max_step=0.01)
"""
# FINAL RESULT
def final_result():
    # Get info from get_values
    E_guess = get.energy_guess()
    
    # Root finding process to get E
    E_solution = root_scalar(error_E(E_guess), bracket=[-5.0, 5.0])
    E_final = E_solution.root
    
    return E_final


E_binding = final_result()
us_eigenfunction = solve_ivp(lambda r, y: eq.radial_equation(r, y, E_binding),
                             get.range_of_radius(), get.initial_conditions(),
                             method='RK45', max_step=0.01)
"""

# To visualize u(r) vs. r and V(r)
r_values = solution_final.t
u_values = solution_final.y[0]
V_values = [pot.V_c_squarewell(r) for r in r_values]

# Graph of function u(r), V(r) and E
plt.figure()
plt.plot(r_values, 20 * u_values, label='u(r)')
plt.plot(r_values, V_values, label='Potential V(r) (MeV)')
plt.axhline(y=E_binding, color='r', linestyle='--', label='Binding energy E (MeV)')
plt.xlabel('r (fm)')
plt.ylabel('u(r)')
plt.title('Eigenfunction u(r) vs. ditance r')
plt.legend()
plt.grid(True)
plt.show()
