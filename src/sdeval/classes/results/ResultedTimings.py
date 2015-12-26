from Proceedings import Proceedings

class ResultedTimings(object):
    """
    This is a decorator class of the Proceedings class. It provides to every entry in the
    Proceedings lists an extra entry, namely an ResultingFile-Instance, if existent.

    .. seealso:: :mod:`Proceedings <sdeval.classes.results.Proceedings>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, proceedings = None, task = None, timeStamp = None):
        """
        This is the constructor of the ResultedTimings-Class. Either a proceedings instance is given and
        this will be used then, or a new Proceedings instance is generated given the task and the timeStamp.

        :param proceedings: The proceedings instance we want to decorate
        :type  proceedings: Proceedings
        :param      task: The task we want to create the Proceedings instance of
        :type       task: Task
        :param timeStamp: The timestamp of the execution of the task
        :type  timeStamp: string
        :raise   IOError: If neither a Proceedings instance nor a task or a timeStamp is given
        """
        if proceedings:
            self.__proceedings = proceedings
        elif task and timeStamp:
            self.__proceedings = Proceedings(task,timeStamp)
        else:
            raise IOError("In ResultedTimings constructor: Neither proceedings, nor a tuple of task and a timestamp are given.")
        self.__ResultingFileDict = {}

    def getTask(self):
        """
        Returns the name of the task of these proceedings.

        :returns: The name of the task of this ResultedTimings instance
        :rtype:   string
        """
        return self.__proceedings.getTask()

    def getTimeStamp(self):
        """
        Returns the timestamp of the calculations that are run.

        :returns: A the time stamp of the proceedings
        :rtype:   string
        """
        return self.__proceedings.getTimeStamp()

    def getProceedings(self):
        """
        Returns the Proceedings instance we are decorating here.

        :returns: The underlying Proceedings instance
        :rtype:   Proceedings
        """
        return self.__proceedings

    def getResultingFileDict(self):
        """
        Returns the dictionary with the saved timings.

        :returns: The internal dictionary with the saved timings
        :rtype:   dictionary
        """
        return self.__ResultingFileDict

    def getRUNNING(self):
        """
        Returns the currently running computations.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return map(lambda x: x+[None], self.__proceedings.getRUNNING())

    def getWAITING(self):
        """
        Returns the currently waiting computations.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return map(lambda x: x+[None], self.__proceedings.getWAITING())

    def getCOMPLETED(self):
        """
        Returns the completed computations.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return map(lambda x: x + [None] if str(x) not in self.__ResultingFileDict
               else x + [self.__ResultingFileDict[str(x)]],self.__proceedings.getCOMPLETED())

    def getERROR(self):
        """
        Returns the computations that were causing an error.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return map(lambda x: x + [None] if str(x) not in self.__ResultingFileDict
               else x+ [self.__ResultingFileDict[str(x)]],self.__proceedings.getERROR())

    def setRUNNING(self, tuple):
        """
        Adds a tuple to the list of currently running computations. It is assumed that the tuple is
        contained in the WAITING list, otherwise this function does nothing.

        :param tuple: A tuple of the form (problem instance, computer algebra system)
        :type  tuple: list
        """
        self.__proceedings.setRUNNING(tuple[:2])

    def setCOMPLETED(self,tuple,timings):
        """
        Adds a tuple to the list of completed computations. It is assumed that the tuple is
        contained in the RUNNING list, otherwise this function does nothing.

        :param   tuple: A tuple of the form (problem instance, computer algebra system)
        :type    tuple: list
        :param timings: The resulted times from the computations
        :type  timings: dict
        """
        self.__proceedings.setCOMPLETED(tuple[:2])
        self.__ResultingFileDict[str(tuple[:2])] = timings
