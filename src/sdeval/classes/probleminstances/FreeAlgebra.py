from ProblemInstance import ProblemInstance

class FreeAlgebra(ProblemInstance):
    """
    The concrete problem instance FreeAlgebra from SymbolicData. It represents polynomial systems in a free algebra
    with integer coefficients. Details on FreeAlgebra can be found in SymbolicData.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, name, sdTable,vars=None, basis=None, uptoDeg=None):
        """
        The constructor of an FreeAlgebra-Instance. The name and the SD-Table are needed for the superclass ProblemInstance.
        The other parameters are the vars used for the polynomial system, the basis containing polynomials and the upToDegree-Entry.

        :param         name: The name of the FreeAlgebra-ProblemInstance
        :type          name: string
        :param      sdTable: The SDTable containing FreeAlgebra-Instances. This input will not be checked.
        :type       sdTable: SDTable
        :param         vars: A list of variables used in the FreeAlgebra-System
        :type          vars: list
        :param        basis: The polynomials forming a basis of the FreeAlgebra-System. This input will not be checked whether
                             there are polynomials using variables not in the list of variables.
        :type         basis: list
        :param      uptoDeg: The uptoDeg Entry.
        :type       uptoDeg: unsigned int
        """
        super(FreeAlgebra,self).__init__(name,sdTable)
        if (
                len(vars) == 0 or
                len(basis) == 0
            ):
            raise IOError("Either the variable list was empty, or the basis. Either way, the creation of an instance of FreeAlgebra was not possible.")
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
        Returns a string representation of this FreeAlgebra-Entry. It has the following form::
            FreeAlgebra-Entry: <name of the Entry>
            Variables: <comma separated variables>
            Up to degree: <uptoDeg>
            basis:
            <poly1>
            <poly2>
            ...
        """
        result="FreeAlgebra-Entry: %s\nVariables: %s\nUp to degree: %s\nbasis:\n%s" % (self.getName(), ",".join(self.__vars),self.__uptoDeg, "\n".join(self.__basis))
        return result

    def __del__(self):
        """
        TODO
        """
        pass
