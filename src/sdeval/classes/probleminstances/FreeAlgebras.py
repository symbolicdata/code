from ProblemInstance import ProblemInstance

class FreeAlgebras(ProblemInstance):
    """
    The concrete problem instance FreeAlgebras from SymbolicData. It represents polynomial systems in a free algebra
    with integer coefficients. Details on FreeAlgebras can be found in SymbolicData.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, name, sdTable,vars=None, basis=None, uptoDeg=None):
        """
        The constructor of an FreeAlgebras Instance. The name and the SD-Table are needed for the superclass ProblemInstance.
        The other parameters are the vars used for the polynomial system, the basis containing polynomials and the upToDegree-Entry.

        :param         name: The name of the FreeAlgebras ProblemInstance
        :type          name: string
        :param      sdTable: The SDTable containing FreeAlgebras Instances. This input will not be checked.
        :type       sdTable: SDTable
        :param         vars: A list of variables used in the FreeAlgebras System
        :type          vars: list
        :param        basis: The polynomials forming a basis of the FreeAlgebras System. This input will not be checked whether
                             there are polynomials using variables not in the list of variables.
        :type         basis: list
        :param      uptoDeg: The uptoDeg Entry.
        :type       uptoDeg: unsigned int
        """
        super(FreeAlgebras,self).__init__(name,sdTable)
        self.__vars              = vars
        self.__basis             = basis
        self.__uptoDeg           = uptoDeg

    def getVars(self):
        """
        Returns the variables used in the polynomial system.

        :returns: The variables of the polynomial system
        :rtype:   list
        """
        return self.__vars

    def getBasis(self):
        """
        Returns the basis of the integer polynomial system.

        :returns: The basis of the integer polynomial system.
        :rtype:   list
        """
        return self.__basis

    def getUpToDeg(self):
        """
        Returns the uptoDeg-value.

        :returns: The uptoDeg-value
        :rtype:   unsigned int
        """
        return self.__uptoDeg

    def __str__(self):
        """
        Returns a string representation of this FreeAlgebras Entry. It has the following form::
            FreeAlgebras-Entry: <name of the Entry>
            Variables: <comma separated variables>
            Up to degree: <uptoDeg>
            basis:
            <poly1>
            <poly2>
            ...
        """
        result="FreeAlgebras-Entry: %s\nVariables: %s\nUp to degree: %s\nbasis:\n%s" % (self.getName(), ",".join(self.__vars),self.__uptoDeg, "\n".join(self.__basis))
        return result

    def __del__(self):
        """
        TODO
        """
        pass
