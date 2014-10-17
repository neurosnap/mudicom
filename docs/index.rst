.. mudicom documentation master file, created by
   sphinx-quickstart on Sat Jun  7 23:03:23 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mudicom's documentation!
===================================

Contents:

Mudicom is a light-weight python package that wraps around other tools that are widely used
in the open-source community to read, extract images, and validate DICOM files.
There are two critical libraries that mudicom depends upon:

*  GDCM_ (C++)
*  dicom3tools_ (C++, command line tools)

.. _GDCM: http://sourceforge.net/projects/gdcm/

.. _dicom3tools: http://www.dclunie.com/dicom3tools.html

Mudicom also depends upon 2-3 python packages:

*  numpy_ (Image manipulation)
*  matplotlib_ (Image saving)
*  PIL_ (Image saving)

.. _numpy: http://www.numpy.org/

.. _matplotlib: http://matplotlib.org/

.. _PIL: http://pillow.readthedocs.org/en/latest/

Either matplotlib or PIL is required for saving an image,
which up to the user's preference.
I have found that matplotlib yields better quality images,
but it's mainly because of color mapping.

Once dependencies have been installed, the package has the ability to read
DICOM elements, manipulate DICOM image data using numpy, and validate DICOM
elements to ensure the file conforms to the DICOM standard.

.. toctree::
   :maxdepth: 3

   install
   tutorial
   api_reference
   transfer_syntax
   upcoming
   contribute
   authors


