.. _rebuild:
.. highlight:: rst

==========================================
Rebuilding or updating a Linux Workstation
==========================================

A couple of quick notes. The material below does not cover RHEL 6.
RHEL 6 is quite old, and additional procedures may be required. This
document explains how to bring RHEL 7 and 8 workstations and servers
up to the currently supported (on |today|) versions, 7.9 and 8.4.

The topics below appear in the order in which you should do them. If 
you have done this procedure previously, you may recognize steps that
you may omit. The processes for updating workstation and server versions
of RHEL are similar enough that in the text below the term *RHEL* can be
applied to either/both.

In the examples below, we show the update program's name as ``yum``. With
RHEL 8, the program's name was changed to ``dnf``. They are work-alikes, so
with most ``yum`` commands you can substitute ``dnf``. In fact, many RHEL 8
machines will have an alias or a symbolic link that will let you type ``yum``
as the command name.

Understanding versions
----------------------

Every software package on Linux has a version number associated with it.
The versions usually consist of three digits (or pairs of digits) 
separated by dots. Most software will tell you the version when you
either run the program with no input, or when you add ``--version`` as
the only argument. Here are two examples. ::

    [~]: python --version
    Python 3.9.5

    [~]: python
    Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02)

- ``3`` is the major version. A change in the major version means that there are some incompatibilities with previous versions (``2``).
- ``9`` is the minor version. This means there were some functional changes between ``3.8`` and ``3.9``, but there should be backward compatibility.
- ``5`` is a patch, also known as a bugfix. 

Despite the dots, versions are not interpreted as decimal numbers. In the
above example, the next minor version is ``3.10`` which is nine versions
ahead of ``3.1``. Got it?

As you might guess, going from RHEL 7 to RHEL 8 is a big change, but going
from RHEL 7.7 to 7.9 or RHEL 8.1 to 8.4 is a much less complex process.

Determine the state of your machine
------------------------------------ 

So which version of RHEL is your computer running, and when was it last
updated? This important question is easy to answer. The followinging
command will print the answer in plain English. ::

    cat /etc/redhat-release

Now when was it last done? ::

    ls -l /etc/redhat-release

If you are already on RHEL 7.9 or RHEL 8.4, you can skip down to step XXXX.

Special privileges
-------------------

Every Linux machine has a user named ``root``. It is not so much that this
user has special abilities, as it is that there are no restrictions on what
this user may do. If you are logged in as ``root``, and you want to remove
every file from all the discs, Linux will not blink, and will promptly 
carry out this disastrous move.

A much safer way to go about the upcoming process is to ask for permission
one command at a time through a polite request -- prefacing the command
with ``sudo``. East coast natives seem pronounce this word *SUE doh*, whereas 
west coast natives say *SUE doo*.

Your regular login ID must be in the file ``/etc/sudoers``, and the way to find
out is to try something safe and simple, like ::

    sudo date

If Linux slaps you down, you will need to be added to the above file. On the 
other hand, if this is your computer, you will probably be OK.

Check the disc space
---------------------

Running out of disc space is inconvenient. Running out of disc space
during an upgrade of the OS is serious problem. Let's find out how
much space you have. ::

    df -h

The result you will see looks something like this, where the middle
row with the ``/`` by itself is the figure that should interest you. ::

    Filesystem                         Size  Used Avail Use% Mounted on
    devtmpfs                            47G     0   47G   0% /dev
    tmpfs                               47G     0   47G   0% /dev/shm
    .....
    /dev/md126p4                       208G   50G  159G  24% /
    .....
    /dev/mapper/urarana_vg1-opt         50G  6.9G   44G  14% /opt
    /dev/mapper/urarana_vg1-home       300G   24G  277G   8% /home

Even ``20G`` in the Avail column is plenty, and it is a matter of 
space rather than percentage full. 

Rebooting
-------------

It is time to reboot the machine. We need to kick off all the users, and
start with everything "clean" to avoid surprises. We will be rebooting 
several times, and this is how you do it. ::

    sudo shutdown --reboot now

In one or two minutes, the computer will be back online.

Finding out what is going on
-----------------------------

OK, let's see who is logged in. There should not be anyone but you, and
the command is easy ::

    [~]: w
 11:14:28 up 0 days, 1 minute,  1 user,  load average: 0.05, 0.05, 0.05
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    gflanagi pts/0    172.29.189.4     11:14    1.00s  0.15s  0.01s w

If you see something like the above, let's proceed. If not, make some 
phone calls and ask people to log out.

What are you key applications on this computer?
------------------------------------------------

We are looking for the BIG APPS that are not a part of 
Linux itself, and that you use for research. R, QGIS, Gaussian, Picard,
AMBER, *etc*. Write down the names and versions of these packages
before the next step.

Update for security first
----------------------------

As Linux sees it, all updates are divided into two groups: updates
that have security implications, and the rest of them. We will do
the security updates first. Let's find out what needs an update that
involves security. ::

    sudo yum check-updates --security

Check the resulting list to see if any of your BIG APPS are on the
list. They probably will not be, but make a note of any that are.

Nothing on the list? Great.  If they differ only in minor version
or patches, you can proceed with minimum worry.  If the difference
is in *major* versions, you should stop and get some help from
someone with more experience.

Now, let's do the security updates. It may take a few minutes, and you
will be asked if it is OK to proceed before the process begins. ::

    sudo yum update --security

For many of the changes to take effect, you will need to reboot the
machine, so ... do it now.

Potential security issues
---------------------------

Linux has become more secure as time passes, and each security update
may hit a few tripwires. Let's see if there are any, and we'll sort it
out later.

1. Run ``w`` like we did to see if anyone else is logged in. The
part of the answer that interests us this time is the load average,
this part. ::

     load average: 0.05, 0.05, 0.05

Numbers well below ``1.0`` should be expected. If you see small
numbers like the above, you can skip to the next step.

If you see load numbers that are close to or above ``1.0``, we need
to find the cause. In this case, we will use the program ``top``
that will show a full-screen list of the most active processes (the
biggest users of CPU). The top part of the table shown on the screen
will look something like this example. ::

       PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      3988 nagios    20   0  776480  37848   3852 S   2.0  0.0 420:32.01 ncpa_listener
      3926 root      20   0 2597032  59544   2848 S   1.0  0.1   2746:20 Eaton-IPP
      3208 root      20   0  120692   6816   1352 S   0.7  0.0 863:01.06 sh

In the right hand column, if you see a process named
``selinuxtroubleshoot`` (or at least the first few letters of that
name), then there is some new program that is in continuous violation
of the new, upgraded security. We need to identify it, stop it, and
deal with it later.

Let's check the security audit log, with this command: ``sudo tail
/var/log/audit/audit.log``.  The ``tail`` command shows the last
few lines of any file, and it is often used to inspect a logfile
that is being updated while the computer runs.

[[[ Put example output here ]]]

Whatever the program is, you can stop it with ``sudo pkill programname``.

Update the rest of the packages
----------------------------------

This is a lather-rinse-repeat of the security updates, but without the 
``--security`` limiting. The lines that start with ``#`` are there just
to remind you of the purpose. ::

    # Find out what remains to be updated.
    sudo yum check-updates 
    # If you don't see your BIG APPs in a different major version,
    sudo yum update
    # Reboot
    sudo shutdown --reboot now

Repeat the preceding step in case the same program is churning away fighting
the new security rules.

Almost finished ....
----------------------

Once in while, and solely due to the order in which we have done the
updates, a package can be left behind, or an update to one package
may cause another one to be slightly out of date. If nothing else, 
a quick check should be reassuring. So .. one .. more .. time ::

    sudo yum update

Probably nothing, and you will be told that there is nothing to update.
