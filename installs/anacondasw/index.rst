.. _anacondasw:
.. highlight:: rst

====================================
Anaconda
====================================


Maintenance
~~~~~~~~~~~~~~~~~~~~

Installation
----------------

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

Upgrade
-----------

Remove or disable
---------------------

