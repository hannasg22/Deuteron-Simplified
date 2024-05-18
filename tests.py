"""This module will contain all the tests to check that the code works.

We will check each function, see that the given result is of the type we are
expecting and that the functions are actually doing what they are designed for.
"""

import unittest
import jsonlines
from hypothesis import given, settings
from hypothesis import strategies as st
import get_values as get
import potential as pot
import schro_equation as eq
import find_energy as find

# TESTS FOR get_values.py
class TestValues(unittest.TestCase):
    """In each case we will make sure that the returned object is of the type
    we expect it. These will be the expected outputs' forms in order to use
    them in the rest of the code.
    """

    def test_central_V(self):
        result = get.central_V()
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one
        self.assertEqual(len(result), 2)
    
    def test_initial_conditions(self):
        result = get.initial_conditions()
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one
        self.assertEqual(len(result), 2)

    def test_boundary_condition(self):
        result = get.boundary_condition()
        # Tests if the function returns a tuple
        self.assertIsInstance(result, float)
        
    def test_range_of_radius(self):
        result = get.range_of_radius()
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one
        self.assertEqual(len(result), 2)
        
    def test_energy_guess(self):
        result = get.energy_guess()
        # Tests if the function returns a float
        self.assertIsInstance(result, float)

# TESTS FOR potential.py
class TestCentralPotential(unittest.TestCase):
    """We extract the depth and range of the potential from the real data and
    compare the results we expect with the ones the function V_c_squarewell
    returns.
    """
    @given(r_values=st.data())
    @settings(max_examples=20)
    def test_V_c_squarewell(self, r_values):
        # Get actual values for potential depth and range from data file
        V0_c, r0_c = get.central_V()      
        # Take different probe values of r
        r = r_values.draw(st.floats(min_value = 0.0, max_value = 10.0))
        if r <= r0_c:
            V_expected = -V0_c
        else:
            V_expected = 0.0
        result = pot.V_c_squarewell(r)
        # Tests if the function returns the expected V value
        error_msg = f"""Error when calculating the potential value for r = {r},
                     we expect the value {V_expected} but got {result}."""
        self.assertAlmostEqual(result, V_expected, msg=error_msg)
        

# TESTS FOR schro_equation.py

# TESTS FOR find_energy.py
class TestErrorE(unittest.TestCase):
    """We will test that for the actual value of the eigenvalue we get a small
    error. This means that the function will find the root near that result.
    """

    def test_error_E(self):
        # Define the actual value of the binding energy for deuteron
        E_real = -2.25 # MeV
        # Error value with real binding energy
        error_min = abs(find.error_E(E_real))
        # Tolerance we accept for the error
        eps = 0.1
        # Tests if the error obtained for the real E is actually small
        error_msg = f"""This error function will not find the root near enough
                     of the binding energy {E_real}."""
        self.assertGreater(eps, error_min, msg=error_msg)



if __name__ == '__main__':
    unittest.main()
