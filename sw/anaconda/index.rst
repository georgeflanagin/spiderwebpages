.. _anaconda:
.. highlight:: rst

========================
Anaconda
========================

Description
~~~~~~~~~~~~

Anaconda is a package manager that allows the use of other several pieces of
software widely used by scientists. As well as the server install on the Spydur
cluster, there are desktop versions of Anaconda. These are some of the packages 
that are a part of the Anaconda collection:

:ref:`JupyterNotebooks`

:ref:`SciPy`

:ref:`SciKitLearn`

:ref:`Spyder`

:ref:`NumPy`

:ref:`Dask`

:ref:`Bokeh`

:ref:`TensorFlow`

:ref:`Numba`

:ref:`pandas`

:ref:`pytorch` 

:ref:`matplotlib` 

Contacts
~~~~~~~~~~

Samples, kits, and getting started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Additional documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Quirks, gotchas, and other advisories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use Anaconda, it is necessary to tell your Spydur session
where the Anaconda distro is installed. The following block of 
code is found in the ``/etc/bashrc`` file::

    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/usr/local/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/usr/local/anaconda3/etc/profile.d/conda.sh" ]; then
            . "/usr/local/anaconda3/etc/profile.d/conda.sh"
        else
            export PATH="/usr/local/anaconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<

If you are using some other Anaconda installation, you must include
something similar in your own environment, generally in the ``~/.bashrc``
file.

Module file[s]
------------------

SLURM skeleton
-------------------------

