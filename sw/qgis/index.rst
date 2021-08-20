.. _module:
.. highlight:: rst

====================================
QGIS
====================================

Description
~~~~~~~~~~~~

QGIS is a professional GIS application that is built on top of and
proud to be itself Free and Open Source Software (FOSS).  QGIS is
generally used interactively to draw maps. It is also possible to
use it non-interactively.

Contacts
~~~~~~~~~~

- `Beth Zizzamia <https://directory.richmond.edu/bios/bzizzami/>`_ / GIS Operations Mgr & Tech / Geography Department / bzizzami / 804.484.1545
- `Dr. Guoping Huang <https://directory.richmond.edu/bios/ghuang/>`_ / Interim Spatial Analysis Lab Director and Visiting GIS Lecturer / Geography Department / ghuang / 804.484.1518

Samples, kits, and getting started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use QGIS interactively, you will need to have X-windows (X11)
installed on your desktop computer. This will support your being
able to see the output of QGIS immediately. When connecting to
Spydur, it is necessary to specify that you want an X-windwos
connection::

    ssh -Y netid@spydur

If you need help installing X-windows, please contact the Help Desk
in one of these convenient ways::

    804.287.6400
    helpdesk@richmond.edu
    

Additional documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS maintains a full set of online documentation 
at https://docs.qgis.org/3.16/en/docs/index.html

Quirks, gotchas, and other advisories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although *multi-threaded* and *multi-processing* are often used
interchangeably, there is a meaningful difference between the two.
QGIS is *not* multi-threaded, only *multi-processing* meaning that
it can divide the processing between several cores in an environment
like Spydur.

Nonetheless, it is important to set the value for the awkwardly
named parameter ``QGIS_SERVER_MAX_THREADS`` to the number of cores
you have reserved in your SLURM job. If you do not do so, QGIS will
try to use every available core on the node, and if this exceeds the
number you requested, your job will fail.

Maintenance
~~~~~~~~~~~~~~~~~~~~

Module file[s]
------------------

No module file is required to use QGIS.

SLURM skeleton
-------------------------

There is a skeleton SLURM file you can use as a starting point
at ``/home/installer/skeletons/qgis.slurm``.
