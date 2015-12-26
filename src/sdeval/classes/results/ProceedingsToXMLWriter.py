import xml.dom.minidom as dom

class ProceedingsToXMLWriter(object):
    """
    This is a builder class that creates an xml string representing a given proceedings of a task.

    .. seealso:: :mod:`Proceedings <sdeval.classes.results.Proceedings>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def createXMLFromProceedings(self, proceedings):
        """
        Returns an XML-Representation of the Proceedings. This representation has the following form::

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
              "same as running"
            </completed>
            <error>
              "same as running"
            </error>
          </proceedings>

        :param    proceedings: The proceedings we want to have the xml representation of
        :type     proceedings: Proceedings
        :returns:              An xml-representation of the proceedings
        :rtype:                xml.dom.minidom.Document
        """
        result = dom.Document()
        result.appendChild(result.createElement("proceedings"))
        tempNode = result.firstChild
        #Adding the timestamp
        tempNodeTimeStamp = tempNode.appendChild(result.createElement("timestamp"))
        tempNodeTimeStamp.appendChild(result.createTextNode(proceedings.getTimeStamp()))
        #Adding taskname
        tempNodeTask = tempNode.appendChild(result.createElement("task"))
        tempNodeTask.appendChild(result.createTextNode(proceedings.getTask()))
        #Adding the WAITING list:
        tempNodeWaiting = tempNode.appendChild(result.createElement("waiting"))
        for w in proceedings.getWAITING():
            tempNodeEntry = tempNodeWaiting.appendChild(result.createElement("entry"))
            tempNodeEntryPI = tempNodeEntry.appendChild(result.createElement("probleminstance"))
            tempNodeEntryPI.appendChild(result.createTextNode(w[0]))
            tempNodeEntryCAS = tempNodeEntry.appendChild(result.createElement("computeralgebrasystem"))
            tempNodeEntryCAS.appendChild(result.createTextNode(w[1]))
        #Adding the RUNNING list:
        tempNodeRunning = tempNode.appendChild(result.createElement("running"))
        for w in proceedings.getRUNNING():
            tempNodeEntry = tempNodeRunning.appendChild(result.createElement("entry"))
            tempNodeEntryPI = tempNodeEntry.appendChild(result.createElement("probleminstance"))
            tempNodeEntryPI.appendChild(result.createTextNode(w[0]))
            tempNodeEntryCAS = tempNodeEntry.appendChild(result.createElement("computeralgebrasystem"))
            tempNodeEntryCAS.appendChild(result.createTextNode(w[1]))
        #Adding the COMPLETED list:
        tempNodeCompleted = tempNode.appendChild(result.createElement("completed"))
        for w in proceedings.getCOMPLETED():
            tempNodeEntry = tempNodeCompleted.appendChild(result.createElement("entry"))
            tempNodeEntryPI = tempNodeEntry.appendChild(result.createElement("probleminstance"))
            tempNodeEntryPI.appendChild(result.createTextNode(w[0]))
            tempNodeEntryCAS = tempNodeEntry.appendChild(result.createElement("computeralgebrasystem"))
            tempNodeEntryCAS.appendChild(result.createTextNode(w[1]))
        #Adding the ERROR list:
        tempNodeError = tempNode.appendChild(result.createElement("error"))
        for w in proceedings.getERROR():
            tempNodeEntry = tempNodeError.appendChild(result.createElement("entry"))
            tempNodeEntryPI = tempNodeEntry.appendChild(result.createElement("probleminstance"))
            tempNodeEntryPI.appendChild(result.createTextNode(w[0]))
            tempNodeEntryCAS = tempNodeEntry.appendChild(result.createElement("computeralgebrasystem"))
            tempNodeEntryCAS.appendChild(result.createTextNode(w[1]))
        return result

