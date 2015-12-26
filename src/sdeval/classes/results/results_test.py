import unittest
from Proceedings import Proceedings
from ResultedTimings import ResultedTimings
from ProceedingsToHTMLWriter import ProceedingsToHTMLWriter
from ProceedingsToXMLWriter import ProceedingsToXMLWriter
from ResultedTimingsToHTMLWriter import ResultedTimingsToHTMLWriter
from ResultedTimingsToXMLWriter import ResultedTimingsToXMLWriter
from ResultingFile import ResultingFile
from ResultingFileFromOutputBuilder import ResultingFileFromOutputBuilder
from ..Task import Task

class TestProblemInstances(unittest.TestCase):
    """
    Contains tests for the results-files. These do the following
    - Keeping track of which processes are currently running, waiting, completed or raised an error.
    - If the tests completed, then the consumed time is produced.
    - Writing human readable HTML and machine-readable XML files for displaying the status.

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def setUp(self):
        """
        The setup for all the tests. We usually will need a Task-instance and a timestamp. Those are created here.
        """
        testName = "PrettyTestTask"
        testComputationProblem = "PrettierComputationProblem"
        testSDTables = ["sdtable1", "sdtable2", "sdtable3", "sdtable4"]
        testPIs = ["PI1", "PI2", "PI3", "PI4"]
        testCASs = ["cas1", "cas2", "cas3", "cas4"]
        self.testTask = Task(testName, testComputationProblem, testSDTables, testPIs, testCASs)
        self.testTimeStamp = "201405161350"

    def test_Proceedings(self):
        """
        This tests checks the correctness of the Proceedings class. The following tests are covered:
        1. Creation of Proceedings with None as the task (fail)
        2. Creation of Proceedings with an integer as task (fail)
        3. Creation of Proceedings with None as timestamp (fail)
        4. Creation of Proceedings with an integer as timestamp (fail)
        5. Correct initialization of the proceedings
           5.1. Test the initial set
           5.2. Test the getters
           5.3. Test setRunning with incorrect value
           5.4. Test setRunning with correct value
           5.5. Test setCompleted with incorrect value
           5.6. Test setCompleted with correct value
           5.7. Test setERROR with incorrect value
           5.8. Test setERROR with correct value.
        """
        #1.
        testPassed =1
        try:
            prcdngs = Proceedings(None, self.testTimeStamp)
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could create Proceedings with no Task")
        #2.
        try:
            prcdngs = Proceedings(1, self.testTimeStamp)
            testPassed = 0
        except:
            pass
        if (testPassed ==0):
            self.fail("Could create Proceedings with 1 as Task")
        #3.
        try:
            prcdngs = Proceedings(self.testTask, None)
            testPassed = 0
        except:
            pass
        if (testPassed==0):
            self.fail("Could create Proceedings with None as timestamp")
        #4.
        try:
            prcdngs = Proceedings(self.testTask, 1)
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could create Proceedings with 1 as timestamp")
        #5.
        prcdngs = Proceedings(self.testTask, self.testTimeStamp)
        #5.1
        self.assertEqual(len(prcdngs.getWAITING()),16,"Number of waiting processes was not correct")
        self.assertEqual(prcdngs.getRUNNING(),[],"Running processes initially wrong")
        self.assertEqual(prcdngs.getCOMPLETED(),[],"Completed processes initially wrong")
        self.assertEqual(prcdngs.getERROR(),[], "Erroneous processes initially wrong")
        #5.2
        self.assertEqual(prcdngs.getTask(), self.testTask.getName(), "Initialization with wrong task performed")
        self.assertEqual(prcdngs.getTimeStamp(), self.testTimeStamp, "Initialization with wrong timeStamp")
        #5.3
        prcdngs.setRUNNING("abc")
        self.assertEqual(len(prcdngs.getWAITING()),16,"invalid setRunning changed WAITING list.")
        self.assertEqual(prcdngs.getRUNNING(),[],"invalid setRunning changed RUNNING list.")
        self.assertEqual(prcdngs.getCOMPLETED(),[],"invalid setRunning changed COMPLETED list.")
        self.assertEqual(prcdngs.getERROR(),[], "invalid setRunning changed ERROR list.")
        #5.4
        prcdngs.setRUNNING(["PI1","cas1"])
        self.assertEqual(len(prcdngs.getWAITING()),15,"setRunning changed WAITING list wrongly.")
        self.assertEqual(prcdngs.getRUNNING(),[["PI1","cas1"]],"setRunning did not affect RUNNING list.")
        self.assertEqual(prcdngs.getCOMPLETED(),[],"setRunning changed COMPLETED list.")
        self.assertEqual(prcdngs.getERROR(),[], "setRunning changed ERROR list.")
        #5.5
        prcdngs.setCOMPLETED("abc")
        self.assertEqual(len(prcdngs.getWAITING()),15,"invalid setCompleted changed WAITING list wrongly.")
        self.assertEqual(prcdngs.getRUNNING(),[["PI1","cas1"]],"invalid setCompleted changed RUNNING list.")
        self.assertEqual(prcdngs.getCOMPLETED(),[],"invalid setCompleted changed COMPLETED list.")
        self.assertEqual(prcdngs.getERROR(),[], "invalid setCompleted changed ERROR list.")
        #5.6
        prcdngs.setCOMPLETED(["PI1","cas1"])
        self.assertEqual(len(prcdngs.getWAITING()),15,"setCompleted changed WAITING list.")
        self.assertEqual(prcdngs.getRUNNING(),[],"setCompleted changed RUNNING list wrongly.")
        self.assertEqual(prcdngs.getCOMPLETED(),[["PI1","cas1"]],"setCompleted did not change COMPLETED list.")
        self.assertEqual(prcdngs.getERROR(),[], "setCompleted changed ERROR list.")
        #5.7
        prcdngs.setERROR(["PI1","cas1"])
        self.assertEqual(len(prcdngs.getWAITING()),15,"invalid setERROR changed WAITING list.")
        self.assertEqual(prcdngs.getRUNNING(),[],"invalid setERROR changed RUNNING list.")
        self.assertEqual(prcdngs.getCOMPLETED(),[["PI1","cas1"]],"invalid setERROR changed COMPLETED list.")
        self.assertEqual(prcdngs.getERROR(),[], "invalid serERROR changed ERROR list.")
        #5.8
        prcdngs.setRUNNING(["PI2","cas1"])
        prcdngs.setERROR(["PI2", "cas1"])
        self.assertEqual(len(prcdngs.getWAITING()),14,"setERROR changed WAITING list.")
        self.assertEqual(prcdngs.getRUNNING(),[],"setERROR changed RUNNING list wrongly.")
        self.assertEqual(prcdngs.getCOMPLETED(),[["PI1","cas1"]],"setERROR changed COMPLETED list.")
        self.assertEqual(prcdngs.getERROR(),[["PI2", "cas1"]], "setERROR changed ERROR list wrongly.")
        
    def test_ResultedTimings(self):
        """
        This tests checks the correctness of the ResultedTimings class. The following tests are covered:
        1. Creation of ResultedTimings with None in every input part (fail)
        2. Creation of ResultedTimings with wrong Datatypes (fail)
           2.a) Proceedings integer value
           2.b) Task and/or timestamp integers
        3. Correct initialization of the ResultedTimings
           3.1. Test the initial set
           3.2. Test the getters
           3.3. Test setRunning with incorrect value
           3.4. Test setRunning with correct value
           3.5. Test setCompleted with incorrect value
           3.6. Test setCompleted with correct value
           3.7. Test setERROR with incorrect value
           3.8. Test setERROR with correct value.
        """
        testPassed = 1
        #1.
        try:
            rst = ResultedTimings(None,None,None)
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could create instance of ResultedTimings with None in all entries")
        #2.a
        try:
            rst = ResultedTimings(1)
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could create instance of ResultedTimings with Integer as associated Proceedings")
        #2.b
        try:
            rst = ResultedTimings(None, 1,1)
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could create ResultedTimings with wrong datatypes for task and timestamp")
        #3
        rst = ResultedTimings(None,self.testTask,self.testTimeStamp)
        #3.1
        self.assertEqual(len(rst.getWAITING()),16,"Number of waiting processes was not correct")
        self.assertEqual(rst.getRUNNING(),[],"Running processes initially wrong")
        self.assertEqual(rst.getCOMPLETED(),[],"Completed processes initially wrong")
        self.assertEqual(rst.getERROR(),[], "Erroneous processes initially wrong")
        #3.2
        self.assertEqual(rst.getTask(), self.testTask.getName(), "Initialization with wrong task performed")
        self.assertEqual(rst.getTimeStamp(), self.testTimeStamp, "Initialization with wrong timeStamp")
        self.assertEqual(rst.getResultingFileDict(),{}, "Initialization with wrong resultingFileDict")
        rst.setRUNNING("abc")
        self.assertEqual(len(rst.getWAITING()),16,"invalid setRunning changed WAITING list.")
        self.assertEqual(rst.getRUNNING(),[],"invalid setRunning changed RUNNING list.")
        self.assertEqual(rst.getCOMPLETED(),[],"invalid setRunning changed COMPLETED list.")
        self.assertEqual(rst.getERROR(),[], "invalid setRunning changed ERROR list.")
        #5.4
        rst.setRUNNING(["PI1","cas1"])
        self.assertEqual(len(rst.getWAITING()),15,"setRunning changed WAITING list wrongly.")
        self.assertEqual(rst.getRUNNING(),[["PI1","cas1", None]],"setRunning did not affect RUNNING list.")
        self.assertEqual(rst.getCOMPLETED(),[],"setRunning changed COMPLETED list.")
        self.assertEqual(rst.getERROR(),[], "setRunning changed ERROR list.")
        #5.5
        timingTemp = {"real":1.2, "user":1.3, "sys": 1.4}
        rst.setCOMPLETED("abc",timingTemp)
        self.assertEqual(len(rst.getWAITING()),15,"invalid setCompleted changed WAITING list wrongly.")
        self.assertEqual(rst.getRUNNING(),[["PI1","cas1",None]],"invalid setCompleted changed RUNNING list.")
        self.assertEqual(rst.getCOMPLETED(),[],"invalid setCompleted changed COMPLETED list.")
        self.assertEqual(rst.getERROR(),[], "invalid setCompleted changed ERROR list.")
        #5.6
        rst.setCOMPLETED(["PI1","cas1"],timingTemp)
        self.assertEqual(len(rst.getWAITING()),15,"setCompleted changed WAITING list.")
        self.assertEqual(rst.getRUNNING(),[],"setCompleted changed RUNNING list wrongly.")
        self.assertEqual(rst.getCOMPLETED(),[["PI1","cas1",timingTemp]],"setCompleted did not change COMPLETED list.")
        self.assertEqual(rst.getERROR(),[], "setCompleted changed ERROR list.")
        #5.7
        rst.setERROR(["PI1","cas1"], timingTemp)
        self.assertEqual(len(rst.getWAITING()),15,"invalid setERROR changed WAITING list.")
        self.assertEqual(rst.getRUNNING(),[],"invalid setERROR changed RUNNING list.")
        self.assertEqual(rst.getCOMPLETED(),[["PI1","cas1",timingTemp]],"invalid setERROR changed COMPLETED list.")
        self.assertEqual(rst.getERROR(),[], "invalid serERROR changed ERROR list.")
        #5.8
        rst.setRUNNING(["PI2","cas1", None])
        rst.setERROR(["PI2", "cas1"],timingTemp)
        self.assertEqual(len(rst.getWAITING()),14,"setERROR changed WAITING list.")
        self.assertEqual(rst.getRUNNING(),[],"setERROR changed RUNNING list wrongly.")
        self.assertEqual(rst.getCOMPLETED(),[["PI1","cas1",timingTemp]],"setERROR changed COMPLETED list.")
        self.assertEqual(rst.getERROR(),[["PI2", "cas1",timingTemp]], "setERROR changed ERROR list wrongly.")
        
    def test_ProceedingsToHTMLWriter(self):
        """
        Testing the correctness of the ProceedingsToHTMLWriter class.
        The following test cases are covered:
        1. Calling a ProceedingsToHTMLWriter with a wrong parameter
           1.a None
           1.b an integer value
        2. Calling the ProceedingsToHTMLWriter with a correct parameter
        """
        wrtr = ProceedingsToHTMLWriter()
        #1.a
        strRepresentation = wrtr.createHTMLFromProceedings(None)
        self.assertEqual(strRepresentation, None)
        #1.b
        strRepresentation = wrtr.createHTMLFromProceedings(1)
        self.assertEqual(strRepresentation, None)
        #2
        prcdngs = Proceedings(self.testTask, self.testTimeStamp)
        expectedOutput = "<html>\n\
<head>\n\
\t<title>PrettyTestTask run at 201405161350</title>\n\
\t<link rel=\"stylesheet\" type=\"text/css\" href=\"proceedings_css.css\">\n\
</head>\n\
<body>\n\
<h1> Task: PrettyTestTask </h1>\n\
<h2> Run at time: 201405161350 </h2>\n\
<br><br>\n\
<table id=\"mainTable\">\n\
\t<tr>\n\
\t\t<td id=\"piAndCAS\"> Problem Instance/Computer Algebra System</td>\n\
\t\t<td id=\"casName\">cas4</td>\n\
\t\t<td id=\"casName\">cas1</td>\n\
\t\t<td id=\"casName\">cas3</td>\n\
\t\t<td id=\"casName\">cas2</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI1</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI2</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI3</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI4</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
</table>\n\
</body>\n\
</html>"
        self.assertEqual(wrtr.createHTMLFromProceedings(prcdngs), expectedOutput,"HTML representation was wrong")
        

    def test_ProceedingsToXMLWriter(self):
        """
        Testing the correctness of the ProceedingsToXMLWriter class.
        The following test cases are covered:
        1. Calling a ProceedingsToXMLWriter with a wrong parameter
           1.a None
           1.b an integer value
        2. Calling the ProceedintsToXMLWriter with a correct parameter
        """
        wrtr = ProceedingsToXMLWriter()
        #1.a
        strRepresentation = wrtr.createXMLFromProceedings(None)
        self.assertEqual(strRepresentation, None)
        #1.b
        strRepresentation = wrtr.createXMLFromProceedings(1)
        self.assertEqual(strRepresentation, None)
        #2
        prcdngs = Proceedings(self.testTask, self.testTimeStamp)
        strRepresentation = wrtr.createXMLFromProceedings(prcdngs).toxml()
        expectedOutput = "<?xml version=\"1.0\" ?><proceedings><timestamp>201405161350</timestamp><task>PrettyTestTask</task><waiting><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry></waiting><running/><completed/><error/></proceedings>"
        self.assertEqual(expectedOutput, strRepresentation,"Output of XML-file did not match what we wanted to have")


    def test_ResultedTimingsToHTMLWriter(self):
        """
        Testing the correctness of the ResultedTimingsToHTMLWriter class.
        The following test cases are covered:
        1. Calling a ResultedTimingsToHTMLWriter with a wrong parameter
           1.a None
           1.b an integer value
        2. Calling the ResultedTimingsToHTMLWriter with a correct parameter
        """
        wrtr = ResultedTimingsToHTMLWriter()
        #1.a
        strRepresentation = wrtr.createHTMLFromResultedTimings(None)
        self.assertEqual(strRepresentation, None)
        #1.b
        strRepresentation = wrtr.createHTMLFromResultedTimings(1)
        self.assertEqual(strRepresentation, None)
        #2
        rsltTimings = ResultedTimings(None, self.testTask, self.testTimeStamp)
        expectedOutput = "<html>\n\
<head>\n\
\t<title>PrettyTestTask run at 201405161350</title>\n\
\t<link rel=\"stylesheet\" type=\"text/css\" href=\"proceedings_css.css\">\n\
</head>\n\
<body>\n\
<h1> Task: PrettyTestTask </h1>\n\
<h2> Run at time: 201405161350 </h2>\n\
<br><br>\n\
<table id=\"mainTable\">\n\
\t<tr>\n\
\t\t<td id=\"piAndCAS\"> Problem Instance/Computer Algebra System</td>\n\
\t\t<td id=\"casName\">cas4</td>\n\
\t\t<td id=\"casName\">cas1</td>\n\
\t\t<td id=\"casName\">cas3</td>\n\
\t\t<td id=\"casName\">cas2</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI1</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI2</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI3</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
\t<tr>\n\
\t\t<td id=\"piName\">PI4</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t\t<td id=\"waitingCalc\">WAITING</td>\n\
\t</tr>\n\
</table>\n\
</body>\n\
</html>"
        self.assertEqual(expectedOutput,wrtr.createHTMLFromResultedTimings(rsltTimings),"HTML output of ResultedTimings was not correct.")


    def test_ResultedTimingsToXMLWriter(self):
        """
        Testing the correctness of the ResultedTimingsToXMLWriter class.
        The following test cases are covered:
        1. Calling a ResultedTimingsToXMLWriter with a wrong parameter
           1.a None
           1.b an integer value
        2. Calling the ResultedTimingsToXMLWriter with a correct parameter
        """
        wrtr = ResultedTimingsToXMLWriter()
        #1.a
        strRepresentation = wrtr.createXMLFromResultedTimings(None)
        self.assertEqual(strRepresentation, None)
        #1.b
        strRepresentation = wrtr.createXMLFromResultedTimings(1)
        self.assertEqual(strRepresentation, None)
        #2
        rsltTimings = ResultedTimings(None, self.testTask, self.testTimeStamp)
        strRepresentation = wrtr.createXMLFromResultedTimings(rsltTimings).toxml()
        expectedOutput = "<?xml version=\"1.0\" ?><proceedings><timestamp>201405161350</timestamp><task>PrettyTestTask</task><waiting><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI1</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI2</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI3</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas1</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas2</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas3</computeralgebrasystem></entry><entry><probleminstance>PI4</probleminstance><computeralgebrasystem>cas4</computeralgebrasystem></entry></waiting><running/><completed/><error/></proceedings>"
        self.assertEqual(strRepresentation, expectedOutput)

    def test_ResultingFile(self):
        """
        This tests checks the correct initialization of ResultingFile.
        It covers the following tests after initializing it with some dummy-input:
        1. Test the getters
           1.a) Invalid dicitonary for the time
           1.b) Valid dicitonary for the time
        2. Test the string representation
        """
        #1.a
        testGuy1 = ResultingFile(None,None,None,None)
        self.assertEqual(testGuy1.getTimes(),
                         {"real":0.0,"user":0.0,"sys":0.0},
                         "Times with None as input were not correctly initialized.")
        self.assertEqual(testGuy1.getCASOutput(),None, "Casoutput was not None as expected.")
        self.assertEqual(testGuy1.getComputerAlgebraSystem(),None, "Computeralgebrasystem was not None as expected")
        self.assertEqual(testGuy1.getProblemInstance(),None,"Probleminstance was not None as expected")
        #1.b
        testGuy2 = ResultingFile("Magic", "MagicCAS", "hello", {"real":10.0,"user":5.0,"sys":5.0})
        self.assertEqual(testGuy2.getTimes(),
                         {"real":10.0,"user":5.0,"sys":5.0},
                         "Times with valid entry were not correctly initialized.")
        self.assertEqual(testGuy2.getCASOutput(),"hello", "Casoutput was not as expected.")
        self.assertEqual(testGuy2.getComputerAlgebraSystem(),"MagicCAS", "Computeralgebrasystem was not as expected")
        self.assertEqual(testGuy2.getProblemInstance(),"Magic","Probleminstance was not as expected")
        #2
        expectedOutput = "Problem instance: Magic\n\
Computer algebra system: MagicCAS\n\
Times:\n\
    real: 10.0\n\
    user: 5.0\n\
     sys: 5.0\n\
Output:\n\
hello"
        self.assertEqual(expectedOutput, str(testGuy2),"String representation of ResultingFile was not correct.")


    def test_ResultingFileFromOutputBuilder(self):
        """
        This tests checks the correctness of the ResultingFileFromOutputBuilder class.
        It covers the following cases for an instance of ResultingFileFromOutputBuilder:
        1. None is input
        2. Input has not the time-entries as last three lines
        3. Input has the three time entries correctly as last three lines.
        4. Input has the three time entries scattered as the last three lines.
        """
        builder = ResultingFileFromOutputBuilder()
        testPassed = 1
        #1.
        try:
            rf = builder.build("MagicInstance", "MagicCAS", None)
            testPassed = 0
        except:
            pass
        if (testPassed ==0):
            self.fail("Could build a ResultingFile with None as specified output.")
        #2.
        try:
            rf =builder.build("MagicInstance", "MagicCAS", "hello")
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could build a ResultingFile with no time entries in the end")
        #3.
        try:
            rf = builder.build("MagicInstance", "MagicCAS", "hello\nreal 0.10\nuser 0.01\nsys 0.09")
        except:
            self.fail("Gave the ResultingfileBuilder a correct input, but it could not use it.")
        #4.
        try:
            rf = builder.build("MagicInstance", "MagicCAS", "hello\n  \t  real 0.10\n\t   user 0.01\t\n\tsys 0.09")
        except:
            self.fail("Gave the ResultingfileBuilder a correct but scattered input, but it could not use it.")
        print rf.getTimes()
        self.assertEqual(rf.getTimes(),
                         {"real":"0.10","user":"0.01","sys":"0.09"},
                         "Times with valid entry were not correctly initialized.")
        self.assertEqual(rf.getCASOutput(),"hello", "Casoutput was not as expected.")
        self.assertEqual(rf.getComputerAlgebraSystem(),"MagicCAS", "Computeralgebrasystem was not as expected")
        self.assertEqual(rf.getProblemInstance(),"MagicInstance","Probleminstance was not as expected")


if __name__=="__main__":
    unittest.main()
