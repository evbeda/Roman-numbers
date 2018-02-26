import unittest
from test_roman_to_int import (
    TestRomanToInt,
    Roman_to_decimal_to_roman,
)
from test_roman import TestRoman

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRomanToInt))
    test_suite.addTest(unittest.makeSuite(Roman_to_decimal_to_roman))
    test_suite.addTest(unittest.makeSuite(TestRoman))
    return test_suite


if __name__ == "__main__":
    #So you can run tests from this module individually.
    unittest.main()