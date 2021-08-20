.. _first:
.. highlight:: rst

====================================
Your first SLURM job
====================================

*NOTE: If you run aground with the outlined instructions below, send
an email to* ``hpc+slurm@richmond.edu``

Using slurmwriter
-------------------

Perhaps you are new to SLURM, and you would like a little interactive
help? ``slurmwriter`` is a simple dialog-based program to help you be
successful. After you create one SLURM job, you can use it as a pattern
for ones ahead. 

The ``slurmwriter`` is aware of the set up of the cluster where you are
logged in. It knows the names of the installed programs, the names of 
the partitions on the cluster, and it queries Linux to find out what
accounting groups you are a part of. Even these features will prevent
a lot of misspelled words that would cause your job to fail.

At the end of this section, there is an example execution of ``slurmwriter``.
Let's take a look at its collection of questions.

Name of your job
~~~~~~~~~~~~~~~~~~

You can name your job anything you like. It is a good idea to keep it
relatively short, and it is an even better idea to have the first few
letters give you an idea of what the job is about. 

Name of your job's output file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The suggested value will with the name of our job with ``.txt`` appended.
This is the file where the history of your job's execution will be 
recorded, not the name of a data output. This is sometimes called your
job's "tombstone" file, and it may not contain much information at all.
SLURM, however, needs to know where to write these data.

Name of the program you want to run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``slurmwriter`` knows the names of the major packages on the machine, and you
can either choose one or leave this response blank. If you give the name
of program, ``slurmwriter`` will find the appropriate module files and 
add the directives that they be loaded for you to the job file it creates
for you. If you leave it blank, you can add these later with a text editor.

Name of the partition where you want to run your job
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some other scheduling programs, these locations are called *queues*.
For SLURM systems, the word is *partition*. ``slurmwriter`` will 
suggest the name of the default partition, but you can choose any 
partition to which you have access. If you misspell the partition name,
``slurmwriter`` will show you the list of available partitions to help
you get it right the next time.

The name of the account for the job
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SLURM keeps things fair. As such, your netid is associated with one
or more accounts that are used to group time, and these accounts
ensure everyone gets a fair share. The default value will likely
be the correct one. As with partitions, ``slurmwriter`` will 
ensure you spell the account names correctly.

You input data directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The files containing the data you intend to process should be found
in this directory.

Your scratch directory
~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming your job has recovery points, partial results, or any data
files created along the way, this is generally where they will be found. 

**Note:** this directory is never backed up. 

Job parameters: memory, cores, run time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are a student, these values are often supplied by the instructor
who is guiding your work. In all cases, ``slurmwriter`` will not let you
request more cores or memory than are available in the partition you
have chosen, nor will it let you exceed the maximum execution time
configured for the partition.

When to start your job
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sure -- everyone wants to run now. 

The name of the job file
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, this file (the one you submit to SLURM for execution)
will have the name of your job with the suffix ``.slurm`` appended.


Sample session
~~~~~~~~~~~~~~~~~~

The following is a sample transaction ::

    slurmwriter. Version of 2021-08-04T14:42
          rules. Version of 2021-08-04T14:42

    Slurmwriter is a simple program to help new SLURM users format
    their first jobs properly. A SLURM job can be a little tedious
    to construct, and by answering a few questions, this utility
    can help you get the basics correct the first time.

    Name of your job : myverybigjob
    Name of your job's output file [/home/gflanagi/myverybigjob.txt] :
    What program do you want to run [] : dot
    Name of the partition where you want to run your job [gpu*] :
    What account is your user id, gflanagi, associated with [users] :
    Where is your input data directory [/home/gflanagi] :
    Where is your scratch directory [/home/gflanagi/scratch] :
    How much memory (in GB) [16] :
    How many cores [8] :
    How long should this run (in hours) [1] :
    When do you want the job to run [now] :
    What will be the name of this new jobfile [/home/gflanagi/myverybigjob.slurm] :

    ----------------------

    Name of your job => myverybigjob
    Name of your job's output file => /home/gflanagi/myverybigjob.txt
    What program do you want to run => dot
    Name of the partition where you want to run your job => gpu*
    What account is your user id, gflanagi, associated with => users
    Where is your input data directory => /home/gflanagi
    Where is your scratch directory => /home/gflanagi/scratch
    How much memory (in GB) => 16
    How many cores => 8
    How long should this run (in hours) => 01:00:00
    When do you want the job to run => 2021-08-11T14:02
    What will be the name of this new jobfile => /home/gflanagi/myverybigjob.slurm

    These are the answers you provided. Are they OK? [y] : y
    Writing file /home/gflanagi/myverybigjob.slurm...

Writing a job script on your own
---------------------------------

You know what program you want to run, right? You are half-way there.
We have a tool named ``slurmwriter`` that is a good way to start
if you are completely new to SLURM, Linux, and the command line
world. ``slurmwriter`` is discussed in the next section.

SLURM variables all start with ``#SBATCH`` at the beginning of the
line, one of these commands per line.

The following is a list of variables that you should set, with 
an explanation of their meaning. They can be placed in any order, but
they all must be in the script before the execution statements that
will run your programs.

``#SBATCH --account=`` This variable should be given the value of your faculty
sponsor's ``netid``. The value will influence where in the 

``#SBATCH --begin=`` You can leave this out, and your job will start
as soon as SLURM can schedule you. You can also use "tommorow" and
"midnight" if you like.

``#SBATCH --mail-user=`` The only reasonable answer is your UR email
address.

``#SBATCH --mail-type=`` Most of the time, the value ``ALL`` is the right
one to use.

``#SBATCH --mem=`` Your answer will probably be something like ``10GB``. It
might not be 10, but the gigabyte written as ``GB`` is the usual unit of
measure.

``#SBATCH --ntasks=1`` To SLURM, the execution of a program is a *task*. No
matter how many cores or how much memory, most of the time you will
be setting ``ntasks`` to one. 

``#SBATCH --cpus-per-task=`` To SLURM, a CPU is a "core," in the more modern
vocabulary. 

``#SBATCH --partition=`` To SLURM, a partition is a collection of
one or more nodes with similar properties. If you do not specify
this term, SLURM will assign your job to the most available partition.

``#SBATCH --time=`` In this case, time is the answer to the question
"how long should this job run before we give up?"

