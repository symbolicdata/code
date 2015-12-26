#!/usr/bin/env python2
#.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>

"""
!!DEPRECATED!!
This module contains routines for creating tasks which will then be run on another machine.
This file expects a path for the XML-Data of the symbolic data project as parsing argument.
After that the interactive user mode will be started, where a user can decide which calculation
he wants to perform on which computer algebra system with which input data. After that,
an export folder will be created. For details read the descriptions of the particular functions.
.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
"""

#-------------------- Initialization Stuff --------------------

from optparse import OptionParser
from classes.XMLRessources import XMLRessources
from classes.Task import Task
from classes.TaskFolderCreator import TaskFolderCreator
from classes.MachineSettings import MachineSettings
import os

#PARSING and initializing the interface to the XMLRessources folder

parser = OptionParser("create_tasks.py [options] Arguments")
parser.add_option("-s", "--source", dest="xmldatapath", help="The complete path to XML-Data")
                                                        #We need the loacation
                                                        #of our XML-Data
(opts, args) = parser.parse_args()

stdxmlDataPathDir = os.path.join("..", "..", "data", "XMLResources")

if (len(args) == 0): # We need at least one argument
    if not os.path.isdir(stdxmlDataPathDir):
        print "This program needs at least one argument, namely the path to the XMLRessources folder"
        sys.exit(-2)
    else:
        xmlDataPath = os.path.realpath(stdxmlDataPathDir)
else:
    xmlDataPath = os.path.realpath(args[0])

xmlres = XMLRessources(xmlDataPath)

#FIND OUT SUPPORTED COMPUTATION PROBLEMS:
#They are simply the ones taht are in classes/templates/comp
sdEvalPath = os.path.realpath(os.path.dirname(__file__))
suppComputationProblems = filter(lambda x: os.path.isdir(os.path.join(sdEvalPath,"classes","templates","comp",x)),
                                 os.listdir(os.path.join(sdEvalPath,"classes","templates","comp")))

#-------------------- Initialization stuff ends ----------

# -------------------- Interactive user mode --------------------

operation = raw_input("What operation do you want to execute? ")
while suppComputationProblems.count(operation) == 0:
    print "Possible inputs:"
    print "\n".join(el for el in suppComputationProblems)
    operation = raw_input("Choose your operation: ")
compProbInstanceModule = __import__("classes.computationproblems.%s"%operation,globals(),locals(),[operation])
compProbInstanceClass = getattr(compProbInstanceModule,operation)
cpInstance = compProbInstanceClass()
piSDTables = map(lambda x: xmlres.loadSDTable(x),cpInstance.getAssociatedTables())
chosenProblemInstances = []
completeProblemList = []
for x in piSDTables:
    completeProblemList += x.listEntries()
flag = True
while (flag):
    problem = raw_input("Now choose a concrete problem you wish to deal with: ")
    while completeProblemList.count(problem) == 0:
         print "Possible inputs:"
         print "\n".join(el for el in filter(lambda x: x not in chosenProblemInstances,completeProblemList))
         problem = raw_input("Choose your problem: ")
    if not problem in chosenProblemInstances:
        chosenProblemInstances.append(problem)
    tmp = raw_input("Type \"y\" if you want to add further problems: ")
    if tmp !="y":
        flag = False
casList = cpInstance.getPossibleComputerAlgebraSystems()
CASs = []
flag = True
while (flag):
    CAS = raw_input("On which computer algebra system do you want to execute your calculation? ")
    while casList.count(CAS) == 0:
        print "Possible inputs:"
        print "\n".join(el for el in filter(lambda x: x not in CASs,casList))
        CAS = raw_input("Choose your computer algebra system: ")
    if not CAS in CASs:
        CASs.append(CAS)
    tmp = raw_input("Type \"y\" if you want to add further computer algebra systems: ")
    if tmp !="y":
        flag = False
name = raw_input("Please choose the name for that task: ")
while name =="":
    print "The name shall not be the empty string!"
    name = raw_input("Please choose the name for that task: ")
#Now, we have all information to create the task
theTask = Task(name, cpInstance.getName(), map(lambda x: x.getName(),piSDTables),chosenProblemInstances,CASs)
casDict = {}
for c in CASs:
    command = raw_input("Command for executing %s on the target-machine: "%c)
    casDict[c] = command
command = raw_input("The time command name on the target machine: ")
ms = MachineSettings(casDict, command)
#Now we create the taskfolder.
tf = TaskFolderCreator().create(theTask,xmlres,ms)
pathToSaveInp = raw_input("Now choose to which folder the taskfolder shall be exported: ")
while not os.path.isdir(pathToSaveInp):
    pathToSaveInp = raw_input("Path not valid. Please choose another one: ")
tf.write(pathToSaveInp,xmlres)
print "Creation of task successful. Goodbye."
