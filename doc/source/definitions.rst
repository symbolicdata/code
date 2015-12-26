Definitions of terms used in the SDEval Project
===============================================

Author: Albert Heinle <albert.heinle@googlemail.com>

.. _Task:

**Task**
  A task is always associated to a certain `computation problem`_. A
  task contains a list of `SD-Tables`_, that contain entries that are
  suitable as input for the associated computation problem.

  From those SD-Tables, a task contains a set of problem instances (see
  Definition \ref{def:ProblemInstance}). Additionally, a task contains a
  set of computer algebra systems (see Definition
  \ref{def:computeralgebrasystem}), that provide algorithms for solving the
  associated computation problem. Every set in a task is not
  empty. Furthermore, a task has a name.

  *Example:* Let us call a task ``xyz``, and let its associated
  computation problem be ``GB_Z_lp``.

  This is an entry in the Symbolic-Data table ``COMP`` and
  represents the commutative Gröbner basis computation in a
  commutative ring using the lexicographical ordering and given
  generators that have coefficients in :math:`\mathbb{Z}`.

  The only existing SD-Table_, that provides an entries that can be
  used as inputs for the Gröbner basis algorithms, is meanwhile
  ``IntPS`` (see Symbolic-Data). From this table, we choose as one of
  our problem instances the instance ``Amrhein``. A computer algebra
  system, that provides an algorithm for ``GB_Z_lp`` is for example
  Singular_.

.. _`Computation Problem`:
.. _`Computation Problems`:

**Computation Problem**
  A computation problem is a problem, which is specified in the
  SD-Table_ ``COMP`` of the Symbolic Data project. In the context of
  SDEval we are using it to specify which computations we want to
  perform on certain `problem instances`_, resp. which algorithm shall
  be used.

  *Example:* A computation problem is for example ``GB_Z_lp``.

  This is an entry in the SD-Table_ table ``COMP`` and represents
  the commutative Gröbner basis computation in a commutative ring
  using the lexicographical ordering and given generators that have
  coefficients in :math:`\mathbb{Z}`.

.. _`Problem Instance`:
.. _`Problem Instances`:

**Problem Instance**

  A problem instance is in our context a representation---specified by
  Symbolic-Data---of a concrete input for suitable algorithms.
  Suitable means that the entries for the chosen algorithms can be
  read from this problem instance. A problem instance is always
  contained in a SD-Table_.

  *Example:* A problem instance is for example the entry ``Amrhein``
  in the SD-Table_ ``IntPS``. It contains variables and a basis of
  polynomials, and those can be used for Gröbner basis computations,
  for example.

.. _SD-Table:
.. _SD-Tables:

**SD-Table**
  A SD-Table denotes the folder structure of a chosen subfolder in the
  ``XMLRessources`` folder in the Symbolic-Data project.


  *Example:* There are several folders in ``XMLRessources``. Some
  examples:

   * ``IntPS``
   * ``COMP``
   * ``{ModPS``
   * ``CAS``

.. _`computer algebra system`:
.. _`computer algebra systems`:

**Computer Algebra System**
  A computer algebra system is a program, described by an entry in the
  SD-Table_ ``CAS``. It provides algorithms to solve different
  `computation problems`_.

  *Example:* Singular_ is a computer algebra system.

.. _Taskfolder:

**Taskfolder**
  A taskfolder is always associated to exactly one task_. It contains:

    * the task_ itself
    * For every `problem instance`_ and for every `computer algebra
      system`_ the taskfolder contains one executable file, that
      contains the calculation steps for the calculation of the
      `computation problem`_.
    * An executable file ``runTasks.py`` and all needed modules_ of
      this file.
    * The `machine settings`_ for the `target machine`_ of the task.

  It serves the purpose to be exported as a single folder to a `target
  machine`_, where the calculations shall be run at.

  *Example:* In order to have an example of a taskfolder,
  just run ``create_tasks[_gui].py``, and the folder that is
  created in the end, that is a taskfolder.

.. _module:
.. _modules:

**Module**
  A module is a collection of executable code of a certain
  programming/script-language.

  *Example:* In the SDEval project, there is, for example, a module
  called ``classes.probleminstances``.

  It contains representations as classes of different types of
  `problem instances`_.

.. _`machine setting`:
.. _`machine settings`:

**Machine Settings**
  Machine settings is a collection of machine-specific constants of the
  `target machine`_. Those are:

  * For every computer algebra system the command to execute it on the
    target machine.
    * The command for the time measurement (`time command`_) on the
    `target machine`_ with the desired options of the user.
  * Optional, it can contain further entries.

  *Example:* The command for time measurement is on every UNIX-like
  machine simply ``time``. The command to run e.g. version 15 of
  Maple_ on a machine known to the author is ``maple15``.

.. _`target machine`:
.. _`target machines`:

**Target Machine**
  A target machine is the computer on which in the end the
  computations for a specific task_ will take place. In our choices of
  words we assume in general, that it has a UNIX-like operating system
  installed. There must be a `time command`_ available on that
  machine.

.. _`time command`:

**Time Command**
  A time command is a tool for time measurement. On UNIX-like
  operating systems it is e.g. the command ``time``.

  In the context of SDEval we need that this time command is able to
  produce its output in the IEEE Std 1003.2-1992 (POSIX.2) described
  way. On UNIX-machines, it is achieved by adding the option ``-p`` to
  the command.

  *Example:* For example, on a mac, this is how the time command
  works::

    $ time -p echo "Hello"
    Hello
    real 0.00
    user 0.00
    sys 0.00

**Proceedings**
  Proceedings contain information about the status of the execution of
  the files in the taskfolder_. For the status, there are the
  following options:

    * ``RUNNING``   -- The file is running
    * ``WAITING``   -- The file is waiting for its execution
    * ``COMPLETED`` -- The execution of the file is finished
    * ``ERROR``     -- An Error occured

  During the execution, there will always be an XML and an HTML file
  written visualizing the current proceedings.

  *Example:* Let us take the entry ``Amrhein`` of the ``IntPS`` table
  and let the `computer algebra systems`_ Singular_ and Maple_ be
  chosen for the computation of a Gröbner basis of those systems.

  In the beginning, both execution files (i.e. for Singular_ and
  Maple_ are ``WAITING``. If one of the files is executed on its
  `computer algebra system`_, it has the status ``RUNNING``, and when
  the computation is completed, the status will change to
  ``COMPLETED``.

**Resulting File**
  During the execution of the files in a taskfolder_, there are
  always resulting files containing the output of the `computer
  algebra system`_ and the `time command`_.

  *Example:* A resulting file after executing some singular commands
  has for example the following form::

                         SINGULAR                                 /
     A Computer Algebra System for Polynomial Computations       /   version 3-1-5
                                                               0<
     by: W. Decker, G.-M. Greuel, G. Pfister, H. Schoenemann     \   Jul 2012
    FB Mathematik der Universitaet, D-67653 Kaiserslautern        \
    a2+a+2bf+2ce+d2,
    2ab+b+2cf+2de,
    2ac+b2+c+2df+e2,
    2ad+2bc+d+2ef,
    2ae+2bd+c2+e+f2,
    2af+2be+2cd+f

    $Bye.
    real 0.53
    user 0.01
    sys 0.01

.. _Singular: http://www.singular.uni-kl.de/
.. _Maple: http://www.maplesoft.com/
