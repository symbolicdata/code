import unittest
from RunTaskOptions import RunTaskOptions
from RunTaskOptionsToXMLWriter import RunTaskOptionsToXMLWriter

class TestRunTaskOptionsToXMLWriter(unittest.TestCase):
    """
    Tests for the class RunTaskOptionsToXMLWriter.

    .. moduleauthor:: Albert Heinle<aheinle@uwaterloo.ca>
    """

    def testXMLRep(self):
        """
        This test creates a RunTaskOption instance and checks if the XML representation is correct.
        1. All values are set
        2. Some None-values
           2.a maxCPU=None
           2.b maxMem=None
        """
        #1.
        rto = RunTaskOptions(7200,1024,8, resume=True)
        rtowriter = RunTaskOptionsToXMLWriter()
        s = rtowriter.createXMLFromRunTaskOptions(rto).toxml()
        expectedString = """<?xml version="1.0" ?><RunTaskOptions><maxCPU>7200</maxCPU><maxMem>1024</maxMem><maxJobs>8</maxJobs><resume>1</resume></RunTaskOptions>"""
        self.assertEqual(s,expectedString, "Test 1. failed. String representation not as expected, but: %s"%s)
        #2.a
        rto = RunTaskOptions(None,1024,8)
        rtowriter = RunTaskOptionsToXMLWriter()
        s = rtowriter.createXMLFromRunTaskOptions(rto).toxml()
        expectedString = """<?xml version="1.0" ?><RunTaskOptions><maxCPU/><maxMem>1024</maxMem><maxJobs>8</maxJobs><resume>0</resume></RunTaskOptions>"""
        self.assertEqual(s,expectedString, "Test 2.a failed. String representation not as expected, but: %s"%s)
        #2.b
        rto = RunTaskOptions(3600,None,8)
        rtowriter = RunTaskOptionsToXMLWriter()
        s = rtowriter.createXMLFromRunTaskOptions(rto).toxml()
        expectedString = """<?xml version="1.0" ?><RunTaskOptions><maxCPU>3600</maxCPU><maxMem/><maxJobs>8</maxJobs><resume>0</resume></RunTaskOptions>"""
        self.assertEqual(s,expectedString, "Test 2.b failed. String representation not as expected, but: %s"%s)

if __name__=="__main__":
    unittest.main()
