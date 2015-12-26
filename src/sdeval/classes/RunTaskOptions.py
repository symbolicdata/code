class RunTaskOptions(object):
    """
    This class handles the options given when calling runTasks.py.
    It is a collection of the following data:
    - Maximum CPU Time available for each computation
    - Maximum Memory available for each computation
    - Maximum amount of computations that should be run in parallel.
    - Indicator, if runTask.py was called to finish an uncompleted job
    
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """
    
    def __init__(self, maxCPU=None, maxMem=None, maxJobs=1, resume=False):
        """
        Constructor of RunTaskOptions. It can be called without any parameters; then we have:
        - No limit on CPU time resources
        - No limit on Memory resources.
        - Exactly one computation will be run at a time.
        - We are ot resuming any Task

        If any of the given numbers is less or equal to 0, a ValueError is raised.

        :param      maxCPU: The maximum CPU time in seconds for the computations
        :type       maxCPU: integer (>0)
        :param      maxMem: The maximum memory (in bytes) that a computation is allowed to use.
        :type       maxMem: integer (>0)
        :param     maxJobs: The maximum amount of computations that shall be run in parallel.
        :type      maxJobs: integer (>0)
        :param      resume: Indicator if an uncompleted task is being resumed.
        :type       resume: bool
        :raises ValueError: If any of the above parameters do not fit the required type,
                            a ValueError is raised.
        """
        if maxCPU != None:
            if int(maxCPU)<=0:
                raise ValueError("The maximum CPU time was not a positive integer")
            self.__maxCPU = int(maxCPU)
        else:
            self.__maxCPU = None
        if maxMem != None:
            if int(maxMem)<=0:
                raise ValueError("The maximum memory limit was not a positive integer")
            self.__maxMem = int(maxMem)
        else:
            self.__maxMem = None
        if int(maxJobs)<=0:
           raise ValueError("The maximum amount of jobs was not a positive integer")
        self.__maxJobs = int(maxJobs)
        if type(resume)!=bool:
            raise ValueError("The flag whether we resume a task or not should be of boolean type")
        self.__resume = resume


    def getMaxMem(self):
        """
        Returns the maximum amount of memory each computation is allowed to use.

        :returns: The maximum amount of memory (in bytes) each computation is allowed to use.
        :rtype:   integer
        """
        return self.__maxMem

    def getMaxCPU(self):
        """
        Returns the maximum amount of CPU time each computation is allowed to use.

        :returns: The maximum amount of CPU time (in seconds) each computation is allowed to use.
        :rtype:   integer
        """
        return self.__maxCPU

    def getMaxJobs(self):
        """
        Returns the maximum amount of computations that can be run in parallel.

        :returns: The maximum amount of parallel computations.
        :rtype:   integer
        """
        return self.__maxJobs

    def getResume(self):
        """
        Returns the flag if the task is being resumed or not.

        :returns: The flag if the task was stopped in between and is resumed.
        :rtype:   bool
        """
        return self.__resume

    def setResume(self, newValue):
        """
        Set the flag if the task has been resumed to the provided new value.

        :param newValue: The new value for the `resume`-flag
        :type  newValue: bool
        :raises TypeError: if input parameter was not boolean
        """
        if type(newValue)!=bool:
            raise TypeError("Incorrect type for newValue")
        self.__resume = newValue

    def __str__(self):
        """
        Returns the string representation of the RunTaskOptions instance.
        It looks like the following::

          RunTask Options:
           * Maximum CPU time for each computation (in seconds): `maxCPU`
           * Maximum memory consumption for each computation: `maxMem`
           * Maximum amount of computations that can be run in parallel: `maxJobs`
           * Task has beein interrupted before and is now being resumed: `resume`

        If maxCPU or maxMem are not specified by the user, the function replaces maxCPU resp. maxMem
        above by the string "N.A."
        
        :returns: String representation of the RunTaskOptions instance.
        :rtype:   string
        """
        result = """RunTask Options:
* Maximum CPU time for each computation (in seconds): %s
* Maximum memory consumption for each computation (in Bytes): %s
* Maximum amount of computations that can be run in parallel: %i
* Task has been interrupted before and is now being resumed: %r""" % ("N.A." if self.getMaxCPU()==None else str(self.getMaxCPU()),
                                                                       "N.A." if self.getMaxMem()==None else str(self.getMaxMem()),
                                                                       self.getMaxJobs(),
                                                                       self.getResume())
        return result
