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

* GDCM with python wrapper

Image

* GDCM with python wrapper
* numpy
* Pillow (or matplotlib)

Validate

* GDCM with python wrapper
* dicom3tools

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

Debian (Ubuntu)

.. code:: bash

	$ apt-get install dicom3tools

Max OS X

* Download http://www.dclunie.com/dicom3tools/workinprogress/macexe/
* Unzip
* Move dciodvfy to /usr/local/bin/


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

Debian (Ubuntu)

.. code:: bash

	$ apt-get install cmake

Max OS X

.. code:: bash

	$ brew install cmake

SWIG
~~~~

* PCRE is required for SWIG

.. code:: bash

	$ apt-get install libpcre3 libpcre3-dev

* Download the latest version of SWIG
* Extract compressed file e.g. swig-3.0.2

.. code:: bash

	$ wget http://prdownloads.sourceforge.net/swig/swig-3.0.2.tar.gz
	$ tar -zxvf swig-3.0.2.tar.gz

* Install SWIG

.. code:: bash

	$ cd swig-3.0.2
	$ ./configure
	$ make
	$ make install

Debian (Ubuntu)

.. code:: bash

	$ sudo apt-get install swig3.0

Max OS X

.. code:: bash

	$ brew install cmake

GDCM
~~~~

* Download the latest version of GDCM
* Extract compressed file to desired location e.g. ~/gdcm-2.4.2.tar.gz

.. code:: bash

	$ wget http://tcpdiag.dl.sourceforge.net/project/gdcm/gdcm%202.x/GDCM%202.4.2/gdcm-2.4.2.tar.gz
	$ tar -zxvf gdcm-2.4.2.tar.gz

The trick with GDCM is that the build directory must be separated
from the source directory.  -fPIC flags need to be set for C/C++
and GDCM_WRAP_PYTHON must be turned on.

.. code:: bash

	$ mkdir gdcm-build
	$ cd gdcm
	$ rm CMakeCache.txt
	$ cd ../gdcm-build
	$ cmake ../gdcm-2.4.2 -DCMAKE_C_FLAGS=-fPIC -DCMAKE_CXX_FLAGS=-fPIC -DGDCM_WRAP_PYTHON=ON

If using CCMAKE then do the following:

.. code:: bash

	$ ccmake ../gdcm-2.4.2

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

Mac OS X
--------

GDCM
~~~~

The process is essentially the same as building from source.
Make sure you can build c++ applications

.. code:: bash

	$ brew install llvm --with-clang -stdlib=libc++

Windows
-------

GDCM
~~~~

The easiest way is to simply run the windows installer, which will
also install the python wrappers.

http://sourceforge.net/projects/gdcm/

Then you can copy and paste gdcm.py, gdcmswig.py, and _gdcmswig.so from gdcm/bin into
your python site-packages folder.
