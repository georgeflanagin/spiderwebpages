.. _qesw:
.. highlight:: rst

====================================
Quantum Espresso
====================================
**Note** *there is a bug in gfortran in versions before 4.9, so it is 
necessary to upgrade the gfortran compiler to at least 4.9.*


Quantum Espresso is available in source code distributions from GitHub. 
Begin by downloading the latest stable tarball, which is 6.7 on |today|::

    wget https://github.com/QEF/q-e/releases/download/qe-6.7.0/qe-6.7-ReleasePack.tgz
    tar zxf qe-6.7-ReleasePack.tgz
    cd qe-6.7

At this point, you can continue with the mostly standard set of steps::

    ./configure
    make all
    make install

At the end of the configure step, QE prints a short message to the screen that
is worth examining::

    ESPRESSO can take advantage of several optimized numerical libraries
    (essl, fftw, mkl...).  This configure script attempts to find them,
    but may fail if they have been installed in non-standard locations.
    If a required library is not found, the local copy will be compiled.

Upgrade
-----------

The installation procedure can be repeated with a new tarball, and the insertion
of ``make clean`` before ``make all`` to remove all the previous targets.

Remove or disable
---------------------

