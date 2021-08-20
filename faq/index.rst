.. _faq:
.. highlight:: rst

======================================================
Frequently Given Answers to Frequently Asked Questions
======================================================

How to get help.
----------------

Generally, email works best. Spydur has a special email address,
``hpc@richmond.edu`` that is always routed to someone who is *not* on
vacation, although on University holidays repsonses may be less
than timely. We have created some sub-addresses for common issues.

``hpc+account@richmond.edu`` -- if you need an account, or if you 
are a faculty member who has a student who needs an account created.
*Note: students must be associated with a faculty member to be granted
an account!*

``hpc+down@richmond.edu`` -- if a node in the cluster is down.

``hpc+install@richmond.edu`` -- if you need software installed.

``hpc+permission@richmond.edu`` -- if you seek permission to execute
a program or read a file.

General Questions
-----------------

Is it case sensitive?
~~~~~~~~~~~~~~~~~~~~~

*Everything* in Linux is case sensitive. OK, perhaps not everything,
but you will be safe if you assume everything is case sensitive.

What is an environment variable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every process in Linux has an *environment*. The environment is
created for you when you login, and for your SLURM jobs when
they are submitted. It allows you to set symbolic names ('variables')
and give them values. These values, unlike shell variables are 
known to programs that you run, and they persist for the duration
of your session.

Traditionally, most environment variables have names in UPPERCASE,
although that is just a custom, and in no way a requirement. 

How do I create a new environment variable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, determine if it already exists. When we want to use the
value of an environment variable, we prefix it with a dollar sign. To 
find out if the variable is exists ("is set"), the following is 
all that is required::

    [~]: echo $ABCD


    [~]: echo $HOME
    /home/gflanagi

If the environment variable exists, its value will be printed. Otherwise,
nothing is printed to the screen. Let's create ``ABCD``::

    export ABCD="First four letters of the alphabet"

Some key points: [1] The word ``export`` is what makes ``ABCD``
into an environment variable. [2] There must be no space around the
``=`` for the statment to work.  [3] Nothing will be printed to the
screen, and there is no confirmation. However, it is immediately
available, and you can demonstrate its existence by::

    [~]: echo $ABCD
    First four letters of the alphabet

What is a shell?
~~~~~~~~~~~~~~~~

When you login, you must be running some program. A shell does
little except allow you to select between other, more useful programs
to run. Think of the computer as a restaurant, the shell as a menu,
and the other programs as the food.

What is a shell variable?
~~~~~~~~~~~~~~~~~~~~~~~~~

A shell variable looks much like an environment variable, and the same
rules apply. However, it is created without the word ``export`` before
the variable name. Shell variables are generally less useful than 
environment variables because they cannot be seen by any process other
than the current execution of the current shell.

What shell am I running?
~~~~~~~~~~~~~~~~~~~~~~~~

You will go far in Linux if you keep in mind a fundamental fact:
Everything is represented somewhere as a file, or at least there
is a file name associated with it. Naturally, the name of your
current shell is in a file, but which one? Try this::

    [~]$ ls -l /proc/$$/exe
     lrwxrwxrwx. 1 gflanagi users 0 Jul 28 09:23 /proc/3339/exe -> /usr/bin/tcsh*

The /proc directory contains all the information about the currently
executing processes on the computer. The special symbol, $$, is the
PID (Process ID of the currently executing process — your shell,
in this case. The exe member is the name of the process, and there
you see /usr/bin/tcsh.

How do I run bash?
~~~~~~~~~~~~~~~~~~~

You need do nothing other than type the word bash, and press the return key::

     [~]$ bash
     Loading global bash settings.
     [~]: ls -l /proc/$$/exe
     lrwxrwxrwx. 1 gflanagi users 0 Jul 28 09:32 /proc/4012/exe -> /usr/bin/bash

Can I permanently change my shell (to bash)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course; in fact, you can change almost all defaults in your Linux
environment. There is a program named chsh (i.e., change shell)
that is available to every user::

    [~]: chsh
     Changing shell for gflanagi.
     New shell [/bin/csh]: /usr/bin/bash
     Password:
     Shell changed.


Note that you are shown the name (in this case an alias) of the
current shell. To be sure you do not do this because you accidentally
typed chsh instead of one of the other 31 built in commands that
start with ch, you are asked for your password.

And yes, if this does not work out for you, the same process can
be used to reverse your choice.

Software Installations
----------------------

How do I get a package installed on Spydur?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Send a message to ``hpc+install@richmond.edu`` and if we can, we will
take care of it for you.

How do I find out if a Python package is installed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is particularly easy to do. Start Python, and type::

    >>> import somestuff
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     ModuleNotFoundError: No module named ’somestuff’

Looks like ``somestuff`` is not installed.

How do I get a list of all installed Python packages?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you think you might not have its name correct, and many packages
do have oddly spelled names, you can use the following oddly named
command::

    pip freeze | sort | less

You will be shown an alphabetized list of everything Python knows
about that is installed on the computer, one page (screen) at a
time. Press the spacebar to see the next page.


How do I install a Python package in my HOME directory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you begin installing your own packages, it is useful to
understand how Python locates the packages you import. There is an
environment variable named PYTHONPATH that Python uses to search
directories. However, there are three implicit locations that do
not appear in the list, and they are searched in this order:

#. “Here,” as in the value of $PWD, your current (Present) Working
    Directory. The implication is that if you are writing a Python
    program, and you put all your files in one directory, they will be
    found, and they will also hide the visibility of imports with the
    same names.
#. $HOME/.local, which is the directory this section of this document
    discusses.
#. The site-packages directory contained in the directory where the
    Python program, itself, is located. Packages installed here are a
    part of the installation seen by all users on the computer.

The Python Package Index (PyPI) contains packages that can be
installed using pip. pip is a standard part of all Python distributions,
whether you are using the Anaconda distro, or the base version from
the Python Software Foundation (python.org). Generally, this goes
without a problem. Just type ``pip install somestuff --user``, and you
will see something like the example::

    [~]: pip install somestuff --user
     Collecting somestuff
       Downloading somestuff-3.9-py2.py3-none-any.whl (11 kB)
     Installing collected packages: somestuff
     Successfully installed somestuff-3.9

Here is what happened:

#. pip retrieved the latest version by default, in this case version
    3.9. [ Note: Packages have their own versions — this does not imply
    that Python 3.9 is in any way required, or even present on the
    computer where this installation took place. — end note. ]
#. If somestuff had required other packages (“dependencies”), pip
    would have installed them, also.
#. The bit about py2.py3-none-any means that somestuff is compatible
    with “any and all” versions of both Python2 and Python3.
#. The package is very small in this case, with the zip containing
    somestuff only being 11kB in size.

And here it is, buried below your home directory::

     [~]: ls -l
     total 24
    -rw-r--r--. 1 gflanagi users 24294 Jul  2 11:04 __init__.py
     drwxr-xr-x. 2 gflanagi users    37 Jul  2 11:04 __pycache__
     drwxr-xr-x. 4 gflanagi users    87 Jul  2 11:04 tests

``init.py`` -- This is the code. Python requires that all packages
have an __init__.py file, in fact, the presence of that file is
what makes them a package that you can import rather than a module.

``pycache`` This directory contains the compiled version of the
source code in __init__.py.

``tests`` These are tests that the package’s author may have used
to verify that the package operates correctly.

How do I remove a locally installed pacakge?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As mentioned elsewhere, the goal is to have software installed
locally for evaluation and testing rather than long-term use. OK,
but what is the danger in keeping the locally installed copy around
“just in case?”

Remember the order in which Python searches for packages — it looks
in $HOME/.local before it looks in the central repository. If we
install the same package in the site-packages directory of /usr/local,
and we later update that package, you will not benefit from this
advance because when you run Python your local copy will be loaded,
first.1

If your package was installed with pip all you need to do is type
the following::

    pip uninstall somestuff

Note that pip will uninstall the first version it finds, in this
case, the one we installed locally.

How do I install from github into my current directory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get the package from github.com or gitlab.com, the author
will provide both a ``setup.py`` file that you run (i.e., python setup.py)
after you download the software, and a ``README`` file that will explain
anything else you need to do.  

Your mileage may vary; the ability and willingness of code authors
to write installation instructions spans a wide spectrum.

PATH problems
---------------

I get an error message when I try to run asdf ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It probably looks like this::

    [~]: asdf
    bash: asdf: command not found...

The problem is likely related to your PATH, a global environment
variable. First, find out what is in your PATH::

    echo $PATH
     /usr/local/ur/tools:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin



PYTHONPATH problems
---------------------

I cannot import X, and I know it's there
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Much like the PATH, Python has an environment variable named
PYTHONPATH. By default, it is empty. More correctly, it contains
only the implied locations, and there are three locations that
you need never be concerned about --- the current working directory,
the ``$HOME/.local`` hidden directory that contains packages
you have installed with the ``--user`` option, and the packages
that are part of the system-wide Python installation.

Suppose your friend Bart Simpson gave you a file named ``skateboard.py``
that you want to use in one of your projects. In fact, you may want
to use it in all of your projects, so putting it in a directory
with some of your other working code does not make much sense.

So you make a directory for Bart’s code and put it the file 
in the new directory::

     cd $HOME
     mkdir -p python.code/bsimpson
     mv skateboard.py python.code/bsimpson

To be able to ``import skateboard``, Python needs to be able to find 
the file. Modify your PYTHONPATH in the following way::

    export PYTHONPATH="$HOME/python.code/bsimpson:$PYTHONPATH"

It is true that PYTHONPATH may be empty (containing only the implicit
locations), but it is good practice to not rely on this fact, and
to include the old value in the new definition.


Execution of Programs
---------------------

How do I get a program to run after I logout?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wrap your command in ``nohup``, like this::

    nohup /my/command -and -its arguments >myout 2>myerr </dev/null &

Let's talk about what happens. ``nohup`` is a program that 
runs your program, essentially another layer inserted between
the shell and the program you want to run. ``nohup`` allows it to
continue after you logout. 

``/my/command``, whatever the program is, will be run, along with
all the arguments and options, however you would normally type in
the command. 

The output of the ``/my/command`` must go somewhere, and the ``>myout`` 
term will send the output to a file. Similarly, ``>myerr`` will contain
the errors, or any messages that the program happens to treat 
as errors.

Finally ``</dev/null`` prevents the program hanging, just in case
there is a part of it that might try to read from the terminal 
window -- a source that is no longer there after you logout.

The ampersand at the end of the line causes ``nohup`` and your
program to disconnect from the keyboard, and that allows you to
do other things. 


