Notes for Authors
=================

Getting and working with the sources
------------------------------------

Get an account at Github
........................

This step is not absolutely necessary if you have other means to
make your private development visible to the public.

#. `Register <https://github.com/signup/free>`_ a new github account.
   Let's assume your account name is ``foofoo``.
#. Sign in to your github ``foofoo`` account.
#. Go to the `official SymbolicData repository
   <https://github.com/symbolicdata/symbolicdata>`_ and click on
   `Fork`. You will now have your own clone of the |PACKAGE_NAME|
   repository.

How to get the sources
......................

Every developer should have a public and a private repository. (See
section about integration manager workflow below.)

You should clone from **your public** repository. ::

     git clone git@github.com:foofoo/symbolicdata.git

How get future updates from the official repository
...................................................

You have to connect your repository with the official one. Add a new
remote with name `upstream`. Do this inside your cloned repository. ::

  git remote add upstream git://github.com/symbolicdata/symbolicdata.git

Now, by using ::

  git fetch upstream

you get all the commits from the official repository.

Note that after `fetch` you only have the commits locally on your
computer. Whether and how you merge them, you can decide after looking
at the current situation. Usually ::

  gitk --all

gives you a nice graphical picture of the DAG (directed acyclic graph)
of the commits.

Workflow: how to work with the repositories
...........................................

The following assumes that the |PACKAGE_NAME| project is working with
the `Integration Manager Workflow
<http://git-scm.com/book/en/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow>`_.

There is a **blessed** `repository
<https://github.com/symbolicdata/symbolicdata>`_ and each developer
has a public repository (for example, at github as described above)
and a private repository on his laptop/desktop computer.

Code would flow via PR (pull requests) to the blessed repository.
Github has a button for pull requests.

Advantage of this workflow is that the integration manager can act as
a person to ensure the quality of the patches. And there is no need to
manage ssh keys in order to give someone write access to the
repository.

If this sounds too complicated for a small project, we can also switch
to a centralized workflow. That should be discussed on the `mailing
list
<https://groups.google.com/forum/?fromgroups#!forum/symbolicdata>`_.

Make yourself known to git
..........................

If in the output of ``git config --list`` you don't find something
like ::

  user.name=FirstName LastName
  user.email=YourFirstName.YourLastName@risc.jku.at

, then you should introduce yourself to git. This will create/modify a
file ``~/.gitconfig``. ::

  git config --global user.name "YourFirstName YourLastName"
  git config --global user.email "YourFirstName.YourLastName@risc.jku.at"

You should use your default email address. This email address is only
used by git to identify you, but not to send any mail to you.

Structure of the repository and how to deal with it
...................................................

The |PACKAGE_NAME| project decided to follow `"A successful Git
branching model"
<http://nvie.com/posts/a-successful-git-branching-model/>`_.

The **blessed** `repository
<https://github.com/symbolicdata/symbolicdata>`_ consists of 3
branches.

`master <https://github.com/symbolicdata/symbolicdata>`_ This branch
  is for all the data that should go into version 3 of |PACKAGE_NAME|
  and marks the latest stable release.

`develop <https://github.com/symbolicdata/symbolicdata/tree/develop>`_
  This branch is for actual development. Main requirement for a commit
  on this branch is that programs must compile and data must be in a
  consistent state (no syntactic errors).

`old-master <https://github.com/symbolicdata/symbolicdata/tree/old-master>`_
  This branch is basically a snapshot from the latest Mercurial
  repository (12-Dec-2012). It contains the full history of former
  |PACKAGE_NAME| commits.

  This branch will eventually be removed.

In fact, there are two disconnected DAGs for ``master``, and
``old-master``. (Something that cannot be done with Mercurial.)

How to work with GIT
--------------------

It is usually enough to work with the following `git`_ commands:

`git pull <http://www.kernel.org/pub/software/scm/git/docs/git-pull.html>`_
  Get the latest changes from the official repository.

`git add <http://kernel.org/pub/software/scm/git/docs/git-add.html>`_ FILE1.mt FILE2.m
  Mark ``FILE1.mt`` and ``FILE2.m`` to be committed in the next commit.

`git commit <http://kernel.org/pub/software/scm/git/docs/git-commit.html>`_
  Commit all marked modifications to the local repository.

  **Note** that only files that have been added via ``git add`` will
  be committed.

  **Note** that after ``git commit`` the modifications have not yet
  left your computer. They are simply stored in your local repository.

  Set the variable ``GIT_EDITOR`` in your ``$HOME/.bashrc`` if you
  don't like ``vi`` so much. ::

    export GIT_EDITOR="emacs -nw"

`git push <http://kernel.org/pub/software/scm/git/docs/git-push.html>`_
  Upload your modifications to the official repository.

`git status <http://kernel.org/pub/software/scm/git/docs/git-status.html>`_
  Investigate which files have changed on your file system.

`git log <http://kernel.org/pub/software/scm/git/docs/git-log.html>`_
  Investigate the history of changes.

.. seealso::

  * `The ProGit Book <http://progit.org/>`_
  * `25 tips for intermediate git users <http://andyjeffries.co.uk/articles/25-tips-for-intermediate-git-users>`_
  * `Use gitk to understand git <http://www.lostechies.com/blogs/joshuaflanagan/archive/2010/09/03/use-gitk-to-understand-git.aspx>`_
  * `Git Cheat Sheet <http://zrusin.blogspot.co.at/2007/09/git-cheat-sheet.html>`_
  * `Git Wiki <https://git.wiki.kernel.org/index.php/Main_Page>`_
  * `Git - SVN Crash Course <http://git.or.cz/course/svn.html>`_
