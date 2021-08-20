.. _databasessw:
.. highlight:: rst

====================================
Databases
====================================

MySQL and MariaDB
~~~~~~~~~~~~~~~~~

Installation
----------------

Installation is particularly simple::

    dnf install mariadb-server mariadb-devel

Upgrade
-----------

Use the Redhat Package Manager::

    dnf update mariadb-server mariadb-devel

Remove or disable
---------------------

Use the Redhat Package Manager::

    dnf remove mariadb-server mariadb-devel



Neo4j Graph Database
~~~~~~~~~~~~~~~~~~~~

Installation
----------------

The RPM is signed, and you will need to add the key to the rpm keyring::

    rpm --import https://debian.neo4j.com/neotechnology.gpg.key
    
The neo4j repository may not be in the list, so add these lines to 
a new file named ``neo4j.repo`` in ``/etc/yum.repos.d`` ::

    [neo4j]
    name=Neo4j Yum Repo
    baseurl=http://yum.neo4j.com/stable
    enabled=1
    gpgcheck=1

Now the database can be installed::

    sudo yum install neo4j

The signing key will be used to validate the download.

Upgrade
-----------

Remove or disable
---------------------

Oracle and Oracle/XE
~~~~~~~~~~~~~~~~~~~~~

PostGreSQL and PgAdmin 4
~~~~~~~~~~~~~~~~~~~~~~~~

Apache Ignite NoSQL Databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
