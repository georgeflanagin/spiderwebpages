.. _installs:
.. highlight:: rst

====================================
Installed software on Spydur
====================================

Legend
~~~~~~~

**Package** --- Admitedly, this is just a name. Some of these are
major systems, some are libraries. The common property is that they
are "units" that can be installed and uninstalled without affecting
something else.

**Version** --- This is supplied by the package provider. Eventually,
there will be multiple versions of quite a few packages. 

**Component** --- Some of the packages have plugins, sub-packages,
or other components that can be installed separately.

**Origin** --- How was it delivered? ``binary`` means the package
provider built it, and we installed it. ``jar`` means it is a program
that must be executed inside the Java virtual machine. ``build``
means we compiled it on Spydur. ``conda`` means that Anaconda was
used to install it. ``CRAN`` means that it is a standard R package.

**CPU** -- ``web`` indicates it is on the webserver only. ``cluster`` means
the compute cluster only. ``both`` means both. 

**Install location** --- The shorthand is that ``$sw`` is ``/usr/local/sw``, the 
mounted file system that is shared across all the compute nodes in the 
cluster. For ``conda`` installs, this is the name of the environment that 
should be enabled to use the software.

**Date** --- When it was installed, nothing more.

**Notes** --- Anything else that needs to be added.
 

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRagrm3HZXGRvky3SW_5mEM8aahebuUCInsAPyRIUN6gi5Z-LMYA2gSqQlYI6Q4LUwkeD-3aHowYI2N/pubhtml" height="500px" width="100%"></iframe>
