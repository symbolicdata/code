class Task(object):
    """
    This class represents a task in the sense of SDEval. It is defined
    in the following way:

    A task is always associated to a computation problem. A task
    contains a list of SD-Tables that contain problem instances that
    can be used as suitable input for algorithms solving the
    computation problem the task is associated to. From those
    SD-Tables a task contains a set of concrete problem instances.
    Moreover, a task contains a set of computer algebra systems, that
    provide algorithms to to solve the computation problem. All those
    sets in a task should not be empty. A task has also a name

    .. seealso:: :mod:`ComputationProblem <sdeval.classes.computationproblems.ComputationProblem>`, :mod:`SDTable <sdeval.classes.SDTable>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self,name, computationProblem, sdTables, problemInstances, computerAlgebraSystems):
        """
        This is the constructor of the class Task.
        It initializes the variables and checks whether the given sets are not empty.

        :param                   name: The name of the task
        :type                    name: string
        :param     computationProblem: The name of the computation problem the task is associated to
        :type      computationProblem: string
        :param               sdTables: A list of names of sdTables where the problem instances are taken from.
        :type                sdTables: list
        :param       problemInstances: A list of names of problem instances in this task
        :type        problemInstances: list
        :param computerAlgebraSystems: A list with computer algebra systems that are chosen to solve the computation problem
                                       associated with this task.
        :type  computerAlgebraSystems: list
        :raises               IOError: If one of the lists sdTables, problemInstances or computerAlgebraSystems is empty,
                                       this error is raised.
        """
        if len(sdTables)==0 or \
            len(problemInstances)==0 or \
            len(computerAlgebraSystems)==0:
            raise IOError("Task instance creation failed. One of the input lists was empty.")
        else:
            self.__name = name
            self.__computationProblem = computationProblem
            self.__sdTables = sdTables
            self.__problemInstances = problemInstances
            self.__computerAlgebraSystems = computerAlgebraSystems

    def getComputationProblem(self):
        """
        Returns the name of the computation problem associated with the task.

        :returns: The name of the computation problem associated with the task
        :rtype:   string
        """
        return self.__computationProblem

    def getAssociatedSDTables(self):
        """
        Returns the list of the to the computation problem associated SD-Tables

        :returns: A list of names of SD-Tables
        :rtype:   list
        """
        return self.__sdTables

    def getProblemInstances(self):
        """
        Returns a list of names of the problem instances the task deals with.

        :returns: A list of problem instances (Entries in SD-Tables)
        :rtype:   list
        """
        return self.__problemInstances

    def getName(self):
        """
        Returns the name of the task.

        :returns: The name of the task
        :rtype:   string
        """
        return self.__name

    def getComputerAlgebraSystems(self):
        """
        Returns the set of computeralgebra systems, that were chosen to solve the computation
        problem on the problem instances.

        :returns: A list of names of computer algebra systems
        :rtype:   list
        """
        return self.__computerAlgebraSystems

    def __str__(self):
        """
        Returns a string representation of the task. It has the follwing form::
          Task: <TaskName>
          Associated computation problem: <computation problem>
          Associated SD-Tables:
            <SDTable 1>
            <SDTable 2>
            ...
          Problem instances:
            <Problem instance 1>
            <Problem instance 2>
            ...
          Chosen computer algebra systems:
            <CAS 1>
            <CAS 2>
            ...
        """
        result ="\
Task:%s\n\
Associated computation problem: %s\n\
Associated SD-Tables:\n\
%s\n\
Problem instances:\n\
%s\n\
Chosen computer algebra systems:\n\
%s\n\
" % (self.__name,
     self.__computationProblem,
     "\n".join(self.__sdTables),
     "\n".join(self.__problemInstances),
     "\n".join(self.__computerAlgebraSystems))
        return result
