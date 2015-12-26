import os
from TaskFolderTree import TaskFolderTree
from TaskFolder import TaskFolder
from templates import comp
from Task import Task
from XMLResources import XMLResources
from MachineSettings import MachineSettings

class TaskFolderCreator(object):
    """
    This is a builder class to generate instances of taskfolders, if the task, the machine settings, and the xmlRessources are given.

    .. seealso: :mod:`TaskFolder <sdeval.classes.TaskFolder>`, :mod:`Task <sdeval.classes.Task>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def create(self,task, xmlRessources, machineSettings):
        """
        The function that creates the taskfolder using the information given in task, the xmlRessources, and the machineSettings.
        If the input is not valid, None is returned.
        
        :param                 task: The task associated to the taskfolder
        :type                  task: Task
        :param        xmlRessources: The interface to the XMLResources folder in Symbolic Data
        :type         xmlRessources: XMLResources
        :param      machineSettings: The machine settings of the target machine
        :type       machineSettings: MachineSettings
        :raises         ImportError: If there is a template not existing.
        :returns:                    An instance of taskfolder fitting to the given task.
        :rtype:                      TaskFolder or None
        """
        if (task == None or xmlRessources == None or machineSettings == None):
            return None
        if ((not isinstance(task, Task)) or
            (not isinstance(xmlRessources,XMLResources)) or (not
            isinstance(machineSettings,MachineSettings))):
            return None
        #Done input check
        pathOfSDEval = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]
        #The only thing we need to create is The taskfolderTree
        tft = TaskFolderTree()
        for s in task.getAssociatedSDTables():
            sdt = xmlRessources.loadSDTable(s)
            for p in filter(lambda x: x in sdt.listEntries(),task.getProblemInstances()):
                for c in task.getComputerAlgebraSystems():
                    #-------------------- complicated python stuff --------------------
                    # What happens here in the next lines:
                    # We load dynamically the builder for the problem instance given by p. Then we create the instance with the
                    # information we know. Those builder and problem instances are found in the module "probleminstances".
                    # After that, we search for the computation problem template for the computer algebra system c.
                    # We will use that function to generate code later for our TaskFolderTree.
                    fromXMLBuilderModule = __import__("probleminstances.%sFromXMLBuilder"%sdt.getName(),globals(),locals(),["%sFromXMLBuilder"%sdt.getName()])
                    builderfunc = getattr(fromXMLBuilderModule,"%sFromXMLBuilder"%sdt.getName())
                    creator = builderfunc(sdt)
                    pi = creator.build(p)
                    codegeneratingModule = __import__("templates.comp.%s.%s.template"%(task.getComputationProblem(),c),globals(),locals(),["generateCode"])
                    codeGenerator = codegeneratingModule.generateCode
                    #-------------------- end of complicated python stuff -------------
                    if task.getComputationProblem() == "GB_Z_lp":
                        tft.addCode(sdt.getName(),p,c,codeGenerator(pi.getVars(),pi.getBasis()))
                    elif task.getComputationProblem() == "GB_Fp_dp":
                        tft.addCode(sdt.getName(),p,c,codeGenerator(pi.getVars(),pi.getBasis(),pi.getCharacteristic()))
                    elif task.getComputationProblem() == "FA_Q_dp":
                        tft.addCode(sdt.getName(),p,c,codeGenerator(pi.getVars(),pi.getBasis(),pi.getUpToDeg()))
                    elif task.getComputationProblem() == "SOL_R_poly_sys":
                        tft.addCode(sdt.getName(),p,c,codeGenerator(pi.getVars(),pi.getBasis()))
        return TaskFolder(task,tft,machineSettings)
