import os
from exceptions.NoSuchSDTable import NoSuchSDTable
from exceptions.NoSuchEntry import NoSuchEntry
import xml.dom.minidom as dom

class SDTable(object):
    """
    This class forms an interface to an arbitrary, but fixed SymbolicData table.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self,tablePath=None, (XMLResources,tableName)=(None,None)):
        """
        This is the constructor of SDTable. An instance can be created in two ways:
           1. By giving the complete path to the table in the XMLResources folder (tablepath). It will not be
              checked, if the entry makes sense.
           2. By giving an instance of XMLResources and the desired tablename. (XMLResources, tableName)
        If the table does not exist, an exception will be raised. (NoSuchSDTable)

        :param     tablePath: The path to the desired SD-Table
        :type      tablePath: string
        :param XMLResources: An instance of XMLResources where we can access a table given by its name.
        :param     tableName: The name of the desired table
        :type  XMLResources: XMLResources
        :type      tableName: string
        :raise NoSuchSDTable: If the table des not exist, this exception will be raised.
        :raise       IOError: If the input was not valid, this exception will be raised.
        """
        if tablePath:
            if not os.path.isdir(tablePath):
                raise NoSuchSDTable("The path " + str(tablePath) + " is not a valid path!")
            else:
                self.__sdTableFolder = os.path.abspath(tablePath)
                self.__name          = (self.__sdTableFolder.split(os.sep))[-1]
        elif XMLResources and tableName:
            if not os.path.isdir(os.path.join(XMLResources.getPath(),tableName)):
                raise NoSuchSDTable("The SDTable "+str(tableName)+" does not exist in XMLResources given by\n"+str(XMLResources))
            else:
                self.__sdTableFolder = os.path.abspath(os.path.join(XMLResources.getPath(),tableName))
                self.__name          = tableName
        else:
            raise IOError("Something was wrong with the Input")

    def loadEntry(self, entryName):
        """
        Loads the entry given by I{entryName} as XML string.

        :param entryName:   Name of the entry in the SD-Table the user wants to access.
        :type  entryName:   string
        :raise NoSuchEntry: If the entry is not in the SD-Table, this exception will be raised.
        :returns:           XML string representing the entry represented by entryName
        """
        entryNameRaw = (entryName[:-4] if entryName.endswith(".xml") else entryName)
        allEntries = self.listEntries()
        if not (entryNameRaw in allEntries):
            raise NoSuchEntry("The entry " + str(entryName) + " does not exist in this SD-Table named "+self.__name)
        else:
            f = open(os.path.join(self.__sdTableFolder, entryNameRaw+".xml"))
            result = f.read()
            f.close()
            try:
                dom.parseString(result)
                return result
            except:
                raise NoSuchEntry("The entry " + str(entryName) + " in this SD-Table named "+self.__name+" does not contain valid XML")

    def listEntries(self):
        """
        Returns a list with the names of all entries in this SD-Table instance

        :returns: List with all entries in this SD-Table
        :rtype:   list
        """
        return map(lambda s: s[:-4],filter(lambda f: f.endswith(".xml"), os.listdir(self.__sdTableFolder)))

    def getName(self):
        """
        Returns the name of this SD-Table

        :returns: Name of SD-Table instance
        :rtype:   string
        """
        return self.__name

    def __str__(self):
        """
        Returns a string representation of the SDTable in the following format::
            SDTable: <Name of SDTable>
            SDTable contains the following entries:
            <Entry1>
            <Entry2>
            ...
        """
        result = "SDTable: %s\nSDTable contains the following entries:\n%s" % (self.__name, "\n".join(self.listEntries()))
        return result
    #TODO:__del
