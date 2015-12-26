import unittest
from ResultedTimingsFromXMLBuilder import ResultedTimingsFromXMLBuilder
from ..Task import Task

class TestResultedTimingsFromXMLBuilder(unittest.TestCase):
    """
    Tests for the class ResultedTimingsFromXMLBuilder

    .. moduleauthor:: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def setUp(self):
        #First, define the task we are working with
        testName = "PrettyTestTask"
        testComputationProblem = "PrettierComputationProblem"
        testSDTables = ["sdtable1", "sdtable2", "sdtable3", "sdtable4"]
        testPIs = ["PI1", "PI2"]
        testCASs = ["cas1", "cas2"]
        #self.resultedTimings1 = {"real":0.0, "user":0.0, "sys":0.0}
        #self.resultedTimings2 = {"real":8.143, "user":3.33, "sys":2.28}
        self.testTask = Task(testName, testComputationProblem, testSDTables, testPIs, testCASs)
        #Now, we give some sample XML strings
        #totally invalid XML:
        self.xml1 = "bla bli blubb"
        #valid xml, but nothing useful for us:
        self.xml2 = """<?xml version="1.0" ?><RunTaskOptions><maxCPU>7200</maxCPU><maxMem>1024</maxMem><maxJobs>8</maxJobs></RunTaskOptions>"""
        #Valid xml, but not valid entries in the completed or erroneous section
        self.xml3= """<?xml version="1.0" ?>
        <proceedings>
            <timestamp>
              123456
            </timestamp>
            <task>
              PrettyTestTask
            </task>
            <running/>
            <waiting>
              "same as running"
            </waiting>
            <completed>
              <entry>
              </entry>
            </completed>
            <error>
              <entry>
              </entry>
            </error>
          </proceedings>
        """
        #completely valid ResultedTimings xml file, no entries for erroneous  or complete stuff.
        self.xml4 = """<?xml version="1.0" ?>
        <proceedings>
            <timestamp>
              123456
            </timestamp>
            <task>
              PrettyTestTask
            </task>
            <running/>
            <waiting>
              <entry>
                <probleminstance>
                  PI1
                </probleminstance>
                <computeralgebrasystem>
                  cas1
                </computeralgebrasystem>
              </entry>
              <entry>
                <probleminstance>
                  PI2
                </probleminstance>
                <computeralgebrasystem>
                  cas1
                </computeralgebrasystem>
              </entry>
              <entry>
                <probleminstance>
                  PI1
                </probleminstance>
                <computeralgebrasystem>
                  cas2
                </computeralgebrasystem>
              </entry>
              <entry>
                <probleminstance>
                  PI2
                </probleminstance>
                <computeralgebrasystem>
                  cas2
                </computeralgebrasystem>
              </entry>
            </waiting>
            <completed/>
            <error/>
          </proceedings>
        """
        #Completely valid ResultedTimings XML file, erroneous and complete stuff not empty, but no timings provided
        self.xml5 = """<?xml version="1.0" ?>
        <proceedings>
            <timestamp>
              123456
            </timestamp>
            <task>
              PrettyTestTask
            </task>
            <running/>
            <waiting>
              <entry>
                <probleminstance>
                  PI1
                </probleminstance>
                <computeralgebrasystem>
                  cas1
                </computeralgebrasystem>
              </entry>
              <entry>
                <probleminstance>
                  PI2
                </probleminstance>
                <computeralgebrasystem>
                  cas1
                </computeralgebrasystem>
              </entry>
            </waiting>
            <completed>
              <entry>
                <probleminstance>
                  PI2
                </probleminstance>
                <computeralgebrasystem>
                  cas2
                </computeralgebrasystem>
              </entry>
            </completed>
            <error>
              <entry>
                <probleminstance>
                  PI1
                </probleminstance>
                <computeralgebrasystem>
                  cas2
                </computeralgebrasystem>
              </entry>
            </error>
          </proceedings>
        """
        #Completely valid ResultedTimings XML file, erroneous and complete stuff not empty, but no timings provided
        self.xml6 = """<?xml version="1.0" ?>
        <proceedings>
            <timestamp>
              123456
            </timestamp>
            <task>
              PrettyTestTask
            </task>
            <running/>
            <waiting>
              <entry>
                <probleminstance>
                  PI1
                </probleminstance>
                <computeralgebrasystem>
                  cas1
                </computeralgebrasystem>
              </entry>
              <entry>
                <probleminstance>
                  PI2
                </probleminstance>
                <computeralgebrasystem>
                  cas1
                </computeralgebrasystem>
              </entry>
            </waiting>
            <completed>
              <entry>
                <probleminstance>
                  PI2
                </probleminstance>
                <computeralgebrasystem>
                  cas2
                </computeralgebrasystem>
                <timings>
                  <real>
                    20.52
                  </real>
                  <user>
                    6.80
                  </user>
                  <sys>
                    2.81
                  </sys>
                </timings>
              </entry>
            </completed>
            <error>
              <entry>
                <probleminstance>
                  PI1
                </probleminstance>
                <computeralgebrasystem>
                  cas2
                </computeralgebrasystem>
                <timings>
                  <real>
                    8.143
                  </real>
                  <user>
                    3.33
                  </user>
                  <sys>
                    2.28
                  </sys>
                </timings>
              </entry>
            </error>
          </proceedings>
        """

    def testResultedTimingsFromXMLBuilder(self):
        """
        Testing the ResultedTimingsFromXMLBuilder class. The tests include the following:
        1. Entering a string that cannot be parsed as XML
        2. Entering a valid XML string, but not coming from ResultedTimings.
        3. Entering a valid XML string, but the form is not as expected.
        4. Entering a valid XML string, with no erroneous or completed tasks
        5. Entering a valid XML string with erroneous and completed tasks, but no timings given.
        6. Entering a valid XML string with valid erroneous and completed tasks.
        """
        prBuilder = ResultedTimingsFromXMLBuilder()
        testsSucceeded = True
        #1.
        try:
            prBuilder.build(self.xml1, self.testTask)
            testsSucceeded = False
        except:
            pass
        if not testsSucceeded:
            self.fail("Test 1. failed. I was able to parse invalid XML string")
        #2.
        try:
            prBuilder.build(self.xml2, self.testTask)
            testsSucceeded = False
        except:
            pass
        if not testsSucceeded:
            self.fail("Test 2. failed. I was able to parse XML string that does not represent ResultedTimings.")
        #3.
        try:
            prBuilder.build(self.xml3, self.testTask)
            testsSucceeded = False
        except:
            pass
        if not testsSucceeded:
            self.fail("Test 3. failed. I was able to parse an XML string representing ResultedTimings, but some\
 entries were not valid.")
        #4.
        tempPRC = prBuilder.build(self.xml4, self.testTask)
        self.assertEqual([],tempPRC.getCOMPLETED(),"Test 4. failed: No completed tasks in the list, but\
 completed tasks were outputted: %s"%str(tempPRC.getCOMPLETED()))
        self.assertEqual([],tempPRC.getERROR(),"Test 4. failed: No erroneous tasks in the list, but\
 erroneous tasks were outputted: %s"%str(tempPRC.getCOMPLETED()))
        self.assertEqual([["PI1","cas1",None],["PI1","cas2",None],["PI2","cas1",None],["PI2","cas2", None]],tempPRC.getWAITING(),
                         "Test 4. failed: Waiting list was not correct, but was: %s"%str(tempPRC.getWAITING()))
        #5.
        try:
            tempPRC = prBuilder.build(self.xml5, self.testTask)
            testsSucceeded = False
        except:
            pass
        if not testsSucceeded:
            self.fail("Test 5. failed. I was able to parse a ResultedTimings XML, where no timings were given\
 in the completed section.")
        #6.
        tempPRC = prBuilder.build(self.xml6, self.testTask)
        self.assertEqual([["PI2","cas2",{"real":"20.52","user":"6.80","sys":"2.81"}]],tempPRC.getCOMPLETED(),
                            "Test 6. failed: Something wrong with returned completed tasks: %s"%str(tempPRC.getCOMPLETED()))
        self.assertEqual([["PI1","cas2",{"real":"8.143","user":"3.33","sys":"2.28"}]],tempPRC.getERROR(),
                         "Test 6. failed: Something is wrong with returned erroneous tasks: %s"%str(tempPRC.getCOMPLETED()))
        self.assertEqual([["PI1","cas1",None],["PI2","cas1",None]],tempPRC.getWAITING(),
                         "Test 6. failed: Waiting list was not correct, but was: %s"%str(tempPRC.getWAITING()))

        
if __name__=="__main__":
    unittest.main()
