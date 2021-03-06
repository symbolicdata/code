"""
This is the template for extracting the solution for the computation problem of computing
real solution of a polynomial system of equations RR from the output of the computer
algebra system Singular.

.. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
"""

import xml.dom.minidom as dom
import re

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def extractSolution(outpString):
    """
    This function extracts the real solutions of a polynomial system
    computed by Singular, using the executable code that was
    generated by the template in the same folder on a certain
    instance.

    It returns a string representation of the solution in XML-format.
    The XML-string will be given as follows::

      <SOL_R_poly_sys_SOL>
        <solutions>
          <solution>
            <equal>
              <varName>variable name</varName>
              <value>solution value</value>
            </equal>
            ...
          </solution>
          ...
        </solutions>
      </SOL_R_poly_sys_SOL>

    If there is no solution given, or something is wrong with the given string,
    a ValueError is raised.

    :param outpString: The String that was returned by the Singular-execution
    :type  outpString: str
    :returns: XML-Representation of the solution.
    :rtype: str
    :raises: ValueError
    """
    if (type(outpString) != str):
        raise ValueError("Wrong Type of argument. String type expected.")
    solBeginStr = "=====Solution Begin====="
    solEndStr   = "=====Solution End====="
    solBeginPos = outpString.index(solBeginStr) + len(solBeginStr)
    solEndStrPos   = outpString.index(solEndStr)
    solStr = outpString[solBeginPos:solEndStrPos].strip()
    solEntries = solStr.split('\n')
    solEntries = map(lambda x: x.strip(),solEntries)
    solEntries = filter(lambda x: x!='',solEntries)
    #From here on, we can assume that we are dealing with a valid
    #string.
    #Construction of the XML-Document
    result = dom.Document()
    result.appendChild(result.createElement("SOL_R_poly_sys_SOL"))
    tempNode = result.firstChild
    #Adding the basis
    tempNodeSolutions = tempNode.appendChild(result.createElement("solutions"))
    for b in solEntries:
        tempSolutionNode =\
            tempNodeSolutions.appendChild(result.createElement("solution"))
        solutionsList = map(lambda x: x.split("="),b.split(","))
        solutionsList = map(lambda x: [x[0].strip(),x[1].strip()],
                            solutionsList)
        for c in solutionsList:
            tempEqualNode =\
              tempSolutionNode.appendChild(result.createElement("equal"))
            tempVarnameNode =\
              tempEqualNode.appendChild(result.createElement("varName"))
            tempValueNode =\
              tempEqualNode.appendChild(result.createElement("value"))
            tempVarnameNode.appendChild(result.createTextNode(c[0]))
            tempValueNode.appendChild(result.createTextNode(c[1]))
    return result.toprettyxml("  ")

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------
