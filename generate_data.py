"""This module takes the values we want to use in the model and saves them
in a file values_deuteron.jsonl to later use them in the calculations.
"""

import jsonlines

# DATA FOR DEUTERON MODEL
data_deuteron = [
    {"Potential": "Central", "Depth_c": 36.5, "Range_c": 2.0},
    {"Initial conditions": "us wavefunction", "us_0": 0.0, "vs_0": 1.0},
    {"Boundary condition": "Final value", "us_fin": 0.2},
    {"Range of radius": "Range r", "r_initial": 0.001, "r_final": 10.0},
    {"Energy guess": -2.0}
]

# FILE TO SAVE DATA
file_name = "values_deuteron.jsonl"

# TO WRITE VALUES IN THE FILE
with jsonlines.open(file_name, mode='w') as writer:
    writer.write_all(data_deuteron)

print(f"'{file_name}' file has been created with the deuteron data in JSON lines format.")
