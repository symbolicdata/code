from ModPS import ModPS
import xml.dom.minidom as dom

class ModPSFromXMLBuilder(object):
    """
    This class serves the purpose to create an ModPS instances from  given XML-Files.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, sdTable):
        """
        This is the constructor of the ModPSFromXMLBuilder. One only needs to provide the SDTable where
        the ModPS-instances are found.

        :param sdTable: The table that contains all the ModPS-instances
        :type  sdTable: SDTable
        """
        self.__sdTable = sdTable

    def build(self,name, xmlRaw=None):
        """
        The main command in this class. Given an raw xml-String containing an ModPS-instance.
        It creates an instance of type ModPS associated to the xml-string and returns it.

        :param   xmlRaw: The xml-Representation of the ModPS-Entry.
        :type    xmlRaw: string
        :param     name: The name of the ModPS-Entry
        :type      name: string
        :raises IOError: If something is wrong with the XMLstring this exception is raised.
        :returns:        An instance of ModPS associated to the xml Input string
        :rtype:          ModPS
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
            raise IOERROR("The given XMLString does not contain variables for the ModPS System!")
        if (xmlTree.getElementsByTagName("basis") == []): # Check, if we have a basis
            raise IOERROR("The given XMLString does not contain a basis for the ModPS System!")
        if (xmlTree.getElementsByTagName("basedomain") == []):
            raise IOERROR("The given XMLString does not contain a basefield.")
        #-------------------- Input Check finished --------------------
        #From here, we can assume that the input is given correct
        #Extract Variables:
        variablesCSV = (xmlTree.getElementsByTagName("vars")[0]).firstChild.data
        variables = map(lambda x: str(x).strip(),variablesCSV.rsplit(","))
        #Extract basis:
        polynomials = xmlTree.getElementsByTagName("basis")[0]
        basis = map(lambda poly: str(poly.firstChild.data).strip(),polynomials.getElementsByTagName("poly"))
        #Extract characteristic:
        characteristic = int(((xmlTree.getElementsByTagName("basedomain")[0]).firstChild.data)[3:-1]) #entry has the form GF(somePrime); here, we extract somePrime
        return ModPS(name, self.__sdTable, variables, basis, characteristic)

    #TODO __del__
