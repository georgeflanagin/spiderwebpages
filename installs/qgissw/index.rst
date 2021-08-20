.. _qgissw:
.. highlight:: rst

====================================
QGIS 
====================================

Installation
----------------

Use the Redhat Package Manager:: 

    dnf install qgis

To install the development packages, the ``python-pygments`` must
be installed first. This library resides in the repo ``optional-rpms``.
Once added to the list of repos::

    dnf install qgis-devel
    dnf install qgis-server

The above actions will also install the ``qgis-python`` and 
``qgis-grass`` packages.

Upgrade
-----------

Use the Redhat Package Manager::

    dnf update qgis
    dnf update qgis-server
    dnf update qgis-devel

Remove or disable
---------------------

Use the Redhat Package Manager:: 

    dnf remove qgis


