How to create this website
==========================

Prerequisites
-------------

This website has been created using 
`Sphinx <http://sphinx.pocoo.org>`_.

It is assumed that a version of Python is already installed locally.
If not, run ::

  sudo apt-get install python

To install Sphinx is as easy as running ::

  sudo easy_install -U Sphinx

in some directory. It would install Sphinx system-wide.

Assuming that you have python installed but no root access to your
computer, you can also install it in your HOME directory without
messing up any other directory. For this we use python's virtual
environment and install everything under ``$HOME/pythonstuff``. Use
bash as shell. Do the following. ::

  D=$HOME/pythonstuff
  mkdir -p $D
  cd $D
  git clone git://github.com/pypa/virtualenv.git
  cd virtualenv
  git checkout master
  python virtualenv.py $D
  export PATH=$D/bin:$PATH
  easy_install -U Sphinx

For future use you should put the line ::

  export PATH=$HOME/pythonstuff/bin:$PATH

into your ``.bashrc`` file.

Upgrading the Sphinx installation is then as easy as ::

  easy_install -U Sphinx

Compilation
-----------

Compilation is simply done by ::

  cd doc/sources
  make html

Now point your browser to a local URL (``file://``) at ``build/html``.
With firefox you could say::

  firefox build/html/index.html
