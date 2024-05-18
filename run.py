"""Results will be obtained through this part of the code. Here we define the
root finding process.

To follow this process we will use two functions implemented by SciPy:
    - root_scalar --> to find the E value which obeys the boundary condition
    - solve_ivp --> to get the eigenfunction with the proper E value

So, first we find the actual value of E eigenvalue through root_scalar and
later we solve the equations for that proper energy with solve_ivp.
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import potential as pot
import schro_equation as eq
import get_values as get
import find_energy as find

# Find the value of E
E_value = root_scalar(find.error_E, method='secant', x0=get.energy_guess())
E_binding = E_value.root
print(E_binding)
# Get the eigenfunction with the proper E value
solution_final = solve_ivp(lambda r, y: eq.radial_equation(r, y, E_binding),
                           get.range_of_radius(), get.initial_conditions(),
                           method = 'RK45', max_step = 0.01)


# To visualize u(r) vs. r and V(r)
r_values = solution_final.t
u_values = solution_final.y[0]
V_values = [pot.V_c_squarewell(r) for r in r_values]

sns.set_style('darkgrid')

plt.figure(figsize=(8, 6))
plt.rcParams['axes.facecolor'] = 'black'
plt.plot(r_values, 20 * u_values, label='$u_s(r)$', color='deeppink', linewidth=2)
plt.plot(r_values, V_values, label='Potential $V_c(r) (MeV)$', color='lightpink', linewidth=2)
plt.axhline(y=E_binding, color='lavender', linestyle='--', linewidth=2.0,
            label='Binding energy $E (MeV)$')
plt.xlim(get.range_of_radius()[0], get.range_of_radius()[1])
plt.xlabel('$r (fm)$', fontsize=12, color='white')
plt.ylabel('$u_s(r)$', fontsize=12, color='white')
plt.suptitle('Graphic representation of the eigenfunction (with enlarged dimensions), the potential and the binding energy.', fontsize=10)
plt.title('$u_s(r)$ vs. $r (fm)$', fontsize=16)
plt.legend(fontsize=10, facecolor='black', edgecolor='white', labelcolor='white')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
