.. _shortcuts:
.. highlight:: rst

=====================================
Shortcuts for common SLURM operations
=====================================

SLURM has several modules, each of which provides an operation with
as many as 100 options. Fortunately, unless you are an administrator,
you only need to use a few of them. The shortcuts will make it a little
easier if you are new to this world.

myjobs
------

Just type ``myjobs``, and you will get a short, not very detailed list
of everything you are currently running.

nodes
-----

Working in this environment, you will need to find out about the states
of the many nodes -- their names, and what they are doing at the moment. 
This is your command. If you type ``nodes`` all by itself, the command 
will explain the options to you::

    The nodes command allows you to get information about the
    nodes in the cluster. The syntax is:

        nodes {what-you-want-to-know-about}

    The options are:

        free    -- show the idle nodes available for assignment.
        avail   -- same as free
        info    -- a more nicely formatted output from <sinfo>
        queues  -- a more nicely formatted output from <squeue>


submit
------

This command allows you to submit a job to SLURM using the defaults
for things like memory size, cores, and so on. For a lot of experiments
and tests, the defaults will do an acceptable job. As with ``nodes``,
if you just type ``submit`` you will be told a bit more about the 
options::

    The submit command allows you to submit slurm jobs in
    batch mode (the usual way of doing things). You can provide
    the name of your job with or without the ".slurm" on the end
    of the file name. You can also submit multiple jobs at the
    same time. Here are some examples:

        submit myjob.slurm -- tells slurm to run myjob.slurm
        submit myjob  -- tells slurm to run myjob.slurm
        submit myjob* -- tells slurm to run any slurm jobs whose
            names start with "myjob"

    Assuming something has been submitted, you will see your running
    jobs summarized at the end of the command.
