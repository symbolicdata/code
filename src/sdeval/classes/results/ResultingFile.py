class ResultingFile(object):
    """
    This is a representation of an result file given as an output of the computer algebra systems
    on the problem instances.
    A resulting file is always associated to a computer algebra system, a problem instance and its
    SD-Table where it has been taken from. It consists of the output of the computer algebra system
    on this problem instance and the output of the time command on the target machine.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, pInstance, cas ,casOutput, time):
        """
        The constructor of the resulting file.

        :param   pInstance: The name of the problem instance that was used as input.
        :type    pInstance: string
        :param         cas: The name of the computer algebra system that was used to perform the calculations
        :type          cas: string
        :param   casOutput: The output of the computer algebra system
        :type    casOutput: string
        :param        time: A dictionary with the timings. It has three keys: real, user and sys. Its values are the corresponding times
        :type         time: dictionary
        """
        self.__pInstance = pInstance
        self.__cas       = cas
        self.__casOutput = casOutput
        self.__time      = time

    def getTimes(self):
        """
        Returns the time the calculation was running for before it ended. It is represented as dictionary

        :returns: The time the computer algebra system needed for that problem instance
        :rtype:   dictionary
        """
        return self.__time

    def getCASOutput(self):
        """
        Returns the output of the computer algebra system on the problem instance

        :returns: The output of the computer algebra system on the problem instance
        :rtype:   string
        """
        return self.__casOutput

    def getComputerAlgebraSystem(self):
        """
        Returns the computer algebra system, on which the calculations took place

        :returns: The name of the computer algebra system
        :rtype:   string
        """
        return self.__cas

    def getProblemInstance(self):
        """
        Returns the name of the problem instance where the input for the algorithm was taken from.

        :returns: The associated problem instance
        :rtype:   string
        """
        return self.__pInstance

    def __str__(self):
        """
        The String representation of the resulting file. It has the follwing form::
          Problem instance: <Name of problem instance>
          Computer algebra system: <Name of computer algebra system>
          Times:
              real: <realtime>
              user: <usertime>
               sys: <systime>
          Output:
            <the output of the computer algebra system>
        """
        result ="\
SD-Table: %s\n\
Problem instance: %s\n\
Computer algebra system: %s\n\
Times:\n\
    real: %s\n\
    user: %s\n\
     sys: %s\n\
Output:\n\
%s" % (self.__sdTable,
       self.__pInstance,
       self.__cas,
       self.__time['real'],
       self.__time['user'],
       self.__time['sys'],
       self.__casOutput)
        return result
