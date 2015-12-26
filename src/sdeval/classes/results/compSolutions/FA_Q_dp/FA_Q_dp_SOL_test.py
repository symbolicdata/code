import unittest
from FA_Q_dp_SOL import FA_Q_dp_SOL

class Test_FA_Q_dp_SOL(unittest.TestCase):
    """
    This is the test routine to test the class FA_Q_dp_SOL, which represents the solution of
    a computation of a Groebner basis for a given list of generators of an ideal.

    . moduleauthor:: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def test_FA_Q_dp_SOL(self):
        """
        This test routine tests the class FA_Q_dp_SOL for consistency.
        The tests that are covered by this function are:
        1. Initialization of FA_Q_dp_SOL
           1.a) Incorrect type for basis
           1.b) Incorrect type for originalGenerators
           1.c) Incorrect type for variables
           1.d) Incorrect type for upToDeg
           1.e) Correct type for basis, but the other parameters are not inputted
           1.f) Correct type for basis and other parameters are inputted
        2. Test the getters and setters of FA_Q_dp_SOL
        3. Test the string representation of FA_Q_dp_SOL
           3.a) With optional parameters left out
           3.b) With optional parameters included
        """
        #1.a)
        testPassed = True
        try:
            faqdpsolinst = FA_Q_dp_SOL(1)
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 1.a) failed; could instantiate FA_Q_dp_SOL with integer as basis")
            
        try:
            faqdpsolinst = FA_Q_dp_SOL([1,2,3,4])
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 1.a) failed; could instantiate FA_Q_dp_SOL with integer list as basis")
        #1.b
        try:
            faqdpsolinst = FA_Q_dp_SOL(["x"],1)
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 1.b) failed; could instantiate FA_Q_dp_SOL with integer as original generator list")
            
        try:
            faqdpsolinst = FA_Q_dp_SOL(["x"],[1,2,3,4])
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 1.b) failed; could instantiate FA_Q_dp_SOL with integer list as original generator list")

        #1.c)
        try:
            faqdpsolinst = FA_Q_dp_SOL(["x"],["x"],1)
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 1.c) failed; could instantiate FA_Q_dp_SOL with integer as variable list")
            
        try:
            faqdpsolinst = FA_Q_dp_SOL(["x"],["x"],[1,2,3,4])
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 1.c) failed; could instantiate FA_Q_dp_SOL with integer list as variable list")
        #1.d
        try:
            faqdpsolinst = FA_Q_dp_SOL(["x"],["x"],["x"],[])
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 1.d) failed; could instantiate FA_Q_dp_SOL with list as maximal degree")

        #1.e
        try:
            faqdpsolinst = FA_Q_dp_SOL(["x"])
        except:
            self.fail("Test 1.e) failed. Could not instantiate FA_Q_dp_SOL with correct solution basis type")

        #1.f
        try:
            faqdpsolinst = FA_Q_dp_SOL(["x"],["y"],["z"],1)
        except:
            self.fail("Test 1.f) failed. Could not instantiate FA_Q_dp_SOL with parameter input types")

        #2
        faqdpsolinst = FA_Q_dp_SOL(["x"],["y"],["x","y"],1)
        self.assertEqual(faqdpsolinst.getBasis(),["x"], "Test 2 failed. Wrong basis returned")
        self.assertEqual(faqdpsolinst.getOriginalGenerators(), ["y"],
                         "Test 2 failed. Wrong list of original generators returned.")
        self.assertEqual(faqdpsolinst.getVars(), ["x","y"], "Test 2 failed. Wrong list of variables returned.")
        self.assertEqual(faqdpsolinst.getUpToDeg(), 1, "Test 2 failed. Wrong maximal degree returned by getter.")

        #3.a
        faqdpsolinst = FA_Q_dp_SOL(["x"])
        outp = str(faqdpsolinst)
        expectedString = """====================
The Calculated Groebner basis is:
x

====================
Optional Information, if provided
--------------------
The original list of generators was:


The set of variables is:


The degree, up to which the Groebner basis was calculated is: 0
====================
"""
        self.assertEqual(outp, expectedString, "Test 3.a failed. Strings did not match")

        #3.b
        faqdpsolinst = FA_Q_dp_SOL(["x"],["y"],["x","y"],1)
        outp = str(faqdpsolinst)
        expectedString = """====================
The Calculated Groebner basis is:
x

====================
Optional Information, if provided
--------------------
The original list of generators was:
y

The set of variables is:
x, y

The degree, up to which the Groebner basis was calculated is: 1
====================
"""
        self.assertEqual(outp, expectedString, "Test 3.b failed. Strings did not match")
