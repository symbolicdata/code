from ComputationProblem import ComputationProblem
import os

class FA_Q_dp(ComputationProblem):
    """
    This computation problem represents the computation of a Groebner basis in a free algebra
    with basedomain as the rational numbers and the degree reverse lexicographical ordering as
    ordering.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """
    __associatedTables = ["FreeAlgebras"]
    """
    The tables containing problem instances that can be used as input for this computation problem
    """
    __name             = "FA_Q_dp"
    """
    The name of the computation problem in the comp folder of symbolic data
    """
    __possibleCASs     = []

    def __init__(self):
        """
        The constructor of the problem instance FA_Q_dp. It checks the templates folder, which
        computer algebra systems are possible to use for that computation problem.
        """
        sdEvalPath = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]
        self.__possibleCASs = filter(lambda x: os.path.isdir(os.path.join(sdEvalPath,"templates","comp",self.__name,x)) ,
                                     os.listdir(os.path.join(sdEvalPath,"templates","comp",self.__name)))

    def getPossibleComputerAlgebraSystems(self):
        """
        Overloading of the function given in ComputationProblem. It lists all computeralgebra
        systems, that provide algorithms to solve this computation problem.

        :returns: A list of names of computer algebra systems.
        :rtype:   list
        """
        return self.__possibleCASs

    def getAssociatedTables(self):
        """
        Overloading the function given in ComputationProblem. It lists all SD-Tables that
        contain problem instances which can be used as input for algorithms solving this computation
        problem.

        :returns: All SD-Tables with suitable problem instances
        :rtype:   list
        """
        return self.__associatedTables

    def getName(self):
        """
        Returns the name of this computation problem as it is given in the comp-table.

        :returns: The name of the computation problem.
        :rtype:   string
        """
        return self.__name

    def addToAssociatedTables(self,associatedTable):
        """
        This method adds a SymbolicData-Table to the list of associated tables to this
        problem. It should contain problem instances that can be used as input for that specific
        computation.

        This function is meant to be used for prototyping new problem instances for SDEval and if they can be used,
        they will be added fixed to the class variable representing the list of associated tables.

        :param associatedTable: The name of the table the user wants to add
        :type  associatedTable: string
        """
        if not associatedTable in self.__associatedTables:
            self.__associatedTables.append(associatedTable)

    def addToComputerAlgebraSystems(self,cas):
        """
        This method adds a computer algebra system to the list of computer algebra systems that
        provide algorithms to solve this specific computation problem.

        This function is meant to be used for checking new computer algebra systems for that computation problem and if they can be used
        in a stable way, they will be added fixed to the class variable representing the list of possible computer algebra systems.

        :param cas: The name of the computer algebra system
        :type  cas: string
        """
        if not cas in self.__possibleCASs:
            self.__possibleCASs.append(cas)
