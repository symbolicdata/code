import xml.dom.minidom as dom

class RunTaskOptionsToXMLWriter(object):
    """
    This is a builder class that creates an XML instance representing the given
    RunTaskOptions given by the user.

    .. seealso: :mod:`RunTaskOptions <sdeval.classes.RunTaskOptions>`
    .. moduleauthor: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def createXMLFromRunTaskOptions(self, rto):
        """
        Returns an XML representation of the rto as instance of the RunTaskOptions class.
        This representation has the following form::
          <?xml version="1.0" ?>
          <RunTaskOptions>
            <maxCPU>`maxCPU`</maxCPU>
            <maxMem>`maxMem`</maxMem>
            <maxJobs>`maxJobs`</maxJobs>
            <resume>`resume`</resume>
          </RunTaskOptions>
        In case any of the values maxCPU or maxMem are None, the respective entry will be empty.

        :param rto: The instance of RunTaskOptions, from which we want to obtain an XML representation.
        :type  rto: RunTaskOptions
        :returns: XML representation of the given instance of RunTimeOptions
        :rtype: xml.dom.minidom
        """
        result = dom.Document()
        result.appendChild(result.createElement("RunTaskOptions"))
        tempNode = result.firstChild
        tempNodeMaxCPU = tempNode.appendChild(result.createElement("maxCPU"))
        tempNodeMaxMem = tempNode.appendChild(result.createElement("maxMem"))
        tempNodeMaxJobs = tempNode.appendChild(result.createElement("maxJobs"))
        tempNodeResume = tempNode.appendChild(result.createElement("resume"))
        if rto.getMaxCPU()!=None:
            tempNodeMaxCPU.appendChild(result.createTextNode(str(rto.getMaxCPU())))
        if rto.getMaxMem()!=None:
            tempNodeMaxMem.appendChild(result.createTextNode(str(rto.getMaxMem())))
        tempNodeMaxJobs.appendChild(result.createTextNode(str(rto.getMaxJobs())))
        tempNodeResume.appendChild(result.createTextNode(str(int(rto.getResume()))))
        return result
