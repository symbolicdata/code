from FreeAlgebra import FreeAlgebra
import xml.dom.minidom as dom

class FreeAlgebrasFromXMLBuilder(object):
    """
    This class serves the purpose to create an FreeAlgebra instances from  given XML-Files.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, sdTable):
        """
        This is the constructor of the FreeAlgebrasFromXMLBuilder. One only needs to provide the SDTable where
        the FreeAlgebra-instances are found.

        :param sdTable: The table that contains all the FreeAlgebra-instances
        :type  sdTable: SDTable
        """
        self.__sdTable = sdTable

    def build(self,name, xmlRaw=None):
        """
        The main command in this class. Given an raw xml-String containing an FreeAlgebra-instance.
        It creates an instance of type FreeAlgebra associated to the xml-string and returns it.

        :param   xmlRaw: The xml-Representation of the FreeAlgebra-Entry.
        :type    xmlRaw: string
        :param     name: The name of the FreeAlgebra-Entry
        :type      name: string
        :raises IOError: If something is wrong with the XMLstring this exception is raised.
        :returns:        An instance of FreeAlgebra associated to the xml Input string
        :rtype:          FreeAlgebra
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
            raise IOERROR("The given XMLString does not contain variables for the FreeAlgebra System!")
        if (xmlTree.getElementsByTagName("basis") == []): # Check, if we have a basis
            raise IOERROR("The given XMLString does not contain a basis for the FreeAlgebra System!")
        if (xmlTree.getElementsByTagName("uptoDeg")==[]): #check, if there is an entry upToDeg
            raise IOERROR("The given XMLString does not contain an upToDeg-Entry!")
        #-------------------- Input Check finished --------------------
        #From here, we can assume that the input is given correct
        #Extract Variables:
        variablesCSV = (xmlTree.getElementsByTagName("vars")[0]).firstChild.data
        variables = map(lambda x: str(x).strip(),variablesCSV.rsplit(","))
        #Extract basis:
        polynomials = xmlTree.getElementsByTagName("basis")[0]
        basis = map(lambda poly: str(poly.firstChild.data).strip(),polynomials.getElementsByTagName("ncpoly"))
        #Extract upToDegree:
        uptoDeg = int((xmlTree.getElementsByTagName("uptoDeg")[0]).firstChild.data)
        return FreeAlgebra(name, self.__sdTable, variables, basis, uptoDeg)

    #TODO __del__
