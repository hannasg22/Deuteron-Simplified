"""This module takes the values we want to use in the model and saves them
in a file values_deuteron.jsonl to later use them in the calculations.
"""

import jsonlines

# DATA FOR DEUTERON MODEL
data_deuteron = [
    {"Potential": "Central", "Depth_c": 35.0, "Range_c": 2.0},
    {"Initial conditions": "us wavefunction", "us_0": 0.0, "vs_0": 1.0},
    {"Boundary condition": "Final value", "us_fin": 0.0},
    {"Range of radius": "Range r", "r_initial": 0.1, "r_final": 10.0},
    {"Energy guess": -1.5}
]

# FILE TO SAVE DATA
file_name = "values_deuteron.jsonl"

# TO WRITE VALUES IN THE FILE
with jsonlines.open(file_name, mode='w') as writer:
    writer.write_all(data_deuteron)

print(f"'{file_name}' file has been created with the deuteron data in JSON lines format.")
