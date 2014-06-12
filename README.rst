
mudicom
========

A python package that validates, reads, and extracts images from a DICOM file.

Quick How To
------------

.. code:: python

    import mudicom
    mu = mudicom.load("mudicom/tests/dicoms/ex1.dcm")
    # returns array of data elements as dicts
    mu.read()
    # returns dict of errors and warnings for DICOM
    mu.validate()
    # creates image object
    img = mu.image()
    # returns numpy array
    img.numpy()
    # using Pillow, saves DICOM image
    img.save_as_pil("ex1.jpg")
    # using matplotlib, saves DICOM image
    img.save_as_plt("ex1_2.jpg")

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
