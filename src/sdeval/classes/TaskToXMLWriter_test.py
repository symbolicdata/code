import unittest
from Task import Task
from TaskToXMLWriter import TaskToXMLWriter
from XMLResources import XMLResources

class TestTaskToXMLWriter(unittest.TestCase):
    """
    Tests for the class TaskToXMLWriter

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def setUp(self):
        self.xmlres = XMLResources()
        testName = "PrettyTestTask"
        testComputationProblem = "GB_Z_lp"
        testSDTables = ["IntPS"]
        testPIs = ["Amrhein", "Becker-Niermann", "Bronstein-86"]
        testCASs = ["Singular", "Magma", "Maple"]
        self.testTask = Task(testName, testComputationProblem, testSDTables, testPIs, testCASs)

    def testCreation(self):
        """
        The following test takes a sample task instance and checks if the xml representation is
        correct.
        """
        ttxw = TaskToXMLWriter()
        xmlRep = ttxw.createXMLFromTask(self.testTask, self.xmlres)
        s = xmlRep.toxml()
        expectedString = """<?xml version="1.0" ?><task><name>PrettyTestTask</name><computationproblem>GB_Z_lp</computationproblem><computeralgebrasystems><computeralgebrasystem>Singular</computeralgebrasystem><computeralgebrasystem>Magma</computeralgebrasystem><computeralgebrasystem>Maple</computeralgebrasystem></computeralgebrasystems><sdtables><sdtable><tablename>IntPS</tablename><probleminstances><probleminstance>Amrhein</probleminstance><probleminstance>Becker-Niermann</probleminstance><probleminstance>Bronstein-86</probleminstance></probleminstances></sdtable></sdtables></task>"""
        self.assertEqual(s,expectedString, "Test failed. Did not write the correct representation of the Task.")
        
if __name__=="__main__":
    unittest.main()
