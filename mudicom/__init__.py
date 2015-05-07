# -*- coding: utf-8 -*-
"""
    mudicom
    ~~~~~~~

    A light-weight python package that validates, reads, and extracts images
    from a DICOM file.

    :copyright: (c) 2015 by Eric Bower
    :license: MIT, see :LICENSE.rst: for more information.
"""

__version__ = '0.1.1'

from .base import Dicom
from . import lookup
from .validation import validate

def load(fname, **kwargs):
    """ Imports DICOM file into memory,
    returns a Dicom object.

    :param fname: Location and filename of DICOM file.
    """
    return Dicom(fname, **kwargs)

# Deprecated: backwards compatability
lookup_VR = lookup.VR
lookup_transfer_syntax = lookup.transfer_syntax