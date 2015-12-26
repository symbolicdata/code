import unittest
from TaskFolder import TaskFolder
from Task import Task
from TaskFolderTree import TaskFolderTree
from MachineSettings import MachineSettings


class TestTaskFolder(unittest.TestCase):
    """
    Tests for the class TaskFolder

    .. moduleauthor:: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def setUp(self):
        testName = "PrettyTestTask"
        testComputationProblem = "PrettierComputationProblem"
        testSDTables = ["sdtable1", "sdtable2"]
        testPIs = ["PI1", "PI2", "PI3", "PI4"]
        testCASs = ["Singular", "Magma", "Maple"]
        self.testTask = Task(testName, testComputationProblem, testSDTables, testPIs, testCASs)
        casDict = {"Singular":"Singular", "Magma":"magma", "Maple":"maple"}
        timeCommand = "time -p"
        self.msTest = MachineSettings(casDict,timeCommand)
        self.tfTree = TaskFolderTree()
        for a in testSDTables:
            for b in testPIs:
                for c in testCASs:
                    self.tfTree.addCode(a,b,c,"/*Test Code*/")

    def testTaskFolder(self):
        """
        Here, we test the functionality of the TaskFolder Class
        Tests include:
        1. Initialization of the TaskFolder Class
           1.a. A test, that initializes the taskFolder with None for all values.
           1.b. A test, that the entries inside of the taskfoldertree coincide with the values that
                can be found in the task-instance, which is given to the function.
           1.c Correct initialization of the TaskFolder instance.
        """
        #1.a
        testVar =0
        try:
            tf = TaskFolder(None,None,None)
            testVar = 1
        except:
            pass
        if (testVar==1):
            self.fail("I was able to initialize a TaskFolder instance with lots of None's as input")
        #1.b
        try:
            tf = TaskFolder(self.testTask, self.tfTree, TaskFolderTree())
            testVar =1
        except:
            pass
        if testVar == 1:
            self.fail("Could initialize the a Taskfolder with not consistent input.")
        #1.c
        try:
            tf = TaskFolder(self.testTask, self.tfTree, self.msTest)
        except:
            self.fail("Could not initialize correct Initialization of tfTree.")
        

if __name__=="__main__":
    unittest.main()

