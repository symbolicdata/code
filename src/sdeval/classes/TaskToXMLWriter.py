import xml.dom.minidom as dom

class TaskToXMLWriter(object):
    """
    This is a builder class that creates an xml string representing a given task.

    .. seealso: :mod:`Task <sdeval.classes.Task>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def createXMLFromTask(self, task, xmlRessources):
        """
        Returns an XML-Representation of the Task. This representation has the following form::

          <task>
            <name>
              "The Taskname"
            </name>
            <computationproblem>
              "The computationproblem associated to the task"
            </computationproblem>
            <computeralgebrasystems>
              <computeralgebrasystem>
                "Name of computer algebra system 1"
              </computeralgebrasystem>
              <computeralgebrasystem>
                "Name of computer algebra system 2"
              </computeralgebrasystem>
              ...
            </computeralgebrasystems>
            <sdtables>
              <sdtable>
                <tablename>
                  "Name of the sdtable"
                </tablename>
                <probleminstances>
                  <probleminstance>
                    "Name of the problem instance"
                  </probleminstance>
                  ...
                </probleminstances>
              </sdtable>
              ...
            </sdtables>

        :param          task: The task we want to have the xml representation of
        :type           task: Task
        :param xmlRessources: The Folder where we can find the different SD-Tables and where we can check the entries
        :type  xmlRessources: XMLRessources
        :returns:             An xml-representation of the task
        :rtype:               xml.dom.minidom.Document
        """
        result = dom.Document()
        result.appendChild(result.createElement("task"))
        tempNode = result.firstChild
        #Adding the name
        tempNodeName = tempNode.appendChild(result.createElement("name"))
        tempNodeName.appendChild(result.createTextNode(task.getName()))
        #Adding the computation problem
        tempNodeCompProb = tempNode.appendChild(result.createElement("computationproblem"))
        tempNodeCompProb.appendChild(result.createTextNode(task.getComputationProblem()))
        #Adding the computer algebra systems
        tempNodeCASs = tempNode.appendChild(result.createElement("computeralgebrasystems"))
        for c in task.getComputerAlgebraSystems():
            tempCasNode = tempNodeCASs.appendChild(result.createElement("computeralgebrasystem"))
            tempCasNode.appendChild(result.createTextNode(c))
        #Adding the SD Tables
        tempNode = tempNode.appendChild(result.createElement("sdtables"))
        for s in task.getAssociatedSDTables():
            tempSDTableNode = tempNode.appendChild(result.createElement("sdtable"))
            tempSDTableNodeName = tempSDTableNode.appendChild(result.createElement("tablename"))
            tempSDTableNodeName.appendChild(result.createTextNode(s))
            tempSDTablePIsNode = tempSDTableNode.appendChild(result.createElement("probleminstances"))
            for p in filter(lambda x: x in xmlRessources.loadSDTable(s).listEntries(),task.getProblemInstances()):
                tempSDTablePINodeName = tempSDTablePIsNode.appendChild(result.createElement("probleminstance"))
                tempSDTablePINodeName.appendChild(result.createTextNode(p))
        return result
