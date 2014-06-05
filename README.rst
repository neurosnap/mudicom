
mudicom
========

A python package that validates, reads, and extracts images from a DICOM file.

Dependencies 
------------
- numpy
- Pillow (or matplotlib)
- GDCM with python wrapper
- dicom3tools

Setup
-----

GDCM Python on Debian
~~~~~~~~~~~~~~~~~~~~~

.. code:: bash
    
    $ apt-get install python-gdcm

If you are using virtualenv then you must create symbolic links 
from /usr/lib/python2.7/dist-packages to virtualenv folder.  See 
below for a quick how-to

GDCM Python from source on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

	$ sudo apt-get install swig2.0

OR 

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
* SET CMAKE\_CXX\_FLAGS to -fPIC
* Press [C] to configure
* SET GDCM\_WRAP\_PYTHON to ON
* [G] to generate

.. code:: bash

	$ make
	$ sudo make install

Virtualenvs: Create link to python modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to virtualenvs or 
default python site-packages directory 
e.g. ~/.virtualenvs/mudicom/lib/python2.7/site-packages

Create symbolic links to absolute path of gdcm.py gdcmswig.py _gdcmswig.so

.. code:: bash

	$ ln -s /usr/lib/python2.7/dist-packages/gdcm.py /virtalenv/path/python/site-packages/gdcm.py
	$ ln -s /usr/lib/python2.7/dist-packages/gdcmswig.py /virtualenv/path/python/site-packages/gdcmswig.py
	$ ln -s /usr/lib/python2.7/dist-packages/_gdcmswig.so /virtualenv/path/python/site-packages/_gdcmswig.so

GDCM on Windows
~~~~~~~~~~~~~~~

The easiest way is to simply run the windows installer, which will
also install the python wrappers.

http://sourceforge.net/projects/gdcm/

Then you can copy and paste gdcm.py, gdcmswig.py, and _gdcmswig.so from gdcm/bin into
your python site-packages folder.


Dicom3Tools (Validator)
~~~~~~~~~~~~~~~~~~~~~~~

http://www.dclunie.com/dicom3tools/dciodvfy.html

Debian:

.. code:: bash

    $ sudo apt-get install dicom3tools


Quick How To
------------

.. code:: python

    import mudicom
    mudicom.Read("ex1.dcm")
    mudicom.Image("ex1.dcm")
    mudicom.Validate("ex1.dcm")

Credits
-------

Eric Bower

Special thanks to `Mathieu Malaterre`_ (primary developer for GDCM), 
of which none of this would be possible.

.. _Mathieu Malaterre: https://github.com/malaterre
