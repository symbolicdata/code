from copy import deepcopy

class TaskFolderTree(object):
    """
    An instance of this tree represents the folder hierarchy on a taskfolder, where the executable
    files are stored for the different computer algebra systems on specific problem instances.
    Its leafs are the executable strings, and the rest of the tree has the following form::

                                         (root)
                                         /    \\
        SD-Tables-level                ...   "Some SDTable"
                                                 \\
        problem instance level                 "Some problem instance"
                                                     \\
        computer algebra system level            "Some computer algebra system"
                                                        \\
        executable code level                        "The executable code"

    .. seealso: :mod:`TaskFolder <sdeval.classes.TaskFolder>`, :mod:`Task <sdeval.classes.Task>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self):
        """
        The constructor of the TaskFolderTree. Nothing is supposed to happen here except from
        initialisation of class variables, as the Tree is built up after initialisation.
        """
        self.__paths = []
        """
        In the variable paths, there are always 4-tuples saved. For example the tuple::

          ["IntPS", "Amrhein", "Singular", "ring R = 0,(a,b,c,d,e,f),lp;..."]
              ^         ^          ^                   ^
              |         |          |                   |
            SDTable   problem     CAS           executable code
        """


    def addCode(self,sdTable, problemInstance, cas, execCode):
        """
        This function is to add code to the tree.

        :param          sdTable: The name of the SD-Table the problem instance is coming from
        :type           sdTable: string
        :param  problemInstance: The name of the problem instance, where the input was taken from
        :type   problemInstance: string
        :param              cas: The name of the computeralgebra system for which the executable code can be used.
        :type               cas: string
        :param         execCode: The executable code for the computer algebra system.
        :type          execCode: string
        """
        if not [sdTable, problemInstance,cas, execCode] in self.__paths:
            self.__paths.append([sdTable, problemInstance,cas, execCode])

    def getAllPaths(self):
        """
        Returns all paths as a list of lists.

        :returns: A list with all paths in the tree
        :rtype:   list
        """
        return self.__paths

    def getPathsBySDTable(self,sdTable):
        """
        Returns all paths in the tree containing the given SD-Table

        :param sdTable: The name of the SD-Table
        :type  sdTable: string
        :returns:       A list of paths where the given SD-Table is in the SD-Table Level
        :rtype:         list
        """
        return filter(lambda x: x[0]==sdTable,self.__paths)

    def getPathsByProblemInstance(self, problemInstance):
        """
        Returns all paths in the tree containing the given SD-Table

        :param problemInstance: The name of the problem instance
        :type:                  string
        :returns:               A list of paths where the given problem instance is in the problem instance level
        :rtype:                 list
        """
        return filter(lambda x: x[1]==problemInstance, self.__paths)

    def getPathsByComputerAlgebraSystem(self, cas):
        """
        Returns all paths in the tree containing the given computer algebra system

        :param cas: The name of the computer algebra system
        :type  cas: string
        :returns:   A list of paths where the given computer algebra system is in the computer algebra system level
        :rtype:     list
        """
        return filter(lambda x: x[2]==cas, self.__paths)

    def __str__(self):
        """
        The string representation of a taskfolder tree. It has the following form::
          <Name Of SDTable 1>
              <Name of problem instance 1.1>
                  <Name of computer algebra system 1.1.1>
                  <Name of computer algebra system 1.1.2>
                  ...
              <Name of problem instance 1.2>
              ...
          <Name of SDTable 2>
          ...
        If it is empty, the output is just the string "Empty Tree"
        """
        if self.__paths == []:
            return "Empty Tree"
        pathsTemp = deepcopy(self.__paths)
        result = ""
        while len(pathsTemp)>0:
            entry = pathsTemp[0]
            result += entry[0] + ":\n"
            pathsWithSDTable = filter(lambda x: x[0] == entry[0],pathsTemp)
            for p in pathsWithSDTable:
                #Remove all the entries where the sdtable is the same as in entry
                pathsTemp.remove(p)
            while len(pathsWithSDTable)>0:
                entryPI = pathsWithSDTable[0]
                result += "    "+entryPI[1] + ":\n"
                pathsWithPI = filter(lambda x: x[1] == entryPI[1],pathsWithSDTable)
                for p in pathsWithPI:
                    pathsWithSDTable.remove(p)
                    result +="        "+p[2]+"\n"
        return result
