=======
Install
=======

This is a step-by-step guide on how to properly install
mudicom.  

Dependencies
------------

There are three main classes in mudicom, each with different
dependencies:

Read
- GDCM with python wrapper

Image
- GDCM with python wrapper
- numpy
- Pillow (or matplotlib)

Validate
- GDCM with python wrapper
- dicom3tools

Linux (Ubuntu)
--------------

Install GDCM with Python
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

	$ apt-get install python-gdcm 

By default, this apt repository installs python into:
/usr/lib/python2.7/dist-packages

Install dicom3tools
~~~~~~~~~~~~~~~~~~~

The best DICOM validator that I have found is dciodvfy,
which is a command-line utility part of the dicom3tools_
toolchain:

.. _dicom3tools: http://www.dclunie.com/dicom3tools/dciodvfy.html

.. code:: bash

	$ apt-get install dicom3tools

Virtualenv (optional)
~~~~~~~~~~~~~~~~~~~~~

Make a virtualenv (optional but highly recommended).

.. code:: bash

	$ mkvirtualenv mudicom

Create symbolic links to absolute path of gdcm.py, gdcmswig.py, and _gdcmswig.so

.. code:: bash

	$ ln -s /usr/lib/python2.7/dist-packages/gdcm.py /virtalenv/path/python/site-packages/gdcm.py
	$ ln -s /usr/lib/python2.7/dist-packages/gdcmswig.py /virtualenv/path/python/site-packages/gdcmswig.py
	$ ln -s /usr/lib/python2.7/dist-packages/_gdcmswig.so /virtualenv/path/python/site-packages/_gdcmswig.so

Test GDCM python package
~~~~~~~~~~~~~~~~~~~~~~~~

Test to make sure GDCM can be imported into python:

.. code:: bash

	$ python
	>>> import gdcm
	>>> exit()

Install python dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

	$ pip install numpy Pillow mudicom

Source
------

GDCM uses cmake (ccmake) and SWIG to compile and to create a python wrapper
around it.

CMAKE
~~~~~~

* Download Cmake_
* Extract compressed file

.. _Cmake: http://www.cmake.org/cmake/resources/software.html

.. code:: bash

	$ cd cmake
	$ ./configure
	$ make
	$ make install

OR

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

Windows
-------

GDCM
~~~~

The easiest way is to simply run the windows installer, which will
also install the python wrappers.

http://sourceforge.net/projects/gdcm/

Then you can copy and paste gdcm.py, gdcmswig.py, and _gdcmswig.so from gdcm/bin into
your python site-packages folder.