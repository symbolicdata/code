import xml.dom.minidom as dom
from ResultedTimings import ResultedTimings
from ..Task import Task

class ResultedTimingsFromXMLBuilder(object):
    """
    This is a builder class that creates instance of the class ResultedTimings
    of a task given an XML string and a Task instance.

    .. seealso:: :mod:`ResultedTimings <sdeval.classes.results.ResultedTimings>`
    .. moduleauthor:: Albert Heinle <aheinle@uwaterloo.de>
    """

    def build(self, xmlRaw, task):
        """
        Returns an instance of ResultedTimings, given an xml-string and an instance of the associated task.
        The given string is assumed to have the following form::
          <?xml version="1.0" ?>
          <proceedings>
            <timestamp>
              "The timestamp"
            </timestamp>
            <task>
              "the name of the executed task"
            </task>
            <running>
              <entry>
                <probleminstance>
                  "A problem instance"
                </probleminstance>
                <computeralgebrasystem>
                  "A computer algebra system"
                </computeralgebrasystem>
              </entry>
            </running>
            <waiting>
              "same as running"
            </waiting>
            <completed>
              "same as running, but with"
               <timings>
                  <real>
                    "real time"
                  </real>
                  <user>
                    "user time"
                  </user>
                  <sys>
                    "sys time"
                  <sys>
                </timings>
            </completed>
            <error>
              "same as completed"
            </error>
          </proceedings>

        An IOError is raised if the XML instance was not valid.
        
        :param    xmlRaw: The xml-representation of the proceedings.
        :type     xmlRaw: string
        :param    task: The task associated to the given proceedings instance.
        :type     task: Task
        :returns: An instance of the ResultedTimings class
        :rtype:   ResultedTimings
        """
        try:
            xmlTree = dom.parseString(xmlRaw)
        except:
            raise IOError("Could not parse the given string as XML-Instance")
        try:
            timeStamp = str((xmlTree.getElementsByTagName("timestamp")[0]).firstChild.data).strip()
        except:
            raise IOError("Given XML instance did not have a timestamp entry")
        result = ResultedTimings(None, task,timeStamp)
        try:
            completedCalculations = xmlTree.getElementsByTagName("completed")[0]
            erroneousCalculations   = xmlTree.getElementsByTagName("error")[0]
        except:
            raise IOError("Could not find entries for completed resp. erroneous computations")
        #First dealing with all the completed calculations
        tempEntry = completedCalculations.firstChild
        while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
            tempEntry = tempEntry.nextSibling
        while tempEntry != None:
            try:
                cas = str((tempEntry.getElementsByTagName("computeralgebrasystem")[0]).firstChild.data).strip()
                pi  = str((tempEntry.getElementsByTagName("probleminstance")[0]).firstChild.data).strip()
                runTimes = tempEntry.getElementsByTagName("timings")[0]
                runTimeReal = str((runTimes.getElementsByTagName("real")[0]).firstChild.data).strip()
                runTimeUser = str((runTimes.getElementsByTagName("user")[0]).firstChild.data).strip()
                runTimeSys = str((runTimes.getElementsByTagName("sys")[0]).firstChild.data).strip()
                runTimesCollected = {"real":runTimeReal,"user":runTimeUser, "sys":runTimeSys}
            except:
                raise IOError("The entries in the list of completed calculations are not valid")
            result.setRUNNING([pi,cas])
            result.setCOMPLETED([pi,cas],runTimesCollected)
            tempEntry = tempEntry.nextSibling
            while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
                tempEntry = tempEntry.nextSibling
        #Now dealing with the erroneous calculations
        tempEntry = erroneousCalculations.firstChild
        while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
            tempEntry = tempEntry.nextSibling
        while tempEntry != None:
            try:
                cas = str((tempEntry.getElementsByTagName("computeralgebrasystem")[0]).firstChild.data).strip()
                pi  = str((tempEntry.getElementsByTagName("probleminstance")[0]).firstChild.data).strip()
                runTimes = tempEntry.getElementsByTagName("timings")[0]
                runTimeReal = str((runTimes.getElementsByTagName("real")[0]).firstChild.data).strip()
                runTimeUser = str((runTimes.getElementsByTagName("user")[0]).firstChild.data).strip()
                runTimeSys = str((runTimes.getElementsByTagName("sys")[0]).firstChild.data).strip()
                runTimesCollected = {"real":runTimeReal,"user":runTimeUser, "sys":runTimeSys}
            except:
                raise IOError("The entries in the list of erroneous computations were not valid.")
            result.setRUNNING([pi,cas])
            result.setERROR([pi,cas],runTimesCollected)
            tempEntry = tempEntry.nextSibling
            while (tempEntry != None and tempEntry.nodeType == dom.Node.TEXT_NODE):
                tempEntry = tempEntry.nextSibling
        return result
