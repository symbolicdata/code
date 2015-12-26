class ProblemInstance(object):
    """
    A problem instance in our context is a representation -- specified by SymbolicData --
    of a concrete input for suitable algorithms. Here, suitable means that the required input
    values for the particular algorithm can be derived from the values in the problem instance.
    A problem instance is contained in an SD-Table.
    This class is meant to be used as abstract class.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, pIName ,sdTable):
        """
        This is the constructor of the ProblemInstance.
        Note: No validity checks will be done (like if the pI is contained in the sdTable

        :param  pIName: The name of the problem instance
        :type   pIName: string
        :param sdTable: The I{SDTable} where one can find the problem instance
        :type  sdTable: SDTable
        """
        self.__name    = pIName
        self.__sdTable = sdTable
        try:
            self.__xmlRaw  = sdTable.loadEntry(pIName)
        except:
            self.__xmlRaw  = None

    def getXMLRaw(self):
        """
        Returns the raw XML-String representing this problem instance.
        This can be None, if the instanciation variables were not valid.

        :return: The raw XML-Represenation of the problem instance, or None.
        :rtype:  string
        """
        return self.__xmlRaw

    def getSDTable(self):
        """
        Returns the SDTable where the problem instance can be found.

        :return: The SDTable containing this problem instance
        :rtype:  SDTable
        """
        return self.__sdTable

    def getName(self):
        """
        Returns the name of the problem instance.

        :return: The name of this problem instance
        :rtype:  string
        """
        return self.__name

    def __str__(self):
        """
        Retunrs a string representation of the problem instance. It has the following form::
            Problem Instance: <Name of Problem instance>
            Associated SD-Table: <Name of associated SD-Table>
            XMLRaw: <the xml raw representation of this problem instance>
        """
        result = "Problem instance: %s\nAssociated SD-Table: %s\nXMLRaw: %s" % (self.__name,self.__sdTable.getName(),self.__xmlRaw)
        return result
    #TODO:__del
