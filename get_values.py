"""This module will define all variables described in the values_deuteron.jsonl
to later use them in the potential.py, deuteron.py and run.py files.
We will have functions getting the values of:
    - Potential depth and range
    - Initial conditions
    - Boundary conditions
    - Range of radius r
    - Energy guess value
"""

import jsonlines

def central_V():
    file_name = "values_deuteron.jsonl"
    depth_and_range = [] # Form of the vector will be [V_C0, r0]

    # Open file and read potential data
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

    # Open file and read initial conditions
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Initial conditions" in line:
                if "us_0" in line:
                    init_cond.append(line["us_0"])
                if "vs_0" in line:
                    init_cond.append(line["vs_0"])
    return init_cond
   
def boundary_conditions():
    file_name = "values_deuteron.jsonl"
    bound_cond = []

    # Open file and read boundary condition
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Boundary condition" in line:
                bound_cond.append(line)

    us_fin = bound_cond[0]['us_fin']
    return us_fin

def range_of_radius():
    file_name = "values_deuteron.jsonl"
    r_range = []

    # Open file and read values for minimum and maximum r
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

    # Open file and read first guess of E value
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Energy guess" in line:
                E_guess = line["Energy guess"]
    return E_guess

