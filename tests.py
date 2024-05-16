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
    
    def test_initial_conditions(self):
        result = get.initial_conditions()
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one
        self.assertEqual(len(result), 2)

    def test_boundary_conditions(self):
        result = get.boundary_conditions()
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


if __name__ == '__main__':
    unittest.main()
