import unittest
import MachineSettings as MS

class TestMachineSettings(unittest.TestCase):
    """
    Tests for the class MachineSettings

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def setUp(self):
        """
        Our setup is a typical one where we have three computer algebra systems in
        in the input dictionary and "time -p" as our time command
        """
        casDict = {"Singular":"Singular", "Magma":"magma", "Maple":"maple"}
        timeCommand = "time -p"
        self.msTest = MS.MachineSettings(casDict,timeCommand)

    def testStringRepresentation(self):
        """
        Tests if the string representation is valid.
        """
        strRep = str(self.msTest)
        expectedStrRep = "Computer algebra systems and commands:\n\
    Magma : magma\n\
    Maple : maple\n\
    Singular : Singular\n\
Time Command: time -p"
        self.assertEqual(strRep,expectedStrRep,
                         "Something was wrong with the string representation of\
an instance of the class MachineSettings")

    def testCasDict(self):
        """
        Tests if the dictionary with the respective computer algebra systems was
        initialized in a valid way.
        """
        casDict = {"Singular":"Singular", "Magma":"magma", "Maple":"maple"}
        self.assertEqual(casDict, self.msTest.getCASDict(),
                     "The dictionary inside the MachineSettings was not validly initialized")

    def testTimeCommand(self):
        """
        Tests whether the time command was saved as expected.
        """
        timeCommand = "time -p"
        self.assertEqual(timeCommand,self.msTest.getTimeCommand(),
                         "The time command inside the MachineSettings was not validly initialized")

    def testCasCommand(self):
        """
        Tests whether the right execution command for a certain computer algebra system
        is returned.
        """
        self.assertEqual(None, self.msTest.getCASCommand("abc123"),
                    "\"abc123\" was not a valid computer algebra system in the list, but\
our machine settings instance returned it as one.")
        self.assertEqual("magma", self.msTest.getCASCommand("Magma"),
                    "Could not receive command for valid computer algebra system (Magma)")

    def testXMLRepresentation(self):
        """
        Tests whether the XML Representation of the Machine Settings is correct.
        """
        expectedXMLRep='<?xml version="1.0" ?><machinesettings><othervars><timecommand>\
time -p</timecommand></othervars><casdictionary><entry><key>Magma</key><value>magma</value>\
</entry><entry><key>Maple</key><value>maple</value></entry><entry><key>Singular</key><value>\
Singular</value></entry></casdictionary></machinesettings>'
        actualXMLRep = self.msTest.toXML().toxml()
        self.assertEqual(expectedXMLRep,actualXMLRep,
                         "The representation of the machine settings as XML was not correct.")
        
if __name__=="__main__":
    unittest.main()
