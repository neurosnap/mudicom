
mudicom
========

A python package that validates, reads, and extracts images from a DICOM file.

Quick How To
------------

.. code:: python

    import mudicom
    mudicom.Read("ex1.dcm")
    mudicom.Image("ex1.dcm")
    mudicom.Validate("ex1.dcm")

Documentation
-------------

Full documentation is available at https://mudicom.readthedocs.org/

Requirements
------------

- Python 2.7
- GDCM with python wrapper

Credits
-------

Written by Eric Bower

Special thanks to `Mathieu Malaterre`_ (primary developer for GDCM), 
of whom without this package would not be possible.

.. _Mathieu Malaterre: https://github.com/malaterre
