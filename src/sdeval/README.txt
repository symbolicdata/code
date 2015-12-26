==================================================
                                                  SDEval v2
==================================================

LICENSE
This program is free software; see LICENSE.TXT for more details

REASON
This program provides algorithms to extract information saved in
Symbolic-Data tables (see the Symbolic-Data project,
http://www.symbolicdata.org) and create executable code for different
computation problems for a number of computer algebra systems.

MANUALS
See folder doc for manuals.
For some basic definitions on the terminology we are using here, see
the definitions.rst in that folder.
There is also a video tutorial available, describing the goals and the
general use of SDEval. You can find it here: https://www.youtube.com/watch?v=CctmrfisZso


REQUIREMENTS
- Python must be installed, at least version 2.6.1
- If it does not come with the Python-installation, python-tk is also
   required
- For the script "runTasks.py", you need a Unix-like OS (i.e. Linux,
   Mac OS, ...)
- there must be a local copy of the Symbolic-Data-tables on the computer

INSTALLATION
Just execute

USAGE AND EXAMPLE
just run
>python ctc.py
in the sdEvalFolder for terminal Task creating, or
>python create_tasks_gui.py
for a task creation using a graphical user interface

Then, in the export task folder, execute
>python runtasks.py

CONTACT
For any questions you can contact Albert Heinle <albert.heinle@rwth-aachen.de>.

ACKNOWLEDGEMENTS
Special thanks to DFG (Deutsche Forschungs Gesellschaft) who funded
the project (Schwerpunkt 1489)

PAPERS
Heinle, Albert, Viktor Levandovskyy, and Andreas Nareike. "Symbolicdata: sdeval-benchmarking for everyone." arXiv preprint arXiv:1310.5551 (2013).
