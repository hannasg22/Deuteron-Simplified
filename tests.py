"""This module will contain all the tests to check that the code works.

We will check each function, see that the given result is of the type we are
expecting and that the functions are actually doing what they are designed for.
"""

import unittest
import jsonlines
import potential as pot
import get_values as get
from hypothesis import given, settings
from hypothesis import strategies as st


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
        V0_c = get.central_V()[0]
        r0_c = get.central_V()[1]       
        # Take different probe values of r
        r = r_values.draw(st.floats(min_value = 0.0, max_value = 10.0))
        if r <= r0_c:
            V_expected = -V0_c
        else:
            V_expected = 0.0
        result = pot.V_c_squarewell(r)
        # Tests if the function returns the expected V value
        self.assertEqual(result, V_expected)


if __name__ == '__main__':
    unittest.main()
