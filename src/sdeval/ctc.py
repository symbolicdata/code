#!/usr/bin/env python2

"""
This module contains routines for creating tasks which will then be
run on another machine. This file expects a path for the XML-Data of
the symbolic data project as parsing argument. After that the
interactive user mode will be started, where a user can decide which
calculation he wants to perform on which computer algebra system with
which input data. After that, an export folder will be created. For
details read the descriptions of the particular functions.

.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
.. moduleauthor:: Benjamin Schnitzler <Benjamin.Schnitzler@rwth-aachen.de>
"""

#-------------------- Initialization Stuff --------------------

from optparse import OptionParser
from classes.XMLRessources import XMLRessources
from classes.Task import Task
from classes.TaskFolderCreator import TaskFolderCreator
from classes.MachineSettings import MachineSettings
import os
import curses
import string
import sys # TODO: delete this (only for testing used)
import re
from ncurses.sprompt import sprompt
from ncurses.tablecols_v2 import tablecols
from ncurses.choicer import choicer

#PARSING and initializing the interface to the XMLRessources folder

parser = OptionParser("create_tasks.py [options] Arguments")
parser.add_option("-s", "--source", dest="xmldatapath", help="The complete path to XML-Data")
                                                        #We need the loacation
                                                        #of our XML-Data
(opts, args) = parser.parse_args()

stdxmlDataPathDir = os.path.join("..", "..", "data", "XMLResources")

if (len(args) == 0): # We need at least one argument
    if not os.path.isdir(stdxmlDataPathDir):
        print "This program needs at least one argument"
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

# event loop function -----------------------------------
class messenger:
  yoff=0
  xoff=0
  win=None
  def __init__(self, win, yoff, xoff, width):
    self.win=win
    self.yoff = yoff; self.xoff=xoff; self.width = width
  def msg(self, message):
    message = message.ljust(self.width)
    self.win.addstr(self.yoff, self.xoff, message)

# event loop to let the user make choices from a list of choices
# TODO: seperate user choices for different input words for
# better visibility
# TODO: auto completion
def event_loop(choices, stdscr, yoff, xoff):
  winH,winW = stdscr.getmaxyx()
  winH -= yoff; winW -= xoff

  choices.sort()

  stdscr.addstr(yoff,xoff,"Possible selections:")

  cWin = tablecols(stdscr, [choices], "  ", 0, yoff+1)
  cWinHeight = min(cWin.get_numlines_of_table(), int(winH/2))
  cWin.set_height(cWinHeight)
  cWin.display_table()

  ms = messenger(stdscr, yoff + cWinHeight + 2, xoff, winW)
  ms2 = messenger(stdscr, yoff + cWinHeight + 5, xoff, winW)
  ms.msg("Esc Esc to quit, Enter to accept")
  ms2.msg("Your choices:")
  sp = sprompt(stdscr,yoff + cWinHeight + 3,xoff)
  sp.print_prompts()

  yoff += cWinHeight + 6

  cr = choicer(choices, " ", "_-")

  ucWin = tablecols(stdscr, [], "  ", 0, yoff)
  ucWinHeight = winH - 3 - cWinHeight
  ucWin.set_height(ucWinHeight)


  while 1:
    c = stdscr.getch(); # get us the user input

    # break out of event loop, if user presses Esc two times
    if c == 27: # Esc key
      c = stdscr.getch()
      ms.msg("Press Esc again to quit!")
      if c == 27: return None
      else:
        ms.msg("Esc Esc to quit, Enter to accept")
        sp.set_cursor()

    if c == 10:
      if not ucWin.has_words():
        ms.msg("No choices made: Press Esc Esc to quit!")
        sp.set_cursor()
      else: # user pressed Return, accept his choices
        return ucWin.get_merged_words()

    # backspace: delete on char to the left
    if c == curses.KEY_BACKSPACE:
      deleted_char = sp.delch_left()
      if not deleted_char: continue
      if deleted_char != " " and \
         (sp.get_lastch() == " " or not sp.get_lastch()):
        ucWin.pop_n_redraw();
      else:
        uinput = sp.get_last_word()
        ucWin[-1] = cr.get_user_choices_additive(uinput)
        ucWin.redraw()
      ms.msg("Esc Esc to quit, Enter to accept")
      sp.set_cursor()
      continue

    # user entered some printable character
    if 32 <= c and c <= 126:
      last_char = sp.get_lastch()
      sp.appendch(c)
      if c == ord(" "): continue
      uinput = sp.get_last_word()
      if last_char == " " or not last_char: # new word
        ucWin.append( cr.get_user_choices_additive(uinput) )
      else: # not a new word, update choices
        ucWin[-1] = cr.get_user_choices_additive(uinput)
      ucWin.redraw()
      ms.msg("Esc Esc to quit, Enter to accept")
      sp.set_cursor()
      continue

    #if c == curses.KEY_DOWN:
    #  cWin.scroll_down(); cWin.display_table();
    #  sp.set_cursor(); continue

    #if c == curses.KEY_UP:
    #  cWin.scroll_up(); cWin.display_table();
    #  sp.set_cursor(); continue

    # TODO: terminal resize event, redraw everything...
    if c == curses.KEY_RESIZE:
      cWin.refresh(); cWin.redraw(); continue

    #ms.msg("pressed '" + str(c) + "' ") # debug output of key

  return uchoices

# -------------------- Interactive user mode --------------------

# Get the computation problem we want to solve first
print "What computation problem do you want to solve?"
print "Possible inputs:"
for i in range(len(suppComputationProblems)):
  print str(i) + " " + suppComputationProblems[i]
print str(len(suppComputationProblems)) + \
      " What problem? I don't have a problem. Get out of my way!"
operation = raw_input("Choose your operation(0-2): ")
try: int(operation)
except: operation = -1
while int(operation) < 0 or \
      int(operation) > len(suppComputationProblems):
  print "\nHow dare you! This operation is not supported!"
  print "You must type a number between 0 and 3!\n"
  operation = raw_input("Choose another operation: ")
  try: int(operation)
  except: operation = -1

if int(operation) == len(suppComputationProblems): sys.exit(0)

operation = suppComputationProblems[int(operation)]

# This is from Al, I did't change it, lets hope, it is correct
compProbInstanceModule = __import__("classes.computationproblems.%s"%operation,globals(),locals(),[operation])
compProbInstanceClass = getattr(compProbInstanceModule,operation)
cpInstance = compProbInstanceClass()
piSDTables = map(lambda x: xmlres.loadSDTable(x),cpInstance.getAssociatedTables())
chosenProblemInstances = []
completeProblemList = []
for x in piSDTables:
    completeProblemList += x.listEntries()
flag = True

# Now we use curses for a better handling of user input
stdscr = curses.initscr()
curses.noecho(); curses.cbreak(); stdscr.keypad(1)

scrh,scrw = stdscr.getmaxyx()

# first get the concrete problem to solve
title = "Now: Choose concrete problems to solve!"
stdscr.addstr(1,0,string.center(title, scrw))
chosenProblemInstances = \
    event_loop(completeProblemList,stdscr, 3, 0)

stdscr.clear()

# now get the CAS
CASs = None
if chosenProblemInstances:
  casList = cpInstance.getPossibleComputerAlgebraSystems()
  title = "Now: Choose the CAS you want to use!"
  stdscr.addstr(1,0,string.center(title, scrw))
  CASs = event_loop(casList,stdscr, 3, 0)

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()

if not CASs: sys.exit(0) # user has aborted

print

# following code is from Al, again no changes
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
