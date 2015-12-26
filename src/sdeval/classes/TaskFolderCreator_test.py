import unittest
from Task import Task
from XMLResources import XMLResources
from MachineSettings import MachineSettings
from TaskFolderCreator import TaskFolderCreator

class TestTaskFolderCreator(unittest.TestCase):
    """
    Tests for the class TaskFolderCreator

    .. moduleauthor:: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def setUp(self):
        testName = "PrettyTestTask"
        testComputationProblem = "GB_Z_lp"
        testSDTables = ["IntPS"]
        testPIs = ["Amrhein", "Becker-Niermann", "Bronstein-86"]
        testCASs = ["Singular", "Magma", "Maple"]
        self.testTask = Task(testName, testComputationProblem, testSDTables, testPIs, testCASs)
        self.testXMLResources = XMLResources()
        casDict = {"Singular":"Singular", "Magma":"magma", "Maple":"maple"}
        timeCommand = "time -p"
        self.msTest = MachineSettings(casDict,timeCommand)

    def test_TaskFolderCreator(self):
        """
        This test covers the basic functionality of TaskFolderCreator.

        It covers the following testCases:
        1. call TaskFolderCreator.create with invalid arguments
           1.a: None for all values
           1.b: An integer value for all imputs
        2. call TaskFolderCreator.create with a Non-existent computation problem
        3. call TaskFolderCreator.create with a computer algebra system, that does not exist
        4. call TaskfolderCreator.create with valid values and check the result.
        """
        testPassed = 1
        #1.a
        self.assertEqual(TaskFolderCreator().create(None,None,None),None,
            "Could build TaskFolder with None for all arguments in TaskFolderCreator.")
        #1.b
        self.assertEqual(TaskFolderCreator().create(1,1,1),None,
            "Could build TaskFolder with an integer value for all arguments in TaskFolderCreator.")
        #2
        testName = "PrettyTestTaskFail"
        testComputationProblem = "asdkflgaljsdgkasdfkh"
        testSDTables = ["IntPS"]
        testPIs = ["Amrhein", "Becker-Niermann", "Bronstein-86"]
        testCASs = ["Singular", "Magma", "Maple"]
        testTaskFail = Task(testName, testComputationProblem, testSDTables, testPIs, testCASs)
        try:
            TaskFolderCreator().create(testTaskFail, self.testXMLResources, self.msTest)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could create task with a non-valid computation-problem")
        #3
        testCASs = testCASs + ["dsakglhkjlasdhgjklahsdflkl"]
        testComputationProblem = "GB_Z_lp"
        testTaskFail = Task(testName, testComputationProblem, testSDTables, testPIs, testCASs)
        try:
            TaskFolderCreator().create(testTaskFail, self.testXMLResources, self.msTest)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could create TaskFolder with non-existent computer algebra system template")
        #4.
        try:
            successfulCreation = TaskFolderCreator().create(self.testTask, self.testXMLResources, self.msTest)
        except:
            self.fail("Could not create TaskFolder with valid entries")
        if (successfulCreation == None):
            self.fail("TaskFolder with valid entries turned out to be None value")
        if (successfulCreation.getTask() != self.testTask):
            self.fail("The Task in the TaskFolder is wrong")
        if (successfulCreation.getMachineSettings() != self.msTest):
            self.fail("The MachineSettings in the Taskfolder are not correct")
        #empirical test of the code
        getTree = successfulCreation.getExecFiles().getAllPaths()
        if len(getTree)!=9:
            self.fail("Wrong number of files in the encoded TaskFolderTree")
        if (filter(lambda x: x[1]=="Amrhein" and x[2]=="Singular",getTree) == []):
            self.fail("One instance with a certain computer algebra system was not loaded.")

if __name__=="__main__":
    unittest.main()
