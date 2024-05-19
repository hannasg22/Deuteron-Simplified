"""This file contains all the tests to check that the code works as it should.

We will check each function, see that the given result is of the type we are
expecting and that the functions are actually doing what they are designed for.
"""

import unittest
import numpy as np
from hypothesis import given, settings
from hypothesis import strategies as st
import get_values as get
import potential as pot
import schro_equation as eq
import find_energy as find

# TESTS FOR get_values.py
class TestValues(unittest.TestCase):
    """In each case we will make sure that the returned object is of the type
    we expect. These will be the expected outputs' forms in order to use them
    in the rest of the files.
    """

    def test_central_V(self):
        result = get.central_V()
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one, 2
        self.assertEqual(len(result), 2)
    
    def test_initial_conditions(self):
        result = get.initial_conditions()
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one, 2
        self.assertEqual(len(result), 2)

    def test_boundary_condition(self):
        result = get.boundary_condition()
        # Tests if the function returns a float
        self.assertIsInstance(result, float)
        
    def test_range_of_radius(self):
        result = get.range_of_radius()
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one, 2
        self.assertEqual(len(result), 2)
        
    def test_energy_guess(self):
        result = get.energy_guess()
        # Tests if the function returns a float
        self.assertIsInstance(result, float)

# TESTS FOR potential.py
class TestCentralPotential(unittest.TestCase):
    """We extract the depth and range of the potential from the real data and
    compare the results we expect with the ones the function V_c_squarewell is
    returning.
    """
    
    @given(r_values=st.data())
    @settings(max_examples=20)
    def test_V_c_squarewell(self, r_values):
        # Get real values for the potential depth and range from the data file
        V0_c, r0_c = get.central_V()      
        # Make different probe values of r
        r = r_values.draw(st.floats(min_value=0.0, max_value=10.0))
        # Define the value we expect the function to return
        if r <= r0_c:
            V_expected = -V0_c
        else:
            V_expected = 0.0
        # Define the value the function is returning
        result = pot.V_c_squarewell(r)
        # Tests if the function returns the expected V value
        error_msg = f"""Error when calculating the potential value for r = {r},
                     we expect the value {V_expected} but got {result}."""
        self.assertAlmostEqual(result, V_expected, msg=error_msg)

# TEST FOR schro_equation.py
class TestSchroedingerEquation(unittest.TestCase):
    """We just test if the function returns a list of floats and if the length
    is the one we expect.
    """
    
    @given(st.floats(min_value=0.1, max_value=10.0), # r
           st.lists(st.floats(min_value=-1.0, max_value=1.0),
                    min_size=2, max_size=2), # y
           st.floats(min_value=-5.0, max_value=5.0) # E
           )
    @settings(max_examples=5)
    def test_radial_equation(self, r, y, E):
        result = eq.radial_equation(r, y, E)
        # Tests if the function returns a list
        self.assertIsInstance(result, list)
        # Tests if the dimension of the output is the expected one, 2
        self.assertEqual(len(result), 2)
        # Tests that the type of objects returned is the expected one
        self.assertIsInstance(result[0], (float, np.float64))
        self.assertIsInstance(result[1], (float, np.float64))

# TESTS FOR find_energy.py
class TestErrorE(unittest.TestCase):
    """We test that for the actual value of the eigenvalue we get a small
    error. This means that the function will find the root near that result.
    BEWARE: the rest of the conditions must also be appropriate.
    """
    
    def test_error_E(self):
        # Define the real value of the eigenvalue of deuteron
        E_real = -2.25 # MeV
        # Error value with real E value
        error_min = abs(find.error_E(E_real))
        # Tolerance we accept for the error
        eps = 0.1
        # Tests if the error obtained for the real E is actually small
        error_msg = f"""This error function will not find the root near enough
                     of the binding energy {E_real}."""
        self.assertGreater(eps, error_min, msg=error_msg)

if __name__ == '__main__':
    unittest.main()
