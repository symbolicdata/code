from MachineSettings import MachineSettings
import xml.dom.minidom as dom

class MachineSettingsFromXMLBuilder(object):
    """
    Creates in instance of the class MachineSettings from an xmlstring

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def build(self, xmlRaw):
        """
        The main command in this class. Given an raw xml-String containing an MachineSettings-instance.
        It creates an instance of type MachineSettings associated to the xml-string and returns it.

        :param   xmlRaw: The xml-Representation of the Machine Settings.
        :type    xmlRaw: string
        :raises IOError: If something is wrong with the XMLstring this exception is raised.
        """
        try:
            xmlTree = dom.parseString(xmlRaw)
        except:
            raise IOError("Could not parse the given string as XML-Instance")
        timeCommand = str(((xmlTree.getElementsByTagName("timecommand")[0]).firstChild.data)).strip()
        casDictNodes = xmlTree.getElementsByTagName("casdictionary")[0]
        casDict = {}
        for c in casDictNodes.childNodes:
            if c.nodeType == dom.Node.TEXT_NODE:
                #Not interesting
                continue
            for k in c.childNodes:
                if k.nodeType == dom.Node.TEXT_NODE:
                    continue
                if k.nodeName == "key":
                    key = str(k.firstChild.data).strip()
                else:
                    value = str(k.firstChild.data).strip()
            casDict[key] = value
        return MachineSettings(casDict,timeCommand)
