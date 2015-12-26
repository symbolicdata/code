import os
from exceptions.XMLRessourcesInvalidPath import XMLRessourcesInvalidPath
from exceptions.NoSuchSDTable import NoSuchSDTable
from SDTable import SDTable

class XMLRessources(object):
    """
    This class is the interface to the Folder XMLRessources in the SymbolicData folder tree.
    Its purpose is, that one can access the different SD-Tables inside this folder.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    __requiredTables = ["IntPS",
                      "FreeAlgebras",
                      "ModPS",
                      "GAlgebras"]
    """
    At least one of those tables should be contained in XMLRessources for being able to work with this table.
    This will be checked when creating this instance
    """

    def __init__(self, folder = os.path.join("..", "..", "data", "XMLResources")):
        """
        This function is the constructor of the class XMLRessources. It sets the internal
        variable folder to the given path. If the given folder is not valid, the constructor raises
        an exception.

        :requires:                       Existence of the folder that was given as input
        :param folder:                   The path to the XMLRessources Folder
        :type  folder:                   A string representing a valid path
        :raise XMLRessourcesInvalidPath: If given folder is not valid, this exception is raised
        """
        
        if not os.path.isdir(folder):
            raise XMLRessourcesInvalidPath("The given folder " + str(folder) + " is not a valid path!")
        if not self.__isValidXMLRessourcesFolder(folder):
            raise XMLRessourcesInvalidPath("The given folder " + str(folder) + "is not a valid XMLRessources folder.\
 Some of the required tables are missing")
        self.__folder = os.path.abspath(folder)

    def __isValidXMLRessourcesFolder(self, folder):
        """
        Checks the validity of the given folder. It is valid, if at least one of the tables of the variable
        __requiredTables is contained in this folder.
        """
        tablesInFolder = filter(lambda f: os.path.isdir(os.path.join(folder, f)),
                                os.listdir(folder))
        containedInRequiredTables = map(lambda f: f in self.__requiredTables,tablesInFolder)
        return (True if len(containedInRequiredTables)>0 else False)

    def loadSDTable(self, tableName):
        """
        Returns an instance of SD-Table specified by the given parameter "tableName"

        :param     tableName: The name of the table the user wants to have access to
        :type      tableName: string
        :return:              An instance of SDTable representing the SDTable given by tableName
        :rtype:               SDTable
        :raise NoSuchSDTable: If the requested SD-Table does not exist, this exception is raised
        """
        if not os.path.isdir(os.path.join(self.__folder,tableName)):
            raise NoSuchSDTable("The table "+str(tableName)+ " does not exist in the XMLRessources folder!\nXMLResources Path: " + self.__folder)
        return SDTable(os.path.join(self.__folder, tableName))

    def listSDTables(self):
        """
        Returns a list with all available SD-Tables in the XMLRessources folder.

        :rtype:    list
        :returns:  A list with all SD-Tables available
        """
        return filter(lambda f: os.path.isdir(os.path.join(self.__folder, f)),
                      os.listdir(self.__folder))

    def getPath(self):
        """
        Returns the Path to the XMLRessources folder.

        :returns: Path of the XMLRessources folder.
        :rtype:   string
        """
        return self.__folder

    def __str__(self):
        """
        Returns a String representation of the instance of XMLRessources. It has the following format::
            Folder: <PathToXMLRessources>
            Folder contains the following SDTables:
            <SDTable1>
            <SDTable2>
            ...
        """
        result = "Folder: {0}\n\
Folder contains the following SDTables:\n{1}".format(self.__folder, "\n".join(self.listSDTables()))
        return result

    def __del__(self):
        """
        The deletion of all internal variables.
        TODO
        """
        pass
