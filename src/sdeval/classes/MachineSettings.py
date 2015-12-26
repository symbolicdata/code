import xml.dom.minidom as dom

class MachineSettings(object):
    """
    This class represents the machine settings for the taskfolder. Machine settings are defined in
    the following way:

    Machine settings contain a collection of machine-specific constants; Those are:
      - For every used computer algebra system the command for executing it
      - The command on the target-machine for calculating the time an execution needs (time-command) with the
        needed options for that time command

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, casDict, timeCommand):
        """
        The initialisation of the MachineSettings. It gets a dictionary with the different computer
        algebra systems and their corresponding execution commands on the target-machine and
        the time command.

        :param     casDict: The dictionary with the computer algebra systems and their execution commands.
        :type      casDict: dictionary
        :param timeCommand: The time command on the target machine with the suitable options.
        :type  timeCommand: string
        """
        self.__casDict = casDict
        self.__timeCommand = timeCommand

    def getCASDict(self):
        """
        Returns the dictionary containing the computer algebra systems and their corresponding execution
        commands on the target-machine.

        :returns: The dictionary with computer algebra systems and their execution commands
        :rtype:   dictionary
        """
        return self.__casDict

    def getTimeCommand(self):
        """
        Returns the time command for the target machine

        :returns: The command to get timings on the target machine
        :rtype:   string
        """
        return self.__timeCommand

    def getCASCommand(self, cas):
        """
        Returns the execution command of the computer algebra system given by cas. If cas does not
        exist in the internal dictionary, None will be returned.

        :param cas: The requested computer algebra system
        :type  cas: string
        :returns:   The execution command for cas on the target-machine
        :rtype:     string or None
        """
        if not cas in self.__casDict.keys():
            return None
        return self.__casDict[cas]

    def toXML(self):
        """
        Returns an XML representation of the machine settings. It has the following form::

          <machinesettings>
            <casdictionary>
              <entry>
                <key>
                  "Name of computer algebra system"
                </key>
                <value>
                  "Execution command on target machine"
                </value>
              </entry>
              ...
            </casdictionary>
            <othervars>
              <timecommand>
                "The time command"
              </timecommand>
            </othervars>
          </machinesettings>

        :returns: An xml representation of the machine settings.
        :rtype:   xml.dom.minidom.Document
        """
        result = dom.Document()
        result.appendChild(result.createElement("machinesettings"))
        tempNode = result.firstChild
        #Creating timecommand section
        tempNodeTime = tempNode.appendChild(result.createElement("othervars"))
        tempNodeTime = tempNodeTime.appendChild(result.createElement("timecommand"))
        tempNodeTime.appendChild(result.createTextNode(self.__timeCommand))
        #creating casdict
        tempNode = tempNode.appendChild(result.createElement("casdictionary"))
        for c in self.__casDict:
            tempNodeEntry = tempNode.appendChild(result.createElement("entry"))
            tempNodeEntryKey = tempNodeEntry.appendChild(result.createElement("key"))
            tempNodeEntryKey.appendChild(result.createTextNode(c))
            tempNodeEntryValue = tempNodeEntry.appendChild(result.createElement("value"))
            tempNodeEntryValue.appendChild(result.createTextNode(self.__casDict[c]))
        return result

    def __str__(self):
        """
        The string representation of the machine settings. It has the following form::
            Computer algebra systems and commands:
                 <Computer algebra system 1> : <Execution Code 1>
                 <Computer algebra system 2> : <Execution Code 2>
                 ...
            Time Command: <Time Command>
        """
        result = "\
Computer algebra systems and commands:\n\
%s\n\
Time Command: %s\
" % ("\n".join("    "+v+" : "+self.__casDict[v] for v in self.__casDict), self.__timeCommand)
        return result;
