import unittest
import MachineSettingsFromXMLBuilder as MSFXMLB
import MachineSettings as MS

class TestMachineSettingsFromXMLBuilder(unittest.TestCase):
    """
    Tests for the class MachineSettingsFromXMLBuilder

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
        self.builder = MSFXMLB.MachineSettingsFromXMLBuilder()

    def test_CorrectInput(self):
        """
        This will simply include the raw xml file of msTest (see setUp)
        We will parse it and then compare the different entries in the original
        msTest and the parsed one.
        """
        actualOutPut = self.builder.build(self.msTest.toXML().toxml())
        self.assertEqual(self.msTest.getCASDict(),actualOutPut.getCASDict(),
                         "The computer algebra dictionary got broken after parsing")
        self.assertEqual(self.msTest.getTimeCommand(),actualOutPut.getTimeCommand(),
                         "We obtain a different time command after parsing")
        self.assertEqual(str(self.msTest),str(actualOutPut),
                         "The string representation of the original machine settings instance\
 and the parsed representative differs.")

    def test_InvalidXML(self):
        """
        We will include some tests here that will cause the parsing errors to raise.

        1) invalid XML syntax
           - Emtpy string
           - "<xml></xml>"
           - "!@#$%^&*()_+"
           - "123467"
        2) Invalid input for Machine Settings XML
        """
        #1)
        testPassed = 1
        try:
            temp = builder.build("")
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build Machine Settings from the empty string.")
        try:
            temp = builder.build("<xml></xml>")
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could build Machine Settings from empty xml.")
        try:
            temp = builder.build("!@#$%^&*()_+")
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could build Machine Settings from completely invalid string.")
        try:
            temp = builder.build("123467")
            testPassed = 0
        except:
            pass
        if testPassed == 0:
            self.fail("Could build Machine Settings from \"123467\".")
        #2)
        try:
            temp = builder.build('<?xml version="1.0" ?><machinesettings><othervars>\
<timecommand>time -p</timecommand></othervars><casdictionary></casdictionary></machinesettings>')
            testPassed = 0
        except:
            pass
        if (testPassed == 0):
            self.fail("Could build Machine Settings from string without computer algebra systems.")
        
if __name__=="__main__":
    unittest.main()
