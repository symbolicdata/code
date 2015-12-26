from Task import Task
import xml.dom.minidom as dom

class TaskFromXMLBuilder(object):
    """
    Creates in instance of the class Task from an xmlstring

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def build(self, xmlRaw):
        """
        The main command in this class. Given an raw xml-String containing an Task-instance.
        It creates an instance of type Task associated to the xml-string and returns it.

        :param   xmlRaw: The xml-Representation of the Task.
        :type    xmlRaw: string
        :raises IOError: If something is wrong with the XMLstring this exception is raised.
        """
        try:
            xmlTree = dom.parseString(xmlRaw)
        except:
            raise IOError("Could not parse the given string as XML-Instance")
        name = str(((xmlTree.getElementsByTagName("name")[0]).firstChild.data)).strip()
        compProblem = str(((xmlTree.getElementsByTagName("computationproblem")[0]).firstChild.data)).strip()
        casSystems = map(lambda x: str((x.firstChild.data)).strip(),xmlTree.getElementsByTagName("computeralgebrasystem"))
        sdTables = map(lambda x: str((x.firstChild.data)).strip(),xmlTree.getElementsByTagName("tablename"))
        probleminstances = map(lambda x: str((x.firstChild.data)).strip(),xmlTree.getElementsByTagName("probleminstance"))
        return Task(name,compProblem,sdTables,probleminstances,casSystems)
