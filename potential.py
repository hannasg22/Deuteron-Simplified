"""This module will contain the potential used to solve our equations.

Parameters needed in the potential:
    r0 : r value for the range of the square well potential (dimensions: fm)
    V_C0 : depth of the potential (dimensions: MeV)
These values must be chosen due to experimental data.

For further information check README.md section.
"""

import get_values as get

# SIMPLIFIED CENTRAL POTENTIAL
def V_c_squarewell(r):
    """This function calculates the value of the central potential for the
    introduced value of r.         

    Input:
        r : distance between proton and neutron

    Output:
        Value of the potential for that certain r
    """

    # Inserting values for central potential
    V0_c = get.central_V()[0]
    r0_c = get.central_V()[1]
    if r <= r0_c:
        return -V0_c
    else:
        return 0.0
