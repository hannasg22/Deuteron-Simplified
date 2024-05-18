# Simplified model for the deuteron

## Goal of the code

Bfriefly explained, this code is provided to solve specifically the most simplified case of the deuteron equation(s) and get its eigenfunction and eigenvalue.

In order to find the results, a specific model for the potential is implemented. But another option could be applied, making use of the user's preferred election.

## Theory

## How to get the results

## Structure of the project
The code is divided in the next files:
- In [generate_data.py](generate_data.py) we insert the data we want to apply for the potential and for the initial and boundary conditions. This will generate a data file called [values_deuteron.jsonl](values_deuteron.jsonl) in JSON lines format and it will allow us to read the data and work with specific values easily.
- In [get_values.py](get_values.py) we extract the data saved in [values_deuteron.jsonl](values_deuteron.jsonl) to later use it easoly in the rest of the code.
- In [potential.py](potential.py) we have the function defining the potential which will be applied to model the deuteron interaction. This is my simplified implementation, but it could be replaced by the user's choice taking care of the form of the function, the inputs, outputs and the dimension of the parameters to be implemented.
- In [schro_equation.py](schro_equation.py) we express the system of equations through the function **rad_equation**. This is the system we will later implement in _solve_ivp_ function of SciPy to get the deuteron eigenfunction.
- In [find_energy.py](find_energy.py) we take the just explained function and insert it in the _solve_ivp_ SciPy method. After that, we compare the obtained eigenfunction's value for the last analysed point of the radius and the actual boundary condition we look for. This way we get the difference between those two values as the output of the **error_E** function defined there.
- In [run.py](run.py) we finally take the **error_E** function and apply it to a root finding method to obtain the energy value minimizing the error. In this case the chosen method is called 'secant', which is defined inside _root_scalar_ function of SciPy. After getting the proper eigenvalue, we can solve again our system described in [schro_equation.py](schro_equation.py) but this time with the correct E value. At this point, the code just will show the obtained result for the energy and the eigenfunction in a plot."
- In [tests.py](tests.py) we test that each function of each module of the code works as it should and has the expected outputs.

