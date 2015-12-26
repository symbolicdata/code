from IntPS import IntPS
import xml.dom.minidom as dom

class IntPSFromXMLBuilder(object):
    """
    This class serves the purpose to create an IntPS instances from  given XML-Files.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, sdTable):
        """
        This is the constructor of the IntPSFromXMLBuilder. One only needs to provide the SDTable where
        the IntPS-instances are found.

        :param sdTable: The table that contains all the IntPS-instances
        :type  sdTable: SDTable
        """
        self.__sdTable = sdTable

    def build(self,name, xmlRaw=None):
        """
        The main command in this class. Given an raw xml-String containing an IntPS-instance.
        It creates an instance of type IntPS associated to the xml-string and returns it.

        :param   xmlRaw: The xml-Representation of the IntPS-Entry.
        :type    xmlRaw: string
        :param     name: The name of the IntPS-Entry
        :type      name: string
        :raises IOError: If something is wrong with the XMLstring this exception is raised.
        :returns:        An instance of IntPS associated to the xml Input string
        :rtype:          IntPS
        """
        #-------------------- Input Check --------------------
        try:
            if xmlRaw:
                xmlTree = dom.parseString(xmlRaw)
            else:
                xmlTree = dom.parseString(self.__sdTable.loadEntry(name))
        except:
            raise IOError("Could not parse the given string as XML-Instance")
        if (xmlTree.getElementsByTagName("vars") == []): # Check, if vars are there
            raise IOERROR("The given XMLString does not contain variables for the IntPS System")
        if (xmlTree.getElementsByTagName("basis") == []): # Check, if we have a basis
            raise IOERROR("The given XMLString does not contain a basis for the IntPS System")
        #-------------------- Input Check finished --------------------
        #From here, we can assume that the input is given correct
        variablesCSV = (xmlTree.getElementsByTagName("vars")[0]).firstChild.data
        variables = map(lambda x: str(x).strip(),variablesCSV.rsplit(","))
        polynomials = xmlTree.getElementsByTagName("basis")[0]
        basis = map(lambda poly: str(poly.firstChild.data).strip(),polynomials.getElementsByTagName("poly"))
        return IntPS(name, self.__sdTable, variables, basis)

    #TODO __del__
