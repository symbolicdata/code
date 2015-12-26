import unittest
from RunTaskOptionsFromXMLBuilder import RunTaskOptionsFromXMLBuilder

class TestRunTaskOptions(unittest.TestCase):
    """
    Tests for the class RunTaskOptionsFromXMLBuilder

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """
    def setUp(self):
        #InvalidXMLfile
        self.xml1 = "abc123"
        #Empty XML file
        self.xml2 = ""
        #Tag is missing completely
        self.xml3 = """<?xml version="1.0" ?><RunTaskOptions><maxMem>1024</maxMem><maxJobs>8</maxJobs><resume>0</resume></RunTaskOptions>"""
        #Tags have non-valid entries
        self.xml4 = """<?xml version="1.0" ?><RunTaskOptions><maxCPU>abc</maxCPU><maxMem>cde</maxMem><maxJobs>efg</maxJobs><resume>0</resume></RunTaskOptions>"""
        #XML with some empty tags
        self.xml5 = """<?xml version="1.0" ?><RunTaskOptions><maxCPU></maxCPU><maxMem/><maxJobs>1</maxJobs><resume>0</resume></RunTaskOptions>"""
        #XML with all tags validly set
        self.xml6 = """<?xml version="1.0" ?><RunTaskOptions><maxCPU>7200</maxCPU><maxMem>1024</maxMem><maxJobs>8</maxJobs><resume>1</resume></RunTaskOptions>"""

    def test_XMLBuilder(self):
        """
        This function covers the following test cases:
        1. Try to parse an invalid XML file
        2. Try to parse the empty string
        3. Try to parse a string, where one tag is missing completely
        4. Try to parse a string with non-valid entries at all
        5. Try to parse a string with some empty tags
        6. Try to parse a string with all tags validly set
        """
        builder = RunTaskOptionsFromXMLBuilder()
        testPassed = True
        #Test 1
        try:
            tobj = builder.build(self.xml1)
            testPassed = False
        except:
            pass
        if testPassed == False:
            self.fail("Test 1. failed. Could build the following RunTaksOptions instance: %s"%str(tobj))
        #2
        try:
            tobj = builder.build(self.xml2)
            testPassed = False
        except:
            pass
        if testPassed == False:
            self.fail("Test 2. failed. Could build the following RunTaksOptions instance: %s"%str(tobj))
        #3
        try:
            tobj = builder.build(self.xml3)
            testPassed = False
        except:
            pass
        if testPassed == False:
            self.fail("Test 3. failed. Could build the following RunTaksOptions instance: %s"%str(tobj))
        #4
        try:
            tobj = builder.build(self.xml4)
            testPassed = False
        except:
            pass
        if testPassed == False:
            self.fail("Test 4. failed. Could build the following RunTaksOptions instance: %s"%str(tobj))
        #5.
        tobj = builder.build(self.xml5)
        self.assertEqual(tobj.getMaxMem(),None, "Test 5. failed. Expected None as maxMem, but got: %s"%str(tobj.getMaxMem()))
        self.assertEqual(tobj.getMaxCPU(),None, "Test 5. failed. Expected None as maxCPU, but got: %s"%str(tobj.getMaxCPU()))
        self.assertEqual(tobj.getMaxJobs(),1, "Test 5. failed. Expected 1 for maxJobs, but got: %s"%str(tobj.getMaxJobs()))
        self.assertEqual(tobj.getResume(),0,"Test 5. failed. Expeced 0 for resume, but got: %s"%str(tobj.getResume()))
        #6.
        tobj = builder.build(self.xml6)
        self.assertEqual(tobj.getMaxMem(),1024, "Test 6. failed. Expected 1024 as maxMem, but got: %s"%str(tobj.getMaxMem()))
        self.assertEqual(tobj.getMaxCPU(),7200, "Test 6. failed. Expected 7200 as maxCPU, but got: %s"%str(tobj.getMaxCPU()))
        self.assertEqual(tobj.getMaxJobs(),8, "Test 6. failed. Expected 8 for maxJobs, but got: %s"%str(tobj.getMaxJobs()))
        self.assertEqual(tobj.getResume(),1,"Test 6. failed. Expeced 1 for resume, but got: %s"%str(tobj.getResume()))

if __name__=="__main__":
    unittest.main()
