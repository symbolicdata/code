from ProblemInstance import ProblemInstance

class ModPS(ProblemInstance):
    """
    The concrete problem instance ModPS from SymbolicData. It represents polynomial systems
    with coefficients in a finite field. Details on ModPS can be found in SymbolicData.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, name, sdTable,vars=None, basis=None, characteristic=None):
        """
        The constructor of an ModPS-Instance. The name and the SD-Table are needed for the superclass ProblemInstance.
        The other parameters are the vars used for the polynomial system, the basis containing polynomials and the characteristic of the basedomain.

        :param           name: The name of the ModPS-ProblemInstance
        :type            name: string
        :param        sdTable: The SDTable containing ModPS-Instances. This input will not be checked.
        :type         sdTable: SDTable
        :param           vars: A list of variables used in the INTP-System
        :type            vars: list
        :param          basis: The polynomials forming a basis of the INTP-System. This input will not be checked whether
                               there are polynomials using variables not in the list of variables.
        :type           basis: list
        :param characteristic: The characteristic of the basedomain
        :type  characteristic: unsigned int, prime-power
        """
        super(ModPS,self).__init__(name,sdTable)
        self.__vars              = vars
        self.__basis             = basis
        self.__characteristic    = characteristic

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

    def getCharacteristic(self):
        """
        Returns the characteristic of the basedomain.

        :returns: The characteristic of the basedomain.
        :rtype:   unsigned int, prime power
        """
        return self.__characteristic

    def __str__(self):
        """
        Returns a string representation of this ModPS-Entry. It has the following form::
            ModPS-Entry: <name of the Entry>
            Variables: <comma separated variables>
            Characteristic: <characteristic>
            basis:
            <poly1>
            <poly2>
            ...
        """
        result="ModPS-Entry: %s\nVariables: %s\nCharacteristic: %s\nbasis:\n%s" % (self.getName(), ",".join(self.__vars),self.__characteristic, "\n".join(self.__basis))
        return result

    def __del__(self):
        """
        TODO
        """
        pass
