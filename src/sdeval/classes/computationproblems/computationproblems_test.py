import unittest
import copy
import FA_Q_dp
import GB_Fp_dp
import GB_Z_lp
import SOL_R_poly_sys

class TestComputationProblems(unittest.TestCase):
    """
    Contains tests for the different computation problems classes, namely
    - FA_Q_dp
    - GB_Z_lp
    - GB_Fp_dp
    - SOL_R_poly_sys

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def test_fileNameSanitizer(self):
        """
        This function tests the protected function _checkIfValidFileName inside
        the abstract class ComputationProblem.

        It should not accept strings that cannot appear as filenames.

        REMARK: As the function is protected, we are checking it via adding
                tables to associated tables of FA_Q_dp, as the function would
                return False if the string is not valid
        
        The covered tests are:
        1) Empty string (False)
        2) Whitespace string (False)
        3) "Singular" (True)
        4) "Python_(-v3-)_.txt" (True)
        5) "!@#$%^&*()_+=" (False)
        """
        cp = FA_Q_dp.FA_Q_dp()
        self.assertFalse(cp.addToAssociatedTables(""), "The file name sanitizer accepted the empty string")
        self.assertFalse(cp.addToAssociatedTables(" \t\n"), "The file name sanitizer accepted a whitespace string")
        self.assertTrue(cp.addToAssociatedTables("Singular"),
                        "The file name sanitizer rejected \"Singular\", a valid string")
        self.assertTrue(cp.addToAssociatedTables("Python_(-v3-)_.txt"),
                        "The file name sanitizer rejected \"Python_(-v3-)_.txt\", a valid string")
        self.assertFalse(cp.addToAssociatedTables("!@#$%^&*()_+="),
                        "The file name sanitizer accepted \"!@#$%^&*()_+=\", an invalid string")

    def test_FA_Q_dp(self):
        """
        This test tests the class FA_Q_dp for its stability.

        The covered tests are:
        1) "FreeAlgebras" is contained in the associated table list
        2) The name is FA_Q_dp
        3) The list of possible, applicable computer algebra systems should not be empty
           In fact, it should by now contain at least
           - Singular
           - Magma
           - GAP
        4) adding of an existing associated table does not change the table
        5) adding a non existing associated table works fine
        6) adding an existing computer algebra system does not change the table
        7) adding a non existing computer algebra system works fine
        """
        #1)
        compProblem=FA_Q_dp.FA_Q_dp()
        self.assertTrue("FreeAlgebras" in compProblem.getAssociatedTables(),
                        "The standard table, \"FreeAlgebras\", was not contained\
 in the class FA_Q_dp")
        #2)
        self.assertEqual("FA_Q_dp", compProblem.getName(), "The class FA_Q_dp does not\
 return a correct name")
        #3)
        self.assertTrue("Singular" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Singular is missing as a possible computer algebra system\
 solving FA_Q_dp")
        self.assertTrue("Magma" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Magma is missing as a possible computer algebra system\
 solving FA_Q_dp")
        self.assertTrue("GAP" in compProblem.getPossibleComputerAlgebraSystems(),
                        "GAP is missing as a possible computer algebra system\
 solving FA_Q_dp")
        #4)
        temp = copy.deepcopy(compProblem.getAssociatedTables())
        compProblem.addToAssociatedTables(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getAssociatedTables()),
                    "Adding of an existing table to the associated tables of FA_Q_dp\
 caused the list of associated tables to change.")
        #5)
        compProblem.addToAssociatedTables("RandomTableNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getAssociatedTables()),
                            "Adding of associated table to FA_Q_dp failed.")
        #6)
        temp = copy.deepcopy(compProblem.getPossibleComputerAlgebraSystems())
        compProblem.addToComputerAlgebraSystems(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                    "Adding of an existing table to the possible computer algebra systems of FA_Q_dp\
 caused the list of associated tables to change.")
        #7)
        compProblem.addToComputerAlgebraSystems("RandomCASNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                            "Adding of computer algebra system to FA_Q_dp failed.")

    def test_GB_Z_lp(self):
        """
        This test tests the class GB_Z_lp for its stability.

        The covered tests are:
        1) IntPS is contained in the associated table list
        2) The name is GB_Z_lp
        3) The list of possible, applicable computer algebra systems should not be empty
           In fact, it should by now contain at least
           - Singular
           - Magma
           - GAP
           - Maple
        4) adding of an existing associated table does not change the table
        5) adding a non existing associated table works fine
        6) adding an existing computer algebra system does not change the table
        7) adding a non existing computer algebra system works fine
        """
        #1)
        compProblem=GB_Z_lp.GB_Z_lp()
        self.assertTrue("IntPS" in compProblem.getAssociatedTables(),
                        "The standard table, \"IntPS\", was not contained\
 in the class GB_Z_lp")
        #2)
        self.assertEqual("GB_Z_lp", compProblem.getName(), "The class GB_Z_lp does not\
 return a correct name")
        #3)
        self.assertTrue("Singular" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Singular is missing as a possible computer algebra system\
 solving GB_Z_dp")
        self.assertTrue("Magma" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Magma is missing as a possible computer algebra system\
 solving GB_Z_dp")
        self.assertTrue("GAP" in compProblem.getPossibleComputerAlgebraSystems(),
                        "GAP is missing as a possible computer algebra system\
 solving GB_Z_dp")
        self.assertTrue("Maple" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Maple is missing as a possible computer algebra system\
 solving GB_Z_dp")
        #4)
        temp = copy.deepcopy(compProblem.getAssociatedTables())
        compProblem.addToAssociatedTables(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getAssociatedTables()),
                    "Adding of an existing table to the associated tables of GB_Z_dp\
 caused the list of associated tables to change.")
        #5)
        compProblem.addToAssociatedTables("RandomTableNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getAssociatedTables()),
                            "Adding of associated table to GB_Z_dp failed.")
        #6)
        temp = copy.deepcopy(compProblem.getPossibleComputerAlgebraSystems())
        compProblem.addToComputerAlgebraSystems(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                    "Adding of an existing table to the possible computer algebra systems of GB_Z_dp\
 caused the list of associated tables to change.")
        #7)
        compProblem.addToComputerAlgebraSystems("RandomCASNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                            "Adding of computer algebra system to GB_Z_dp failed.")

    def test_GB_Fp_dp(self):
        """
        This test tests the class GB_Fp_dp for its stability.

        The covered tests are:
        1) ModPS is contained in the associated table list
        2) The name is GB_Fp_dp
        3) The list of possible, applicable computer algebra systems should not be empty
           In fact, it should by now contain at least
           - Singular
           - Magma
           - GAP
           - Maple
        4) adding of an existing associated table does not change the table
        5) adding a non existing associated table works fine
        6) adding an existing computer algebra system does not change the table
        7) adding a non existing computer algebra system works fine
        """
        #1)
        compProblem=GB_Fp_dp.GB_Fp_dp()
        self.assertTrue("ModPS" in compProblem.getAssociatedTables(),
                        "The standard table, \"ModPS\", was not contained\
 in the class GB_Fp_dp")
        #2)
        self.assertEqual("GB_Fp_dp", compProblem.getName(), "The class GB_Fp_dp does not\
 return a correct name")
        #3)
        self.assertTrue("Singular" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Singular is missing as a possible computer algebra system\
 solving GB_Fp_dp")
        self.assertTrue("Magma" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Magma is missing as a possible computer algebra system\
 solving GB_Fp_dp")
        self.assertTrue("GAP" in compProblem.getPossibleComputerAlgebraSystems(),
                        "GAP is missing as a possible computer algebra system\
 solving GB_Fp_dp")
        self.assertTrue("Maple" in compProblem.getPossibleComputerAlgebraSystems(),
                        "Maple is missing as a possible computer algebra system\
 solving GB_Fp_dp")
        #4)
        temp = copy.deepcopy(compProblem.getAssociatedTables())
        compProblem.addToAssociatedTables(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getAssociatedTables()),
                    "Adding of an existing table to the associated tables of GB_Fp_dp\
 caused the list of associated tables to change.")
        #5)
        compProblem.addToAssociatedTables("RandomTableNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getAssociatedTables()),
                            "Adding of associated table to GB_Fp_dp failed.")
        #6)
        temp = copy.deepcopy(compProblem.getPossibleComputerAlgebraSystems())
        compProblem.addToComputerAlgebraSystems(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                    "Adding of an existing table to the possible computer algebra systems of GB_Fp_dp\
 caused the list of associated tables to change.")
        #7)
        compProblem.addToComputerAlgebraSystems("RandomCASNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                            "Adding of computer algebra system to GB_Fp_dp failed.")
        

    def test_SOL_R_poly_sys(self):
        """
        This test tests the class SOL_R_poly_sys for its stability.

        The covered tests are:
        1) IntPS is contained in the associated table list
        2) The name is SOL_R_poly_sys
        3) adding of an existing associated table does not change the table
        4) adding a non existing associated table works fine
        5) adding a non existing computer algebra system works fine
        6) adding an existing computer algebra system does not change the table
        """
        #1)
        compProblem=SOL_R_poly_sys.SOL_R_poly_sys()
        self.assertTrue("IntPS" in compProblem.getAssociatedTables(),
                        "The standard table, \"IntPS\", was not contained \
in the class SOL_R_poly_sys")
        #2)
        self.assertEqual("SOL_R_poly_sys", compProblem.getName(), "The class SOL_R_poly_sys does not\
 return a correct name")
        #3)
        temp = copy.deepcopy(compProblem.getAssociatedTables())
        compProblem.addToAssociatedTables(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getAssociatedTables()),
                    "Adding of an existing table to the associated tables of SOL_R_poly_sys\
 caused the list of associated tables to change.")
        #4)
        compProblem.addToAssociatedTables("RandomTableNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getAssociatedTables()),
                            "Adding of associated table to SOL_R_poly_sys failed.")
        #5)
        temp = copy.deepcopy(compProblem.getPossibleComputerAlgebraSystems())
        compProblem.addToComputerAlgebraSystems("RandomCASNeverWouldExistsBecauseOfSillyName")
        self.assertFalse(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                            "Adding of computer algebra system to GB_Fp_dp failed.")
        #6)
        temp = copy.deepcopy(compProblem.getPossibleComputerAlgebraSystems())
        compProblem.addToComputerAlgebraSystems(temp[0])
        self.assertTrue(set(temp)==set(compProblem.getPossibleComputerAlgebraSystems()),
                    "Adding of an existing table to the possible computer algebra systems of GB_Fp_dp\
 caused the list of associated tables to change.")

if __name__=="__main__":
    unittest.main()
