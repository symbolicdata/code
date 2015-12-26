import unittest
import Task

class TestTask(unittest.TestCase):
    """
    Tests for the class Task

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def setUp(self):
        self.testName = "PrettyTestTask"
        self.testComputationProblem = "PrettierComputationProblem"
        self.testSDTables = ["sdtable1", "sdtable2", "sdtable3", "sdtable4"]
        self.testPIs = ["PI1", "PI2", "PI3", "PI4"]
        self.testCASs = ["cas1", "cas2", "cas3", "cas4"]
        self.testTask = Task.Task(self.testName, self.testComputationProblem, self.testSDTables, self.testPIs, self.testCASs)

    def testInitialization(self):
        """
        This test checks whether the constructor of Task works well or not.
        Specifically, the following cases are tested:

        1) Invalid name, i.e. empty or just whitespaces
        2) invalid computationProblem, i.e. empty or just whitespaces
        3) An empty list of SDTables
        4) An empty list of ProblemInstances, rest fine
        5) An empty list of computeralgebrasystems, rest fine
        """
        testPassed = 1
        #1)
        try:
            Task.Task("", self.testComputationProblem, self.testSDTables, self.testPIs, self.testCASs)
            testPassed = 0
        except:
            pass
        if (testPassed ==0):
            self.fail("Could make an instance of Task with an empty name.")
        try:
            Task.Task(" \t\n", self.testComputationProblem, self.testSDTables, self.testPIs, self.testCASs)
            testPassed = 0
        except:
            pass
        if (testPassed ==0):
            self.fail("Could create an instance of task whose name consists of whitespaces")
        #2)
        try:
            Task.Task(self.testName, "", self.testSDTables, self.testPIs, self.testCASs)
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could make an instance of Task with an empty name.")
        try:
            Task.Task(self.testName," \t\n", self.testSDTables, self.testPIs, self.testCASs)
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could make an instance of Task with an empty name.")
        #3)
        try:
            Task.Task(self.testName, self.testComputationProblem, [], self.testPIs, self.testCASs)
            testPassed = 0
        except:
            pass
        if (testPassed ==0):
            self.fail("Could make an instance of Task with an empty name.")
        #4)
        try:
            Task.Task(self.testName, self.testComputationProblem, self.testSDTables, [], self.testCASs)
            testPassed =0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could make an instance of Task with an empty name.")
        #5)
        try:
            Task.Task(self.testName, self.testComputationProblem, self.testSDTables, self.testPIs, [])
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could make an instance of Task with an empty name.")

    def testGetters(self):
        """
        Tests the following "getter" functions of the class TASK:
         - getComputationProblem
         - getName
         - getAssociatedSDTables
         - getProblemInstances
         - getComputerAlgebrasystems
        """
        self.assertTrue(self.testTask.getComputationProblem()=="PrettierComputationProblem",
                        "The name of the computationproblem was not correct")
        self.assertTrue(self.testTask.getName() == "PrettyTestTask",
                        "The name of the task was not correct")
        self.assertTrue(self.testTask.getAssociatedSDTables() == ["sdtable1", "sdtable2", "sdtable3", "sdtable4"],
                        "Associated SD Tables were not returned correctly")
        self.assertTrue(self.testTask.getProblemInstances() ==  ["PI1", "PI2", "PI3", "PI4"],
                        "Associated problem instances were not listed correctly")
        self.assertTrue(self.testTask.getComputerAlgebraSystems() == ["cas1", "cas2", "cas3", "cas4"])

    def testStringRepresentation(self):
        """
        Tests the string representation of an instance of the class Task.
        """
        expectedOutput = "Task:PrettyTestTask\n\
Associated computation problem: PrettierComputationProblem\n\
Associated SD-Tables:\n\
sdtable1\n\
sdtable2\n\
sdtable3\n\
sdtable4\n\
Problem instances:\n\
PI1\n\
PI2\n\
PI3\n\
PI4\n\
Chosen computer algebra systems:\n\
cas1\n\
cas2\n\
cas3\n\
cas4"
        self.assertEqual(str(self.testTask), expectedOutput,
                    "String representation of our test instance of Task was not correct")


if __name__=="__main__":
    unittest.main()
