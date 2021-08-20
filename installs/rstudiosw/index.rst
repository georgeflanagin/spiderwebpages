.. _rstudiosw:
.. highlight:: rst

====================================
R-Studio
====================================

For R-Studio to work, R must be installed. R comes from Redhat, and
as such it must be installed by root (this can take a while)::

    dnf install R

*NOTE:* R-studio will install the software *anyway*, even if R is not
present. Just because it installs does not mean it will be usuable, or
even complain during the installation.

R-Studio builds are signed with their key, and it must be
installed on the local keyring along with being added to the rpm keyring::

    gpg --keyserver keys.gnupg.net --recv-keys 3F32EE77E331692F
    gpg --export --armor 3F32EE77E331692F > rstudio-signing.key
    rpm --import rstudio-signing.key

R-Studio must be installed by the root user::

    wget https://download2.rstudio.org/server/centos8/x86_64/rstudio-server-rhel-1.4.1717-x86_64.rpm
    # Validate the build.
    rpm -K rstudio-server-rhel-1.4.1717-x86_64.rpm
    # Install it.
    sudo dnf install rstudio-server-rhel-1.4.1717-x86_64.rpm

Now verify everything is present. The following instruction will print 
*nothing* if all is well, otherwise it will tell you what is missing::

    sudo rstudio-server verify-installation

At this point, it is time to start it::

    sudo rstudio-server start

The configuration can be lightly self-tested with the following command::

    /usr/lib/rstudio-server/bin/rserver --test-config
