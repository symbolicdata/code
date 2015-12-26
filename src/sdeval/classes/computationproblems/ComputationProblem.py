class ComputationProblem(object):
    """
    An abstract representation of a computation problem.
    A computation problem is a problem, which is specified in the SymbolicData
    table B{COMP}. In the context of sdeval we use them to specify, which computations
    should be performed on one problem instance (resp. which algorithm should be used)

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """
    def __init__(self):
        """
        As this class is meant to be pure abstract, an error will be raised if the user tries to make an
        instance of this ComputationProblem.

        :raises NotImplementedError: Always when you try to make an instance
        """
        raise NotImplementedError("You cannot make an instance of ComputationProblem as it is abstract!")

    def getAssociatedTables(self):
        """
        By childclasses of this class, this function must be overloaded, otherwise the exception given here is raised.
        Childclasses should return a list here that contains all names of SD-Tables which contain probleminstances for
        this computation problem.

        :returns: A list of SD-Table names, which contain probleminstances for this computation problem
        :rtype:   list
        :raises NotImplementedError: This error will be raised if the method was not overloaded.
        """
        NotImplementedError("You must overload the method getAssociatedTables if you inherit from ComputationProblem!")

    def getPossibleComputerAlgebraSystems(self):
        """
        By childclasses of this class, this function must be overloaded, otherwise the exception given here is raised.
        Childclasses should return a list here that contains all names of Computeralgebrasystems that provider suitable
        algorithms for the computation problem.

        :returns: A list of names of computer algebra systems that provide algorithms to solve the computation problem.
        :rtype:   list
        :raises NotImplementedError: This error will be raised if the method was not overloaded.
        """
        NotImplementedError("You must overload the method getPossibleComputerAlgebraSystems if you inherit from ComputationProblem!")

    def getName(self):
        """
        By childclasses of this class, this function must be overloaded, otherwise the exception given here is raised.
        Childclasses should return the name of the computation problem they are representing.

        :returns: A list of names of computer algebra systems that provide algorithms to solve the computation problem.
        :rtype:   list
        :raises NotImplementedError: This error will be raised if the method was not overloaded.
        """
        NotImplementedError("You must overload the method getName if you inherit from ComputationProblem!")

    def addToAssociatedTables(self,associatedTable):
        """
        Childclasses should use this method to add a SymbolicData-Table to the list of associated tables to this
        problem. It should contain problem instances that can be used as input for that specific
        computation.

        This function is meant to be used for prototyping new problem instances for SDEval and if they can be used,
        they will be added fixed to the class variable representing the list of associated tables.

        :param associatedTable: The name of the table the user wants to add
        :type  associatedTable: string
        """
        NotImplementedError("You must overload the method addToAssociatedTables if you inherit from ComputationProblem!")

    def addToComputerAlgebraSystems(self,cas):
        """
        Childclasses should use this method to add a computer algebra system to the list of computer algebra systems that
        provide algorithms to solve this specific computation problem.

        This function is meant to be used for checking new computer algebra systems for that computation problem and if they can be used
        in a stable way, they will be added fixed to the class variable representing the list of possible computer algebra systems.

        :param cas: The name of the computer algebra system
        :type  cas: string
        """
        NotImplementedError("You must overload the method addToComputerAlgebraSystems if you inherit from ComputationProblem!")
