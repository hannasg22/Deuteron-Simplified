"""This file contains the values we will use in the model and saves them
in the file values_deuteron.jsonl to later put them in the calculations.
"""

import jsonlines

# Define the data for the deuteron
data_deuteron = [
    {"Potential": "Central", "Depth_c": 36.7, "Range_c": 2.0},
    {"Initial conditions": "us wavefunction", "us_0": 0.0, "vs_0": 1.0},
    {"Boundary condition": "Final value", "us_fin": 0.1},
    {"Range of radius": "Range r", "r_initial": 0.001, "r_final": 10.0},
    {"Energy guess": -2.0}
]

file_name = "values_deuteron.jsonl"
# Write the values inside the JSONLines file
with jsonlines.open(file_name, mode='w') as writer:
    writer.write_all(data_deuteron)

print(f"'{file_name}' file has been created with the deuteron data in JSON lines format.")
