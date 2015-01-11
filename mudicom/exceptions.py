# -*- coding: utf-8 -*-
"""
    mudicom.exceptions
    ~~~~~~~~~~~~~~~~~~

    Module for package specific exceptions
"""


class InvalidDicom(IOError):
    """ A DICOM file must have the correct tag to be validated as a
    DICOM file. Read the DICOM standard for more information. """
    pass
