import unittest
from TaskFolderTree import TaskFolderTree

class TestTaskFolderTree(unittest.TestCase):
    """
    Tests for the class TaskFolderTree

    .. moduleauthor:: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def test_TaskFolderTree(self):
        """
        Testing the main functionality of TaskFolderTree

        This function includes the following tests:
        1. Test correct initialization (i.e. all paths should be empty)
        2. Test string representation
           1. empty tree
           2. filled tree
        3. Add paths and check all the getters to be correct or not.
        """
        #1.
        tft = TaskFolderTree()
        self.assertEqual(tft.getAllPaths(),[],"Initial paths list in TaskFolderTree is not empty")
        self.assertEqual(tft.getPathsBySDTable("asdklfh"),[],"Initial paths list contains an entry with SDTable")
        self.assertEqual(tft.getPathsByProblemInstance("ireotueroi"),[],
                         "Initial paths list contains an entry with a probleminstance")
        self.assertEqual(tft.getPathsByComputerAlgebraSystem("'ukl;yu;klp"),[],
                         "Initial paths list contains an entry with a cas")
        #2.1
        self.assertEqual(str(tft), "Empty Tree", "String representation of empty tree was not valid.")
        #2.2
        tft.addCode("MySDTable", "MyPI1", "MyCAS1", "maleficient code 1.")
        tft.addCode("MySDTable", "MyPI2", "MyCAS1", "maleficient code 2.")
        tft.addCode("MySDTable", "MyPI1", "MyCAS2", "maleficient code 3.")
        tft.addCode("MySDTable", "MyPI2", "MyCAS2", "maleficient code 4.")
        expectedStringRep = """MySDTable:
    MyPI1:
        MyCAS1
        MyCAS2
    MyPI2:
        MyCAS1
        MyCAS2
"""
        self.assertEqual(str(tft),expectedStringRep, "String representation of non-empty Tree is not valid")
        #3
        self.assertEqual(len(tft.getAllPaths()),4,"Amount of Paths was wrong")
        self.assertEqual(len(tft.getPathsBySDTable("MySDTable")),4,"Path number by SDTable was wrong")
        self.assertEqual(len(tft.getPathsByProblemInstance("MyPI1")),2,"Path number by Problem instance was wrong")
        self.assertEqual(len(tft.getPathsByComputerAlgebraSystem("MyCAS1")),2,
                         "Path number by CAS was wrong")
        


if __name__=="__main__":
    unittest.main()
