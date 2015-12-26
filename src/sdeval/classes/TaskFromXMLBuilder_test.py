import unittest
from TaskFromXMLBuilder import TaskFromXMLBuilder

class TestTaskFromXMLBuilder(unittest.TestCase):
    """
    Tests for the class TaskFromXMLBuilder

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """
    
    def testTaskCreate(self):
        """
        This test covers the basic functionality of TaskFromXMLBuilder.build

        The covered test cases are the following:
        1. Create Task with an empty string as XML-String
        2. Create Task with some values being invalid:
           2.a. Empty string for the name
           2.b. Empty list of computer algebra systems
           2.c. Empty string for computation problem
           2.d. Empty list for sdtables
           2.e. Empty list for problem instances
        3. Valid Task creation. Test if all got parsed correctly
        """
        #1.
        testPassed = 1
        xmlString = ""
        try:
            TaskFromXMLBuilder().build(xmlString)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build a Task from an empty xml-string")
        #2.a
        xmlString = """<task>
  <name>
  </name>
  <computationproblem>
    CompProb
  </computationproblem>
  <computeralgebrasystems>
    <computeralgebrasystem>
      cas1
    </computeralgebrasystem>
    <computeralgebrasystem>
      cas2
    </computeralgebrasystem>
  </computeralgebrasystems>
  <sdtables>
    <sdtable>
      <tablename>
        sdtable1
      </tablename>
      <probleminstances>
        <probleminstance>
          problemInstance1
        </probleminstance>
        <probleminstance>
          problemInstance2
        </probleminstance>
      </probleminstances>
    </sdtable>
  </sdtables>
  </task>"""
        try:
            TaskFromXMLBuilder().build(xmlString)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build a Task without a name")
        #2.b
        xmlString = """<task>
  <name>
  PrettyTestTask
  </name>
  <computationproblem>
    CompProb
  </computationproblem>
  <computeralgebrasystems>
  </computeralgebrasystems>
  <sdtables>
    <sdtable>
      <tablename>
        sdtable1
      </tablename>
      <probleminstances>
        <probleminstance>
          problemInstance1
        </probleminstance>
        <probleminstance>
          problemInstance2
        </probleminstance>
      </probleminstances>
    </sdtable>
  </sdtables>
  </task>"""
        try:
            TaskFromXMLBuilder().build(xmlString)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build a Task without any computer algebra systems")
        #2.c.
        xmlString = """<task>
  <name>
  Pretty
  </name>
  <computationproblem>
  </computationproblem>
  <computeralgebrasystems>
    <computeralgebrasystem>
      cas1
    </computeralgebrasystem>
    <computeralgebrasystem>
      cas2
    </computeralgebrasystem>
  </computeralgebrasystems>
  <sdtables>
    <sdtable>
      <tablename>
        sdtable1
      </tablename>
      <probleminstances>
        <probleminstance>
          problemInstance1
        </probleminstance>
        <probleminstance>
          problemInstance2
        </probleminstance>
      </probleminstances>
    </sdtable>
  </sdtables>
  </task>"""
        try:
            TaskFromXMLBuilder().build(xmlString)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build a Task without a computation problem")
        #2d
        xmlString = """<task>
  <name>
  PrettyTask
  </name>
  <computationproblem>
    CompProb
  </computationproblem>
  <computeralgebrasystems>
    <computeralgebrasystem>
      cas1
    </computeralgebrasystem>
    <computeralgebrasystem>
      cas2
    </computeralgebrasystem>
  </computeralgebrasystems>
  <sdtables>
    <sdtable>
      <probleminstances>
        <probleminstance>
          problemInstance1
        </probleminstance>
        <probleminstance>
          problemInstance2
        </probleminstance>
      </probleminstances>
    </sdtable>
  </sdtables>
  </task>"""
        try:
            TaskFromXMLBuilder().build(xmlString)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build a Task without an sdtable")
        #2.e
        xmlString = """<task>
  <name>
  PrettyTask
  </name>
  <computationproblem>
    CompProb
  </computationproblem>
  <computeralgebrasystems>
    <computeralgebrasystem>
      cas1
    </computeralgebrasystem>
    <computeralgebrasystem>
      cas2
    </computeralgebrasystem>
  </computeralgebrasystems>
  <sdtables>
    <sdtable>
      <tablename>
        sdtable1
      </tablename>
      <probleminstances>
      </probleminstances>
    </sdtable>
  </sdtables>
  </task>"""
        try:
            TaskFromXMLBuilder().build(xmlString)
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build a Task without any problem instance")

        #3.
        xmlString = """<task>
  <name>
  PrettyWorkingTask
  </name>
  <computationproblem>
    CompProb
  </computationproblem>
  <computeralgebrasystems>
    <computeralgebrasystem>
      cas1
    </computeralgebrasystem>
    <computeralgebrasystem>
      cas2
    </computeralgebrasystem>
  </computeralgebrasystems>
  <sdtables>
    <sdtable>
      <tablename>
        sdtable1
      </tablename>
      <probleminstances>
        <probleminstance>
          problemInstance1
        </probleminstance>
        <probleminstance>
          problemInstance2
        </probleminstance>
      </probleminstances>
    </sdtable>
  </sdtables>
  </task>"""
        try:
            myTask = TaskFromXMLBuilder().build(xmlString)
        except:
            self.fail("Could not build a task with valid xml representation")
        #Checking if everything is correct with this task
        self.assertEqual(myTask.getComputationProblem(),"CompProb",
                         "The computation problem associated with the task is not correct.")
        self.assertEqual(myTask.getName(),"PrettyWorkingTask",
                         "The name of the task was not correctly parsed")
        self.assertEqual(set(myTask.getAssociatedSDTables()),set(["sdtable1"]),
                         "The associated SDTables were not parsed correctly")
        self.assertEqual(set(myTask.getProblemInstances()),set(["problemInstance1","problemInstance2"]),
                         "The problem instances were not parsed correctly")
        self.assertEqual(set(myTask.getComputerAlgebraSystems()),set(["cas1","cas2"]),
                         "The computer algebra systems were not parsed correctly.")
        

if __name__=="__main__":
    unittest.main()
