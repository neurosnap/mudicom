
mudicom
========

A python package that validates, reads, and extracts images from a DICOM file.

Requirements
------------

Base:

- Python <= 2.7
- GDCM with python wrapper (https://github.com/neurosnap/mudicom/blob/master/docs/install.rst)

Validator:

- dicom3tools (http://www.dclunie.com/dicom3tools.html)

Image:

- numpy (http://www.numpy.org/)
- PIL (https://github.com/python-pillow/Pillow); or
- Matplotlib (http://matplotlib.org/)

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

Full documentation is available at
https://github.com/neurosnap/mudicom/tree/master/docs (temporary)

Roadmap
-------

- Extract multiple images from one single DICOM file
- Publish documentation online

Credits
-------

Written by Eric Bower

Special thanks to `Mathieu Malaterre`_ (primary developer for GDCM),
of whom without this package would not be possible.

.. _Mathieu Malaterre: https://github.com/malaterre
