from Task import Task
from TaskFolderTree import TaskFolderTree
from MachineSettings import MachineSettings
from TaskToXMLWriter import TaskToXMLWriter
import os
import shutil

class TaskFolder(object):
    """
    Represents a taskfolder in the sense of SDEval. It is defined in
    the follwing way:

    A taskfolder is associated to a task. It contains:
      - The Task itself (taskInfo.xml)
      - For every probleminstance and for every computer algebra
        system the taskfolder contains one by the computer algebra
        system exutable file, that contains the computation steps to
        solve the computation problem the task is associated to.
      - An executable file runTasks.py to execute the computations.
      - The machine settings for the machine, where the task shall be
        executed on.

    If any one of the input parameters is not valid, the constructor raises an exception

    .. seealso: :mod:`Task <sdeval.classes.Task>`, :mod:`TaskFolderTree <sdeval.classes.TaskFolderTree>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def __init__(self, task, casExecFiles, machineSettings):
        """
        The constructor of the class TaskFolder.
        It gets the needed information to be able to create a taskfolder. That is the task itself,
        the executable files and the machine settings.

        :param            task: The task the taskfolder is associated to
        :type             task: Task
        :param    casExecFiles: A Tree with the executable files as leafs. The tree has the following structure::

                                         (root)
                                         /    \\
                                        ...   "Some SDTable"
                                                 \\
                                                "Some computer algebra system"
                                                    \\
                                                    "The executable code"
        :type     casExecFiles: TaskFolderTree
        :param machineSettings: The Machine Settings of the Machine we execute our code on
        :type  machineSettings: MachineSettings
        :raises: IOError
        """
        if (task==None or casExecFiles==None or machineSettings == None):
            raise IOError("One of the input parameters to Taskfolder was None")
        if (not isinstance(task, Task)):
            raise IOError("The input parameter task was not of type Task")
        if (not isinstance(casExecFiles, TaskFolderTree)):
            raise IOError("The input parameter casExecFiles was not of type TaskFolderTree")
        if (not isinstance(machineSettings, MachineSettings)):
            raise IOError("The input parameter machineSettings was not of Type MachineSettings")
        #From here on, we can assume that the Input is at least type-wise correct
        for p in casExecFiles.getAllPaths():
            if not p[0] in task.getAssociatedSDTables():
                raise IOError("CasExecution was not consistent with Task")
        for a in task.getProblemInstances():
            for b in task.getComputerAlgebraSystems():
                if len(filter(lambda x: x[1] == a and x[2]==b,casExecFiles.getAllPaths()))==0:
                    raise IOError("Some of the problems from the task are not existent in the taskfoldertree")
        self.__task = task
        self.__casExecFiles = casExecFiles
        self.__machineSettings = machineSettings


    def getTask(self):
        """
        Returns the task this Taskfolder instance is associated to.

        :returns: Associated Task
        :rtype:   Task
        """
        return self.__task

    def getExecFiles(self):
        """
        Returns the TaskFolderTree where the executable files are saved

        :returns: The TaskFolderTree with the executable files
        :rtype:   TaskFolderTree
        """
        return self.__casExecFiles

    def getMachineSettings(self):
        """
        Returns the machine settings for the target machine.

        :returns: The machine settings for the target-machine
        :rtype:   MachineSettings
        """
        return self.__machineSettings

    def write(self, path, xmlRessources):
        """
        Writes the TaskFolder into the specified directory path. If
        the name of the associated task is "xyz", the taskfolder will
        be called "xyzEXPORTFOLDER". If the path does not exist, an
        exception is raised.
        It furthermore has the following structure::

          + xyzEXPORTFOLDER
            - runTasks.py         //For Running the task
            - taskInfo.xml        //Saving the Task in XML-Structure
            - machinesettings.xml //The Machine Settings in XML form
            + classes
              //All classes of the SDEval project
            + casSources
                + "Some ProblemInstance"
                  + "Some computer algebra system"
                    - executablefile.sdc
                    - template_sol.py (optional)
                  + ...
                + ...
              + ...

        :param          path: The path where the export-folder shall be saved to.
        :type           path: string
        :param xmlRessources: The interface to the XML Ressources folder
        :type  xmlRessources: XMLResources
        :raise       IOError: If the given path does not exist.
        """
        if not os.path.isdir(path):
            raise IOError("In TaskFolder.write: The path given by " + str(path) + "does not exist!")
        #Getting the path of the SDEval folder
        pathOfSDEval = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]
        #Creating the export folder
        destPath = os.path.join(path,self.__task.getName()+"EXPORTFOLDER")
        os.mkdir(destPath)
        #Copy runTasks.py
        shutil.copy(os.path.join(pathOfSDEval,"runTasks.py"),destPath)
        #Copy compareResults.py
        shutil.copy(os.path.join(pathOfSDEval,"compareResults.py"),destPath)
        #writing taskInfo.xml
        tw = TaskToXMLWriter()
        taskTree = tw.createXMLFromTask(self.__task, xmlRessources)
        f = open(os.path.join(destPath,"taskInfo.xml"),"w")
        taskTree.writexml(f, "  ", "  ", "\n")
        f.close()
        #writing machinesettings.xml
        msTree = self.__machineSettings.toXML()
        f = open(os.path.join(destPath,"machinesettings.xml"),"w")
        msTree.writexml(f, "  ", "  ", "\n")
        f.close()
        #copying the classes folder
        shutil.copytree(os.path.join(pathOfSDEval,"classes"),os.path.join(destPath,"classes"))
        #Making the casSources folder
        os.mkdir(os.path.join(destPath,"casSources"))
        for t in self.__casExecFiles.getAllPaths():
            if not os.path.isdir(os.path.join(destPath,"casSources",t[1])):
                os.mkdir(os.path.join(destPath,"casSources",t[1]))
            os.mkdir(os.path.join(destPath,"casSources",t[1],t[2]))
            f = open(os.path.join(destPath,"casSources",t[1],t[2],"executablefile.sdc"),"w")
            f.write(t[3])
            f.close()
            #if template_sol does exist, it will also be copied into the folder with the executable File.
            if os.path.isfile(os.path.join(pathOfSDEval,"classes", "templates", "comp",
                                           self.__task.getComputationProblem(),t[2],"template_sol.py")):
                shutil.copy(os.path.join(pathOfSDEval,"classes", "templates", "comp",
                                           self.__task.getComputationProblem(),t[2],"template_sol.py"),
                                           os.path.join(destPath, "casSources", t[1],t[2]))
