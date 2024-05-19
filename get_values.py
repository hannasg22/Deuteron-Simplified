"""This module takes out all the variables described in values_deuteron.jsonl
to later apply them in the other files.

We have functions getting the values of:
    - Potential depth and range
    - Initial conditions
    - Boundary conditions
    - Range of radius r
    - Energy guess value
"""

import jsonlines

def central_V():
    file_name = "values_deuteron.jsonl"
    depth_and_range = [] # Form of the list will be [V0_c, r0_c]

    # Open values_deuteron.jsonl file and read the potential data
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Potential" in line:
                if "Depth_c" in line:
                    depth_and_range.append(line["Depth_c"])
                if "Range_c" in line:
                    depth_and_range.append(line["Range_c"])
    return depth_and_range

def initial_conditions():
    file_name = "values_deuteron.jsonl"
    init_cond = [] # Form of the vector will be [us_0, vs_0]

    # Open values_deuteron.jsonl file and read the initial conditions
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Initial conditions" in line:
                if "us_0" in line:
                    init_cond.append(line["us_0"])
                if "vs_0" in line:
                    init_cond.append(line["vs_0"])
    return init_cond
   
def boundary_condition():
    file_name = "values_deuteron.jsonl"

    # Open values_deuteron.jsonl file and read the boundary condition
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Boundary condition" in line:
                bound_cond = line['us_fin']
    return bound_cond

def range_of_radius():
    file_name = "values_deuteron.jsonl"
    r_range = []

    # Open values_deuteron.jsonl file and read the range of the radius
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Range of radius" in line:
                if "r_initial" in line:
                    r_range.append(line["r_initial"])
                if "r_final" in line:
                    r_range.append(line["r_final"])
    return r_range

def energy_guess():
    file_name = "values_deuteron.jsonl"

    # Open values_deuteron.jsonl file and read the first guess for the energy
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Energy guess" in line:
                E_guess = line["Energy guess"]
    return E_guess
