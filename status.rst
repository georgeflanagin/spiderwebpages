.. _status:
.. highlight:: rst

.. include:: substitutions.rst

====================================
HPC status (temporary page)
====================================

Pilot installations
~~~~~~~~~~~~~~~~~~~

The list of software that *can* be installed by ACT (the vendor)
will be provided before the cluster is built.  The list is derived
from an informal inventory of existing academic clusters at UR. The
status is given on this four point scale:

``0`` Not yet attempted.

``1`` Installation incomplete.

``2`` Successfully installed, and appears to be operational.

``3`` Smoke test passed successfully.

``4`` Passed test provided by the PI (or other party) associated with the software, 
or they are known to work because they support some other package that has 
passed level 4.

=============================   ======
Package                         Score
=============================   ======
AMBER                             2
Anaconda core packages            4
Apache Ignite Scientific DB       0
Apache webserver                  3
Columbus                          0
GPG keyring for installs          4
Gaussian                          1
Healpy                            4
MySQL and MariaDB                 4
Neo4j                             2
Oracle/XE                         1
PostGreSQL                        3
PyTorch family of software        3
QGIS                              4
Qchem                             1
Quantum Espresso                  2
RStudio                           3
=============================   ======

Map of partitions and nodes in Spydur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*NOTE* click on the image to enlarge it. Your browser's back-button
will return you to this page. 

|nodemap|

Spydur will have one named partition for each item group shown in the partition
map. For example, if a job is submitted to the partition for the ``basic`` nodes 
(384GB of memory), it will be assigned to one of the eight nodes shown in the 
upper right of the diagram, based on availability.  

The technical information about the partitions is shown in the following figure, 
which also can be enlarged by clicking it.

|partitions|

Administrative Training 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SLURM system will be installed by the vendor. It is quite a large system with 
many options, and we have practiced installing and reinstalling it on *ad hoc* 
clusters created for the purpose of learning about it.

This website
~~~~~~~~~~~~~~~~

The BoK related to Spydur will be available on this website (minus this page).


