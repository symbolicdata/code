#!/usr/bin/env python2
# -*- coding: iso-8859-1 -*-

"""
The GUI for SDEVAL

Here, the user can create a task via a graphical user interface. The idea is the
following:
At first, he decides which kind of problem he wants to deal with.
After that, he chooses concrete Problems from the database of Symbolicdata.
The program will use the tables corresponding to the given problems.

In the End, the user specifies, which computer algebra system he or she wants to
use. By now, we offer the choice between
 - Singular
 - Maple
 - Maple
 - GAP

With some machine settings the user should set, the creation of the task can start
and there will be a folder created in the end that contains code for the different
computer algebra systems.
.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
"""

#For the readability:
dictComputationProblem={"FA_Q_dp":"Groebner basis over free algebra",
                        "GB_Z_lp":"Groebner basis commutative",
                        "GB_Fp_dp":"Groebner basis commutative (finite field)"}

import os # This is for the check if the path does exist in the next step
import shutil

from classes.XMLRessources import XMLRessources
from classes.MachineSettings import MachineSettings
from classes.TaskFolderCreator import TaskFolderCreator
from classes.Task import Task

#### GUI Stuff
import Tkinter
import tkMessageBox
import tkFileDialog
import xml.dom.minidom as dom


################################################################################
#First of all, check, if the directory with the XMLRessources of Symbolicdata
#does exist in the expected path "../XMLResources/". If not, the
#user will be asked later for the path.

stdxmlDataPathDir = os.path.join("..", "..", "data", "XMLResources")
isXMLRessourcesDirectory = \
    os.path.isdir(stdxmlDataPathDir)
    # To make it more platform independent. What stands here would be in unix terms
    #../../../OWLData/XMLResources.

xmlDataPath = None
if (isXMLRessourcesDirectory):
  xmlDataPath = os.path.realpath(stdxmlDataPathDir)

################################################################################
#Lets start with the gui itself.

class CreateTasksGui:
  def __init__(self):
    self.createMainWindow()
    self.createMainMenu()
    self.createMainFrame()
    self.createWindowProblemSelect()
    self.currentWindow = "ProblemSelect"# Other possibilities are TableSelect and CASSelect
    self.checkXMLRessourcesDir()
    self.input_operation = None
    self.input_problemClass = None
    self.input_problems = []
    self.input_compAlgSystems = []
    #self.createTableSelect()
    #self.createCASSelect()
    Tkinter.mainloop()


  ##################################################
  ###### Initialization Stuff
  ##################################################
  def createMainWindow(self):
    self.mainWindow = Tkinter.Tk()
    #self.mainWindow.resizable(width = False, height = False)
    self.mainWindow.title("SDEval -- Create Tasks")

  def createMainMenu(self):
    self.menuBar = Tkinter.Menu(self.mainWindow)
    self.helpMenu = Tkinter.Menu(self.menuBar,tearoff=0)
    self.helpMenu.add_command(label="About SDEval", command=self.thanksPopup)
    self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
    self.mainWindow.config(menu=self.menuBar)

  def thanksPopup(self):
    """
    In the top menubar, there is an option "About SDEval". If you click on it, a
    popup will show up with an information about the project. The showing of the
    popup is made by this window.
    """
    tkMessageBox.showinfo("About SDEVAL", "SDEval is developed at \
Lehrstuhl D für Mathematik, RWTH Aachen University.\
\n\nSpecial thanks to DFG (Deutsche Forschungs Gesellschaft)\
who funded the project (Schwerpunkt 1489)")

  def createMainFrame(self):
    self.mainFrame=Tkinter.Frame(self.mainWindow)
    self.mainFrame.grid();

  def checkXMLRessourcesDir(self):
    global xmlDataPath
    validDir = False
    while not validDir:
      try:
        self.__xmlres = XMLRessources(xmlDataPath)
        validDir = True
      except:
        xmlDataPath = tkFileDialog.askdirectory(mustexist=True)
        validDir = False

  def fillListOfProblems(self):
    """
    In the second window, where the user chooses concrete problems he wants to
    deal with, this method fills the list of entries in the listbox.
    """

    chosenProblemInstances = []
    completeProblemList = []
    for x in self.input_SDTables:
      completeProblemList += x.listEntries()
    for entry in completeProblemList:
      self.lstbx_allProblems.insert(Tkinter.END,entry)
    if len(completeProblemList) != 0:
      self.lstbx_allProblems.select_set(0)

  # def initCASselect(self):
  #   #Fill the machine settings
  #   self.entry_GAP.insert(Tkinter.END, MS.CASpaths["GAP"])
  #   self.entry_Magma.insert(Tkinter.END,MS.CASpaths["Magma"])
  #   self.entry_Maple.insert(Tkinter.END,MS.CASpaths["Maple"])
  #   self.entry_Singular.insert(Tkinter.END,MS.CASpaths["Singular"])
  #   self.entry_Time.insert(Tkinter.END,MS.timeCommand)
  #   #check whether the Computer Algebra systems can handle the current problem:
  #   if self.input_operation=="FA_Q_dp.xml":
  #     self.cb_Maple.config(state = Tkinter.DISABLED)

  ##################################################
  #### Button Behaviours
  ##################################################

  def btnNextBehaviour(self):
    if (self.currentWindow == "ProblemSelect"):
      """
      User was in the first window, selected a problem and wants now to the tables
      to choose concrete instances.
      """
      #########
      #Read the entries and fill the variables with it
      self.input_operation = self.v.get()
      compProbInstanceModule = __import__("classes.computationproblems.%s"%self.input_operation,globals(),locals(),[self.input_operation])
      compProbInstanceClass = getattr(compProbInstanceModule,self.input_operation)
      self.cpInstance = compProbInstanceClass()
      self.input_SDTables = map(lambda x: self.__xmlres.loadSDTable(x),self.cpInstance.getAssociatedTables())

      #########
      #Creating the new window
      self.currentWindow = "TableSelect"
      self.mainFrame.destroy()
      self.createMainFrame()
      self.createTableSelect()
      self.fillListOfProblems()
    else:
      """
      The only other possibility is that the user is at the second window, and wants
      to move on to the third.
      """
      if self.lstbx_chosenProblems.size()<1:
        #Error message if the user has not selected a problem at all!
        tkMessageBox.showerror(title = "No Problem selected", message = "You have to choose at least one problem instance!")
      else:
        #######
        #Read entries and fill variables
        self.input_problems = self.lstbx_chosenProblems.get(0,Tkinter.END)
        ######
        #Create the new window
        self.currentWindow = "CASSelect"
        self.mainFrame.destroy()
        self.createMainFrame()
        self.createCASSelect()


  # def makeCASList(self):
  #   """
  #   In the last window, we have some computer algebra systems to select. This method
  #   returns a list of the selected Computer Algebra Systems.
  #   """
  #   result = []
  #   if self.var_GAP.get() == "Yes":
  #     result.append("GAP.xml")
  #   if self.var_Magma.get() == "Yes":
  #     result.append("Magma.xml")
  #   if self.var_Maple.get() == "Yes":
  #     result.append("Maple.xml")
  #   if self.var_Singular.get() == "Yes":
  #     result.append("Singular.xml")
  #   return result

  def btnCreateClick(self):
    #First, some checks if the Entries given by the user are valid
    ourCASs = filter(lambda x: self.var_CASs[x].get() == "Yes",self.var_CASs.keys())
    notAllCommandsThere = False
    for c in ourCASs:
      if self.entry_CASs[c].get().strip() == "":
        notAllCommandsThere = True
    if notAllCommandsThere:
      tkMessageBox.showerror(title = "Some commands missing", message="You must provide the commands for calling the computer algebra systems you want to call on your target machine.")
    elif self.entry_taskName.get().strip() == "":
      tkMessageBox.showerror(title = "No Taskname given", message="Your task must have a name.")
    elif self.entry_Time.get().strip() == "":
      tkMessageBox.showerror(title = "No time command given", message="You need to specify the time command on your target machine.")
    elif len(ourCASs)==0:
      tkMessageBox.showerror(title = "No Computer Algebra System selected", message="You have to select at least one computer algebra system")
    else:
      #Everything is fine. Start creating the Export Task folder
      exportFolder = tkFileDialog.askdirectory(mustexist = True, title = "Choose a directory where the Export Folder should be placed at.")
      theTask = Task(self.entry_taskName.get().strip(), self.cpInstance.getName(), map(lambda x: x.getName(),self.input_SDTables),self.input_problems,ourCASs)
      casDict = {}
      for c in ourCASs:
        casDict[c] = self.entry_CASs[c].get().strip()
      ms = MachineSettings(casDict, self.entry_Time.get().strip())
      #Now we create the taskfolder.
      tf = TaskFolderCreator().create(theTask,self.__xmlres,ms)
      tf.write(exportFolder,self.__xmlres)
      tkMessageBox.showinfo(title="Successful", message = "The task was successfully created.")
      self.mainWindow.destroy()

  def btnAddClick(self):
    """
    This method deals with the event, that the user adds a problem to his list
    of chosen problems.
    """
    if self.lstbx_allProblems.size()>0:
      #Add just makes sense if the size of the problem list is greater than 0
      self.lstbx_chosenProblems.insert(Tkinter.END,self.lstbx_allProblems.get(self.lstbx_allProblems.curselection()[0]))
      self.lstbx_allProblems.delete(self.lstbx_allProblems.curselection()[0])
      if self.lstbx_allProblems.size()>0:
        self.lstbx_allProblems.select_set(0)

  def btnRemoveClick(self):
    """
    If a problem in the current problem list is not that interesting how it seemed before
    the usere presses the button "remove" and this method will delete it from the list
    """
    if self.lstbx_chosenProblems.size()>0:
      if len(self.lstbx_chosenProblems.curselection())>0:
        self.lstbx_allProblems.insert(Tkinter.END,self.lstbx_chosenProblems.get(self.lstbx_chosenProblems.curselection()[0]))
        self.lstbx_chosenProblems.delete(self.lstbx_chosenProblems.curselection()[0])

  ##################################################
  #### Events
  ##################################################
  def listBoxAllProblemsClicked(self,event):
    """
    Here, if you click on a problem on a listbox, you will get a preview on the screen to see whether it is interesting
    for you or not.
    """
    if self.lstbx_allProblems.size()>0:
      if len(self.lstbx_allProblems.curselection())>0:
        self.txt_preview.delete(1.0, Tkinter.END)
        for s in self.input_SDTables:
          try:
            #problemFileContent = s.loadEntry(self.lstbx_allProblems.get(self.lstbx_allProblems.curselection()[0]))
            fromXMLBuilderModule = __import__("classes.probleminstances.%sFromXMLBuilder"%s.getName(),globals(),locals(),["%sFromXMLBuilder"%s.getName()])
            builderfunc = getattr(fromXMLBuilderModule,"%sFromXMLBuilder"%s.getName())
            creator = builderfunc(s)
            pi = creator.build(self.lstbx_allProblems.get(self.lstbx_allProblems.curselection()[0]))
            problemFileContent = str(pi)
          except:
            continue
        self.txt_preview.insert(Tkinter.END,problemFileContent)


  ##################################################
  #### Input Cheking in the Windows
  ##################################################


  ##################################################
  #### Creation of the different Windows
  ##################################################
  def createWindowProblemSelect(self):
    """
    This is the first window the user is about to see. Here he decides what kind
    of calculations he wants to perform.
    Furthermore, he can decide whether his basering has finite charakteristic or not.
    The next button leads to the selection of concrete problems written down in different
    tables in the SymbolicData database.
    """
    sdEvalPath = os.path.realpath(os.path.dirname(__file__))
    suppComputationProblems = filter(lambda x: os.path.isdir(os.path.join(sdEvalPath,"classes","templates","comp",x)),
                                     os.listdir(os.path.join(sdEvalPath,"classes","templates","comp")))
    self.mainWindow.geometry("%dx%d%+d%+d" % (300, 200, 40, 40))
    #top left corner there is the text labeled by "problem"
    self.lbl_Problem = Tkinter.Label(self.mainFrame, text="Problem:")
    self.lbl_Problem.grid(row=0,columnspan = 2,sticky=Tkinter.W)
    #Now a radio button group with groebner and not Groebner
    self.v = Tkinter.StringVar()
    self.v.set(suppComputationProblems[0])
    self.rb_problemSelect = []
    for i in range(len(suppComputationProblems)):
      self.rb_problemSelect.append(Tkinter.Radiobutton(self.mainFrame,text = dictComputationProblem[suppComputationProblems[i]], variable = self.v, value=suppComputationProblems[i]))
      self.rb_problemSelect[i].grid(row=i+1, columnspan = 2, sticky = Tkinter.W)
    self.rb_problemSelect[0].select() # This is the default selected Button
    #self.entry_characteristic = Tkinter.Entry(self.mainFrame, state = Tkinter.DISABLED)
    #self.entry_characteristic.config(width=6)
    #self.entry_characteristic.grid(row = 6, column = 1, sticky=Tkinter.E)
    #Next Button
    self.btn_next = Tkinter.Button(self.mainFrame,text="Next",command = self.btnNextBehaviour)
    self.btn_next.grid(row = len(suppComputationProblems)+1, column = 1, sticky=Tkinter.E)

  def createTableSelect(self):
    self.mainWindow.geometry("%dx%d%+d%+d" % (575, 625, 40, 40))
    #upper label
    self.lbl_concreteProblems = Tkinter.Label(self.mainFrame, text = "Concrete Problems")
    self.lbl_concreteProblems.grid(row = 0, columnspan = 3)
    #listbox containing all problems
    self.lstbx_allProblems = Tkinter.Listbox(self.mainFrame)
    self.lstbx_allProblems.bind("<Double-Button-1>", self.listBoxAllProblemsClicked)
    self.lstbx_allProblems.grid(row = 1, column = 0, rowspan = 2 ,sticky = Tkinter.W)
    #The button with whome the user can add the problems to the list.
    self.btn_add = Tkinter.Button(self.mainFrame,text = "Add->",command=self.btnAddClick)
    self.btn_add.grid(row = 1, column = 1)
    #The button with whome the user can remove things from the right hand side list.
    self.btn_remove = Tkinter.Button(self.mainFrame,text = "<-Remove",command = self.btnRemoveClick)
    self.btn_remove.grid(row = 2, column = 1)
    #The list with chosen problems
    self.lstbx_chosenProblems = Tkinter.Listbox(self.mainFrame)
    self.lstbx_chosenProblems.grid(row = 1,column = 2, rowspan = 2, sticky = Tkinter.E)
    #The label of the priview window.
    self.lbl_preview = Tkinter.Label(self.mainFrame, text = "Preview:")
    self.lbl_preview.grid(row = 3, columnspan = 3)
    #The preview textbox
    self.txt_preview = Tkinter.Text(self.mainFrame)
    self.txt_preview.grid(row = 4, columnspan = 3)
    #the Next Button
    self.btn_next = Tkinter.Button(self.mainFrame, text = "Next",command = self.btnNextBehaviour)
    self.btn_next.grid(row = 5, column = 2, sticky = Tkinter.E)

  def createCASSelect(self):
    """
    Has the user reached this window, he has already decided which problems he
    wants to deal with. Now he selects the Computer Algebra Systems on which the
    calculations should be perfomed. Additionally, he sets his machine settings
    """
    self.mainWindow.geometry("%dx%d%+d%+d" % (375, 300 + 25*len(self.cpInstance.getPossibleComputerAlgebraSystems()), 40, 40))
    #Top Label
    self.lbl_computerAlgebraSelect = Tkinter.Label(self.mainFrame, text = "Choose the computer algebra systems\n\
on which your calculations should be performed")
    self.lbl_computerAlgebraSelect.grid(row = 0, columnspan = 2)
    #Checkbox select of the computer algebra systems.
    self.var_CASs = {}
    self.cb_CASs  = {}
    for i in range(len(self.cpInstance.getPossibleComputerAlgebraSystems())):
      key = self.cpInstance.getPossibleComputerAlgebraSystems()[i]
      self.var_CASs[key] = Tkinter.StringVar()
      self.var_CASs[key].set("No")
      self.cb_CASs[key] = Tkinter.Checkbutton(self.mainFrame,text = key, variable = self.var_CASs[key],onvalue="Yes", offvalue = "No")
      self.cb_CASs[key].deselect()
      self.cb_CASs[key].grid(row = i+1, columnspan = 2, sticky = Tkinter.W)
    ############
    #Now the Machine Settings.
    self.lbl_MachineSettings = Tkinter.Label(self.mainFrame, text = "Please enter the command line calls for\n\
the local machine to call the following programs:")
    self.lbl_MachineSettings.grid(row = len(self.cpInstance.getPossibleComputerAlgebraSystems())+1, columnspan = 2)
    self.lbl_CASs = {}
    self.entry_CASs = {}
    for i in range(len(self.cpInstance.getPossibleComputerAlgebraSystems())):
        key = self.cpInstance.getPossibleComputerAlgebraSystems()[i]
        self.lbl_CASs[key] = Tkinter.Label(self.mainFrame, text = key)
        self.lbl_CASs[key].grid(row = len(self.cpInstance.getPossibleComputerAlgebraSystems())+2+i, column = 0, sticky = Tkinter.E)
        self.entry_CASs[key] = Tkinter.Entry(self.mainFrame)
        self.entry_CASs[key].config(width = 10)
        self.entry_CASs[key].grid(row = len(self.cpInstance.getPossibleComputerAlgebraSystems())+2+i, column = 1, sticky = Tkinter.W)
    #The Time Command:
    self.lbl_Time = Tkinter.Label(self.mainFrame, text = "Time:")
    self.lbl_Time.grid(row = 2*len(self.cpInstance.getPossibleComputerAlgebraSystems())+2, column = 0, sticky = Tkinter.E)
    self.entry_Time = Tkinter.Entry(self.mainFrame)
    self.entry_Time.config(width = 10)
    self.entry_Time.grid(row = 2*len(self.cpInstance.getPossibleComputerAlgebraSystems())+2,column = 1, sticky = Tkinter.W)
    #Filename to be saved
    self.lbl_name = Tkinter.Label(self.mainFrame, text = "Name of your generated task:")
    self.lbl_name.grid(row = 2*len(self.cpInstance.getPossibleComputerAlgebraSystems())+3, column = 0, sticky = Tkinter.E)
    self.entry_taskName = Tkinter.Entry(self.mainFrame)
    self.entry_taskName.grid(row = 2*len(self.cpInstance.getPossibleComputerAlgebraSystems())+3, column = 1, sticky = Tkinter.W)
    ############
    #Back and Finish Button
    #self.btn_Back = Tkinter.Button(self.mainFrame, text = "Back", command = self.btnBackBehaviour)
    #self.btn_Back.grid(row = 12, column = 0, sticky = Tkinter.W)
    self.btn_CreateExportFolder = Tkinter.Button(self.mainFrame, text = "Create Export Folder", command = self.btnCreateClick)
    self.btn_CreateExportFolder.grid(row = 2*len(self.cpInstance.getPossibleComputerAlgebraSystems())+4, column = 1, sticky = Tkinter.E)

CreateTasksGui()
