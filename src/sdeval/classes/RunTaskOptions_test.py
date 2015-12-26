import unittest
from RunTaskOptions import RunTaskOptions

class TestRunTaskOptions(unittest.TestCase):
    """
    Tests for the class RunTaskOptions

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def testInitialization(self):
        """
        This class tests the initialization of the RunTaskOptions class.
        In particular, the following test cases are covered:
        1. Initialization without any parameters (i.e. defaults values should be in)
        2. Initialization with maxCPU=None, but everything else set
        3. Initialization with maxMemory=None, but everything else is set
        4. Initialization with maxJobs=None, but everything else is set.
        5. Initialization with all values set.
        6. Invalid values:
           6.a. For maxCPU
           6.b. For maxMem
           6.c. For maxJobs
           6.d. for resume
        7. Initialize with all values, set the `resume` flag new, and then check if the value has been correctly set.
           7.a. the resume flag has an incorrect type
           7.b. the resume flag is correctly typed
        """
        #1.
        t = RunTaskOptions()
        self.assertEqual(t.getMaxMem(), None, "Test 1. failed: maxMem should be None, but instead we have: %s"%str(t.getMaxMem()))
        self.assertEqual(t.getMaxCPU(), None, "Test 1. failed: maxCPU should be None, but instead we have: %s"%str(t.getMaxCPU()))
        self.assertEqual(t.getMaxJobs(), 1, "Test 1. failed: maxJobs should be 1, but instead we have: %s"%str(t.getMaxJobs()))
        self.assertEqual(t.getResume(), False, "Test 1. failed: resume should be False, but instead we have: %s"%str(t.getResume))
        #2.
        t = RunTaskOptions(maxMem=1024,maxJobs=4)
        self.assertEqual(t.getMaxMem(), 1024, "Test 2. failed: maxMem should be 1024, but instead we have: %s"%str(t.getMaxMem()))
        self.assertEqual(t.getMaxCPU(), None, "Test 2. failed: maxCPU should be None, but instead we have: %s"%str(t.getMaxCPU()))
        self.assertEqual(t.getMaxJobs(), 4, "Test 2. failed: maxJobs should be 4, but instead we have: %s"%str(t.getMaxJobs()))
        self.assertEqual(t.getResume(), False, "Test 2. failed: resume should be False, but instead we have: %s"%str(t.getResume))
        #3.
        t = RunTaskOptions(maxCPU=7200,maxJobs=6)
        self.assertEqual(t.getMaxMem(), None, "Test 3. failed: maxMem should be 1024, but instead we have: %s"%str(t.getMaxMem()))
        self.assertEqual(t.getMaxCPU(), 7200, "Test 3. failed: maxCPU should be None, but instead we have: %s"%str(t.getMaxCPU()))
        self.assertEqual(t.getMaxJobs(), 6, "Test 3. failed: maxJobs should be 4, but instead we have: %s"%str(t.getMaxJobs()))
        self.assertEqual(t.getResume(), False, "Test 3. failed: resume should be False, but instead we have: %s"%str(t.getResume))
        #4.
        t = RunTaskOptions(maxCPU=7200,maxMem=128)
        self.assertEqual(t.getMaxMem(), 128, "Test 4. failed: maxMem should be 1024, but instead we have: %s"%str(t.getMaxMem()))
        self.assertEqual(t.getMaxCPU(), 7200, "Test 4. failed: maxCPU should be None, but instead we have: %s"%str(t.getMaxCPU()))
        self.assertEqual(t.getMaxJobs(), 1, "Test 4. failed: maxJobs should be 4, but instead we have: %s"%str(t.getMaxJobs()))
        self.assertEqual(t.getResume(), False, "Test 4. failed: resume should be False, but instead we have: %s"%str(t.getResume))        
        #5.
        t = RunTaskOptions(maxCPU=7200,maxMem=256,maxJobs=2, resume = True)
        self.assertEqual(t.getMaxMem(), 256, "Test 5. failed: maxMem should be 1024, but instead we have: %s"%str(t.getMaxMem()))
        self.assertEqual(t.getMaxCPU(), 7200, "Test 5. failed: maxCPU should be None, but instead we have: %s"%str(t.getMaxCPU()))
        self.assertEqual(t.getMaxJobs(), 2, "Test 5. failed: maxJobs should be 4, but instead we have: %s"%str(t.getMaxJobs()))
        self.assertEqual(t.getResume(), True, "Test 5. failed: resume should be True, but instead we have: %s"%str(t.getResume))
        #6a.
        testPassed = True
        try:
            t = RunTaskOptions(maxCPU=-1,maxMem=256,maxJobs=2)
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 6.a. failed: Was able to assign -1 to maxCPU.")
        #6b.
        try:
            t = RunTaskOptions(maxCPU=10,maxMem=0,maxJobs=2)
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 6.b. failed: Was able to assign -1 to maxMem.")
        #6c.
        try:
            t = RunTaskOptions(maxCPU=10,maxMem=10,maxJobs=-10000)
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 6.c. failed: Was able to assign -10000 to maxJobs.")
        #6d.
        try:
            t = RunTaskOptions(maxCPU=10, maxMem=10, maxJobs=2, resume="abc123")
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 6.d. failed: Was able to assign 'abc123' to resume.")
        #7a.
        try:
            t = RunTaskOptions(maxCPU=7200,maxMem=256,maxJobs=2, resume = True)
            t.setResume("abc")
            testPassed = False
        except:
            pass
        if not testPassed:
            self.fail("Test 7.a failed. Could assign something completely invalid to resume via setResume function.")
        #7b.
        t = RunTaskOptions(maxCPU=7200,maxMem=256,maxJobs=2, resume = True)
        t.setResume(False)
        self.assertEqual(t.getMaxMem(), 256, "Test 7b. failed: maxMem should be 1024, but instead we have: %s"%str(t.getMaxMem()))
        self.assertEqual(t.getMaxCPU(), 7200, "Test 7b. failed: maxCPU should be None, but instead we have: %s"%str(t.getMaxCPU()))
        self.assertEqual(t.getMaxJobs(), 2, "Test 7b. failed: maxJobs should be 4, but instead we have: %s"%str(t.getMaxJobs()))
        self.assertEqual(t.getResume(), False, "Test 7b. failed: resume should be False, but instead we have: %s"%str(t.getResume))
        


    def testStringRepresentation(self):
        """
        The tests in this function examine the string representation functionality
        of the RunTaskOptionFile. The tests covered are the following:

        1. Initialization without any parameters
        2. Initialize only maxMem
        3. Initialize only maxCPU
        4. Initialize all the values
        """
        #1
        t = RunTaskOptions()
        expectedString = """RunTask Options:
* Maximum CPU time for each computation (in seconds): N.A.
* Maximum memory consumption for each computation (in Bytes): N.A.
* Maximum amount of computations that can be run in parallel: 1
* Task has been interrupted before and is now being resumed: False"""
        self.assertEqual(str(t),expectedString, "Test 1. failed: The string representation did not coincide with the expected one: %s"%str(t))
        #2
        t = RunTaskOptions(maxMem=128)
        expectedString = """RunTask Options:
* Maximum CPU time for each computation (in seconds): N.A.
* Maximum memory consumption for each computation (in Bytes): 128
* Maximum amount of computations that can be run in parallel: 1
* Task has been interrupted before and is now being resumed: False"""
        self.assertEqual(str(t),expectedString, "Test 2. failed: The string representation did not coincide with the expected one: %s"%str(t))
        #3
        t = RunTaskOptions(maxCPU=120)
        expectedString = """RunTask Options:
* Maximum CPU time for each computation (in seconds): 120
* Maximum memory consumption for each computation (in Bytes): N.A.
* Maximum amount of computations that can be run in parallel: 1
* Task has been interrupted before and is now being resumed: False"""
        self.assertEqual(str(t),expectedString, "Test 3. failed: The string representation did not coincide with the expected one: %s"%str(t))
        #4
        t = RunTaskOptions(maxCPU=120, maxMem=128, maxJobs = 16, resume = True)
        expectedString = """RunTask Options:
* Maximum CPU time for each computation (in seconds): 120
* Maximum memory consumption for each computation (in Bytes): 128
* Maximum amount of computations that can be run in parallel: 16
* Task has been interrupted before and is now being resumed: True"""
        self.assertEqual(str(t),expectedString, "Test 3. failed: The string representation did not coincide with the expected one: %s"%str(t))


if __name__=="__main__":
    unittest.main()
