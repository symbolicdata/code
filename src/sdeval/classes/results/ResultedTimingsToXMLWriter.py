from ProceedingsToXMLWriter import ProceedingsToXMLWriter

class ResultedTimingsToXMLWriter(object):
    """
    This is a builder class that creates an xml string representing a given resulted timings of a task.

    .. seealso:: :mod:`Proceedings <sdeval.classes.results.Proceedings>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def createXMLFromResultedTimings(self, resultedTimings):
        """
        Returns an XML-Representation of the ResultedTimings. This representation has the following form::

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

        :param    resultedTimings: The proceedings we want to have the xml representation of
        :type     resultedTimings: Proceedings
        :returns:                  An xml-representation of the proceedings
        :rtype:                    xml.dom.minidom.Document
        """
        writer = ProceedingsToXMLWriter()
        result = writer.createXMLFromProceedings(resultedTimings.getProceedings())
        #First the completed
        completed = result.getElementsByTagName("completed")[0]
        entries = completed.getElementsByTagName("entry")
        for e in entries:
            pi = (e.getElementsByTagName("probleminstance")[0]).firstChild.data
            cas = (e.getElementsByTagName("computeralgebrasystem")[0]).firstChild.data
            d = resultedTimings.getResultingFileDict()[str([pi,cas])]
            timingsNode = e.appendChild(result.createElement("timings"))
            for k in d:
                tempNode = timingsNode.appendChild(result.createElement(k))
                tempNode.appendChild(result.createTextNode(d[k]))
        #Now the ERROR files
        errors = result.getElementsByTagName("error")[0]
        entries = errors.getElementsByTagName("entry")
        for e in entries:
            pi = (e.getElementsByTagName("probleminstance")[0]).firstChild.data
            cas = (e.getElementsByTagName("computeralgebrasystem")[0]).firstChild.data
            d = resultedTimings.getResultingFileDict()[str([pi,cas])]
            timingsNode = e.appendChild(result.createElement("timings"))
            for k in d:
                tempNode = timingsNode.appendChild(result.createElement(k))
                tempNode.appendChild(result.createTextNode(d[k]))
        return result

