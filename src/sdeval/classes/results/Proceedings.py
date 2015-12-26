class Proceedings(object):
    """
    This is a class representation of the proceedings.

    Proceedings contain information about the status of the execution
    of the files in the taskfolder.

    The status can be one of the following options:

      1) RUNNING
      2) WAITING
      3) COMPLETED
      4) ERROR

    The meanings of the status can be derived from their names. During
    the execution, we additionally write an html file with the
    visualization of the proceedings.
    """

    def __init__(self, task, timeStamp):
        """
        This is the constructor of the Proceedings. It gets a task and puts all the executions in the task into the
        waiting list as initialization.

        An execution is a touple of the follwing form: [Problem instance, Computer algebra system]

        :param      task: The current task
        :type       task: Task
        :param timeStamp: The timestamp of the execution of the task
        :type  timeStamp: string
        """
        self.__WAITING   = []
        self.__RUNNING   = []
        self.__COMPLETED = []
        self.__ERROR     = []
        self.__timeStamp = timeStamp
        self.__task      = task.getName()
        for p in task.getProblemInstances():
            for c in task.getComputerAlgebraSystems():
                self.__WAITING.append([p,c])


    def getTask(self):
        """
        Returns the name of the task of these proceedings.

        :returns: The name of the task of this proceedings instance
        :rtype:   string
        """
        return self.__task

    def getTimeStamp(self):
        """
        Returns the timestamp of the calculations that are run.

        :returns: A the time stamp of the proceedings
        :rtype:   string
        """
        return self.__timeStamp

    def getRUNNING(self):
        """
        Returns the currently running computations.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return self.__RUNNING

    def getWAITING(self):
        """
        Returns the currently waiting computations.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return self.__WAITING

    def getCOMPLETED(self):
        """
        Returns the completed computations.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return self.__COMPLETED

    def getERROR(self):
        """
        Returns the computations that were causing an error.

        :returns: A list of tuples of problem instances and computer algebra systems.
        :rtype:   list
        """
        return self.__ERROR

    def setRUNNING(self, tuple):
        """
        Adds a tuple to the list of currently running computations. It is assumed that the tuple is
        contained in the WAITING list, otherwise this function does nothing.

        :param tuple: A tuple of the form (problem instance, computer algebra system)
        :type  tuple: list
        """
        if tuple in self.__WAITING:
            self.__WAITING.remove(tuple)
            self.__RUNNING.append(tuple)

    def setCOMPLETED(self,tuple):
        """
        Adds a tuple to the list of completed computations. It is assumed that the tuple is
        contained in the RUNNING list, otherwise this function does nothing.

        :param tuple: A tuple of the form (problem instance, computer algebra system)
        :type  tuple: list
        """
        if tuple in self.__RUNNING:
            self.__RUNNING.remove(tuple)
            self.__COMPLETED.append(tuple)
