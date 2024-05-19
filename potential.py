"""This file contains the potential used to solve the system.

Parameters needed in the potential:
    r0_c: r value for the range of the square well potential (units: fm)
    V0_c: depth of the potential (units: MeV)
These values must be chosen due to experimental data.
"""

import get_values as get

# SIMPLIFIED CENTRAL POTENTIAL
def V_c_squarewell(r):
    """This function calculates the value of the central potential for the
    introduced value of r.         

    Input:
        r: distance between proton and neutron
    Output:
        Value of the potential for that r
    """
    # Inserting values for the central potential from get_values.py
    V0_c = get.central_V()[0]
    r0_c = get.central_V()[1]
    # Define the square well potential
    if r <= r0_c:
        return -V0_c
    else:
        return 0.0
