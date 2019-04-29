"""This module is to perform two unit tests"""
import unittest
from dataframe import df

class UnitTests(unittest.TestCase):
    """Define a class in which the tests will run"""

    def test_non_nan(self):
        """This is to test if there are no nan values"""
        self.assertFalse(df.isnull().values.any())

    def test_at_least_one_row(self):
        """This is to test if the dataframe has at least one row."""
        self.assertTrue(len(df) >= 1)

SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
unittest.TextTestRunner(verbosity=2).run(SUITE)
