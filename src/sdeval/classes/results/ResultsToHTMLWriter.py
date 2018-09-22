import os
import HTML
import xml.etree.ElementTree as etree
import xml.dom.minidom as mdom


class ResultsToHTMLWriter(object):

    def createHTMLFromResultFiles(self, resultsFolder, casSystems):
        if resultsFolder is None:
            return None
        resultFiles = os.path.join(resultsFolder,"resultFiles")
        if resultFiles is None:
            return None

        output = ""
        for cas in casSystems:
            table = [['Problem Instance \\ Property']]
            propRow = table[0]

            problemInstances = next(os.walk(resultFiles))[1]
            for problemInstance in problemInstances:
                table.append([problemInstance])
                curRow = table[len(table) - 1]
                solutionPath = os.path.join(resultFiles, problemInstance, cas)
                if 'solutionInXML.xml' in next(os.walk(solutionPath))[2]:
                    solutionFile = os.path.join(solutionPath, "solutionInXML.xml")
                    root = etree.parse(solutionFile).getroot()
                    for prop in root:
                        propName = prop.tag

                        if len(prop.getchildren()) > 0:
                            propPath = os.path.join(solutionPath, "solutionInXMLSplit")
                            if not os.path.exists(propPath):
                                os.mkdir(propPath)
                            propFile = os.path.join(propPath, propName + ".xml")
                            propXML = mdom.parseString(etree.tostring(prop))\
                                    .toprettyxml("  ")
                            open(propFile, 'w').write(propXML)
                            propVal = HTML.link("xml", os.path.relpath(propFile, resultsFolder))
                        else:
                            propVal = prop.text

                        if propName not in propRow:
                            propRow.append(propName)

                        propIndex = propRow.index(propName)
                        while len(curRow) < propIndex:
                            curRow.append('')
                        if len(curRow) == propIndex:
                            curRow.append(propVal)
                        else:
                            curRow[propIndex] = propVal
            output += "<h1>" + cas + "</h1>\n" + HTML.table(table) + "\n"
        return output
