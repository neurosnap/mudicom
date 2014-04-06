
DicomImg
========

A python package that validates, reads, and extracts images from a DICOM file.

Dependencies 
------------
- numpy
- Pillow
- GDCM with python wrapper

Setup
-----

GDCM Python on Debian
~~~~~~~~~~~~~~~~~~~~~

.. code:: bash
    
    apt-get install python-gdcm

GDCM Pythohn from source
~~~~~~~~~~~~~~~~~~~~~~~~


PRE-REQS
~~~~~~~~

.. code:: bash
	$ apt-get install cmake-curses-gui
	$ apt-get install libpcre3 libpcre3-dev

SWIG
~~~~

* Download the latest version of SWIG
* Extract compressed file e.g. swig-2.0.11

.. code:: bash

	$ cd swig-2.0.11
	$ ./configure
	$ make
	$ make install


GDCM
~~~~

* Download the latest version of GDCM
* Extract compressed file to desired location e.g. ~/gdcm.tar.bz2

.. code:: bash

	$ mkdir gdcm-build
	$ cd gdcm
	$ rm CMakeCache.txt
	$ cd ../gdcm-build
	$ ccmake ../gdcm


* Screen will come up,
* Press [T] to go to advanced mode
* SET CMAKE\_C\_FLAGS to -fPIC
* SET CMAKE\_CXX\_FLAGS to -fPIC [Could be optional]
* Press [C] to configure
* SET GDCM\_WRAP\_PYTHON to ON
* [G] to generate

.. code:: bash

	$ make
	$ sudo make install

Create link to python modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to virtualenvs or 
default python site-packages directory 
e.g. ~/.virtualenvs/dcmdb/lib/python2.7/site-packages

Create gdcm.pth file with absolute path to gdcm-build/bin

.. code:: bash

	/home/{user}/gdcm-build/bin

Quick How To
------------

.. code:: python

    import dicomimg as di

Credits
-------

Eric Bower