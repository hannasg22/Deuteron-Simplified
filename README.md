# Simplified model for the deuteron

## Goal of the code

Bfriefly explained, this code is provided to solve specifically the most simplified case of the deuteron equation(s) and get its eigenfunction and eigenvalue.

In order to find the results, a specific model for the potential is implemented. But another option could be applied, making use of the user's preferred election.

## Theory

## How to get the results

## Structure of the project
The code is divided in the next files:
- In [potential.py](potential.py) we have the function defining the potential which will be used to model the deuteron interaction. This is my simplified implementation, but it could be replaced by the user's model taking care on the form of the function, the inputs, outputs and parameters to be implemented.
- In [schro_equation.py](schro_equation.py) we express the system of equations through the function **rad_equation**. This is the system we will later implement in _solve_ivp_ to get the eigenfunction.
- In [tests.py](tests.py) we test that each function of each module of the code works as it should.
- In [generate_data.py](generate_data.py) we insert the data we want to apply for the potential and for the initial and boundary conditions. This will generate a data file called [values_deuteron.jsonl](values_deuteron.jsonl) in JSON lines format and it will allow us to read the data and work with specific values easily.
