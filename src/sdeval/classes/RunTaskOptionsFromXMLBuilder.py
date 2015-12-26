import xml.dom.minidom as dom
from RunTaskOptions import RunTaskOptions

class RunTaskOptionsFromXMLBuilder(object):
    """
    This is a builder class that creates an RunTaskOptions instance represented by the given
    XML-string given by the user.

    .. seealso: :mod:`RunTaskOptions <sdeval.classes.RunTaskOptions>`
    .. moduleauthor: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def build(self, rtoXMLString):
        """
        Given an XML string of the following form::
          <?xml version="1.0" ?>
          <RunTaskOptions>
            <maxCPU>`maxCPU`</maxCPU>
            <maxMem>`maxMem`</maxMem>
            <maxJobs>`maxJobs`</maxJobs>
            <resume>`resume`</resume>
          </RunTaskOptions>
        Then this function creates a RunTaskOptions instance given the information in this file.

        :param rtoXMLString: An XML representation of the RunTaskOptions.
        :type  rtoXMLString: string
        :returns: An instance of RunTaskOptions, represented by the XML string
        :rtype: RunTaskOptions
        :raises IOError: The XML-string was not valid XML or the expected key-value pairs were not available
        """
        try:
            xmlTree = dom.parseString(rtoXMLString)
        except:
            raise IOError("Could not parse the given string as XML-Instance")
        if (xmlTree.getElementsByTagName("maxCPU")[0]).hasChildNodes():
            maxCPU = str((xmlTree.getElementsByTagName("maxCPU")[0]).firstChild.data).strip()
        else:
            maxCPU = None
        if (xmlTree.getElementsByTagName("maxMem")[0]).hasChildNodes():
            maxMem = str((xmlTree.getElementsByTagName("maxMem")[0]).firstChild.data).strip()
        else:
            maxMem=None
        maxJobs = str((xmlTree.getElementsByTagName("maxJobs")[0]).firstChild.data).strip()
        resume = str((xmlTree.getElementsByTagName("resume")[0]).firstChild.data).strip()
        try:
            if (maxCPU!=None):
                maxCPU = int(maxCPU)
            if (maxMem != None):
                maxMem = int(maxMem)
            maxJobs = int(maxJobs)
            resume = bool(int(resume))
        except:
            raise IOError("Values for one of the following was not correctly typed: maxCPU, maxMem, maxJobs, resume.")
        return RunTaskOptions(maxCPU, maxMem, maxJobs,resume)
